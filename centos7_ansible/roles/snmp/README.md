SNMP
=========

This role install and configure snmpd service

Requirements
------------

No requirements

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory.

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `snmp_community` | public | Community name |
| `snmp_allow_clients` | 127.0.0.1 | ip address of snmpd clients |

Dependencies
------------

Nothing

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: servers
  roles:
   - role: snmp
     snmp_community: public
     snmp_allow_clients:
       - 10.100.60.37
       - 127.0.0.1
```

License
-------

BSD

Author Information
------------------

* Jean-Vincent KASSI (jekas@smile.ci)
