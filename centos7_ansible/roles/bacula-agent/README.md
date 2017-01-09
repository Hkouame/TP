bacula-agent
=========

This module deploy the bacula-agent


Role Variables
--------------

| Variables               |     Default values           |   Descriptions                     |
| ------------------------|:--------------------------- :| ----------------------------------:|
| `bacula_fd_port`        | 9102                         | Port of bacula client              |
| `bacula_fd_name`        | {{ ansible_fqdn }}           | Bacula file daemon name            |
| `bacula_fd_password`    | changeme                     | password for file daemon password  |
| `bacula_fd_max_concurrent_job` | 5                     | client maximum concurrent jobs for multi streaming |
| `bacula_fd_restore_dir` | /var/lib/bacula-restores     | Restore directory                  |
| `bacula_fd_heartbeat_interval` | 60                    | Heartbeat interval to maintain active connexion with director |
| `bacula_dir_host`       | bacula                       | Serveur address IP                 |
| `bacula_dir_name`       | {{ bacula_dir_host }}        | Name of director                   |
| `filesets`              |                              | Include/exclude list of file and directory to backup according to client inventory group appartenance |


Dependencies
------------

None

Example Playbook
----------------

Simple example for test :

```YAML
---
- hosts: bacula-agent
  roles:
  - role: bacula-agent 
    bacula_dir_host: bacula
```

Simple example for production :

```YAML
---
- hosts: bacula-agent
  roles:
  - role: bacula-agent
    bacula_dir_host: bacula
    bacula_fd_password: S3cr3Tp@ssw0rD
    filesets:
      - name: bacula-agent
        include:
          - /etc/
          - /usr/local/bin
          - /usr/local/sbin
          - /var/spool/cron
      - name: haproxy
        include:
          - /etc/haproxy
```


Author Information
------------------
```
 michel.graba@smile.ci, koffi.michel74@gmail.com,sysadmins at smile-ci,www.smile.ci
```
