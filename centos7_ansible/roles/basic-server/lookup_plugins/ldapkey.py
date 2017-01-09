#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError

try:
    import ldap, ldapurl, ldap.filter
except ImportError:
    raise AnsibleError(
        "You must install python-ldap on the Ansible client to use the ldapkey plugin")

import collections

from ansible.plugins.lookup import LookupBase

try:
        from __main__ import display
except ImportError:
        from ansible.utils.display import Display
        display = Display()

DEFAULT_LDAP_HOSTPORT = "10.100.60.20"
DEFAULT_LDAP_DN = "dc=smileci,dc=lan"
DEFAULT_LDAP_URLSCHEME = "ldap"
DEFAULT_LDAP_ATTRS = ['sshPublicKey']
DEFAULT_LDAP_SCOPE = ldapurl.LDAP_SCOPE_SUBTREE
DEFAULT_LDAP_FILTERSTR = '(uid=%s)'

class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        ret = []
        try:
            ldapurlstr = variables["lookup_ldapkey_url"]
            ldap_binddn = variables["lookup_ldapkey_binddn"]
            ldap_bindpw = variables["lookup_ldapkey_bindpw"]


            for term in terms:
               display.debug("LDAP key lookup term: %s" % term)
               ret.append(self.ldap_get_key(ldapurlstr, term, ldap_binddn, ldap_bindpw))
            return ret
        except KeyError:
            ldapurlstr = "ldaps:///"

    def ldap_parse_config(self, ldapurlstr):
        ldap_params = ldapurl.LDAPUrl(ldapurlstr)

        if not ldap_params.urlscheme:
            ldap_params.urlscheme = DEFAULT_LDAP_URLSCHEME

        if not ldap_params.hostport:
            ldap_params.hostport = DEFAULT_LDAP_HOSTPORT

        if not ldap_params.dn:
            ldap_params.dn = DEFAULT_LDAP_DN

        if not ldap_params.attrs:
            ldap_params.attrs = DEFAULT_LDAP_ATTRS

        if not ldap_params.scope:
            ldap_params.scope = DEFAULT_LDAP_SCOPE

        if not ldap_params.filterstr:
            ldap_params.filterstr = DEFAULT_LDAP_FILTERSTR


        return ldap_params


    def ldap_get_key(self, ldapurlstr, login, ldap_binddn, ldap_bindpw):

        config = self.ldap_parse_config(ldapurlstr)

        filterstr = ldap.filter.filter_format(config.filterstr, [login])

        ldaph = ldap.initialize(config.initializeUrl())

        # if bindpw is defined
        if ldap_bindpw:
            ldaph.simple_bind_s(ldap_binddn, ldap_bindpw)


        searchr = ldaph.search_s(config.dn, config.scope, filterstr,
                                 config.attrs)


        if len(searchr) == 1:
            entry = searchr[0]
            try:
                return str(entry[1].popitem()[1][0])
            except (IndexError, KeyError):
                raise AnsibleError(
                    "Could not find SSH key for user {}".format(login))

        else:
            raise AnsibleError(
                "Could not find user {} in the LDAP".format(login))
