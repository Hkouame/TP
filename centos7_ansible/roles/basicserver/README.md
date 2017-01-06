Basic server
============

This role describes a basic server, and contains all Smile best practices with regards to locales, default packages, shell and editor config

Prompt configuration
--------------------

The following variable allows you to alter the default prompt (light green) :

* `promptcolor: red`

You can choose the prompt color among ANSI colors : black, red, green, yellow, blue, magenta, cyan, white

Install additionnal packages
----------------------------

The following variable allows you to install additionnal packages :

* `extra_packages`

It takes a list of packages to install

Sudoers configuration
---------------------

The following variables allow you to configure sudo on your server :

* `install_sudoers`: set it to `true` to install a sudoers file
* `sudo_allowed_root_commands`: a list of commands the `smile` user can run as root without password
* `sudo_allowed_users` : a list of users the `smile` user can impersonate without password

Shell aliases, environment variables, etc
-----------------------------------------

You can provide a template that will be copied to `/etc/profile.d` on the server:

* `profiled_template: templates/my_shell_config.j2`

Delivery users
--------------

You can ask the script to create a delivery user for your applications

```
delivery_users:
    - name: smile
      group: www-data
      sshkey:
        - "{{ lookup('file', 'user1.pub') }}"
        - "{{ lookup('ldapkey', 'mabes') }}"
```

`authorized_keys` is not mandatory, if present, you should give it a list of SSH keys that should be enabled for the user

SSH Key LDAP lookups
--------------------

This role adds a new lookup plugin called `ldapkey`, you can use it to lookup SSH keys by login from the Smile LDAP.

In order to use this feature, you need to install `python-ldap` on the machine running Ansible

Anywhere in your playbook, you can use :

```
{{ lookup('ldapkey', 'login') }}
```


Or you can use it in tasks

```
- authorized_key: user=charlie key="{{ item }}"
  with_ldapkey:
    - mabes
    - rogon
```

### Configuration (optional)

By default, it will fetch keys from `directory.vitry.intranet`. If this server isn't accessible to you, of if you want to change some parameters, you can define the URL yourself :

```
    vars:
        lookup_ldapkey_url: ldaps://ldap.prod.vitry.intranet/
```

The `lookup_ldapkey_url` takes a RFC4516 LDAP URL.

You may also override the search filter, base DN, scope, or return attribute

```
    vars:
        lookup_ldapkey_url: "ldaps://directory.vitry.intranet/ou=users,dc=smile,dc=fr?sshPublicKey?sub?(&(!(pwdAccountLockedTime=000001010000Z))(uid=%s))"\
        lookup_ldapkey_binddn: "cn=admin,dc=smile,dc=fr"
        lookup_ldapkey_bindpw: "password"
```

`%s` in the search filter will be replaced by the lookup key
