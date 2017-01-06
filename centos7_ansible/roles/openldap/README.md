OpenLDAP server
===============

This role installs an OpenLDAP server


Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.


Variable | Default value |Description
---------|---------------|--------------
`openldap_backend` | mdb | The backend module to use
`openldap_suffix`|  dc=example,dc=com | Suffix for the LDAP database
`openldap_rootdn` | cn=admin,dc=example,dc=com | The admin DN
`openldap_rootpw` | | The global admin password, if you want to use one
`openldap_ldif`|  | A LDIF file to load, use "example.ldif" to load role-provided sample data
`openldap_overlays` | | A list of overlays to activate (see below)
`openldap_config` | | A dictionary of key-value configuration directives
`openldap_config_extra` | | A dictionary of key-value configuration directives (for per-environment overrides)

Currently supported overlays :
* `ppolicy`



Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        openldap_rootdn: cn=admin,dc=example,dc=com
        openldap_rootpw: admin
        openldap_ldif: example.ldif
      roles:
         - ansible-openldap

License
-------

BSD

