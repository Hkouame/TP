OCIT SELinux Agent Policy
=========

Configure SELinux policy for NRPE and Bacula File Daemon on CentOS 7

Requirements
------------

Bacula FD and NRPE must be installed.

Role Variables
--------------

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `deploy_baculafd_policy` | true  | Deploy SELinux policy for Bacula FD |
| `deploy_nrpe_policy` | true  | Deploy SELinux policy for NRPE |


Dependencies
------------

None.

Example Playbook
----------------

```YAML
    - hosts: all
      roles:
         - ocit-selinux
```
