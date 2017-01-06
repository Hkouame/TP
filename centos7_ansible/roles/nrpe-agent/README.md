Role Name
=========

This role install, configure NRPE/SElinux/Firewall

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `nrpe_bind_address` | 0.0.0.0 | NRPE bind address |
| `nrpe_allowed_hosts` | ['127.0.0.1'] | Array list of poller host allowed to monitor server |
| `nrpe_dont_blame` | 1 | Allow NRPE to accept arguments |
| `nrpe_server_port` | 5666 | NRPE listening port  |
| `nrpe_enable_sepolicy` | true | Install SELinux policy for NRPE plugins (most of them are for Smile plugins) |

Dependencies
------------

None.

Example Playbook
----------------

Simple example, installing and configuring NRPE :

``` YAML
- hosts: centreon-agent
  roles:
    - role: centreon-agent
      nrpe_allowed_hosts: ['192.168.122.10']
```
