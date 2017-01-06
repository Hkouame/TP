Csync2 - Lsyncd
=========

This module install and configure csync2 + lsyncd for Debian and RedHat.

Requirements
------------

Host in group must be resolved by their name return by **uname -n**.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory.

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `lsyncd_enabled` | false | Enable/disable lsyncd |
| `lsyncd_log_dir` | /var/log/lsyncd | Log directory |
| `lsyncd_log_file` | /var/log/lsyncd/lsyncd.log | Log file |
| `lsyncd_max_user_watches` | 4194304 | lsyncd max user watches |
| `lsyncd_status_file` | /var/log/lsyncd/lsyncd.status | status lsyncd file |
| `lsyncd_delay` | 5 | lsyncd delay sync option |
| `lsyncd_max_processes` | 1 | lsyncd max processes |
| `csync2_config_per_group` | true | Deploy csync2 configuration in one file per group instead of all in one file |
| `csync2_bash_logout` | false | Add bash_logout block to check file to synchronise before logout |
| `csync2_key_path` | {{ csync2_conf_dir }}/csync2.key | key csync2 |
| `csync2_backup_folder` | /var/backups/csync2 | Csync2 backup folder |
| `csync2_backup_generations` | 0 | Csync2 backup generations |
| `csync2_groups` | **mandatory** | Declare synchronisation group |
| `csync2_groups.name` | **mandatory** | Synchronisation group name |
| `csync2_groups.auto` | younger | Conflict auto resolution mode |
| `csync2_groups.includes` |  | Files list include in synchronisation |
| `csync2_groups.excludes` |  | Files list to exclude to synchronisation |
| `csync2_groups.actions` |  | Actions to excecute when files matching patterns was modified |
| `csync2_groups.actions.pattern` |  | Pattern to match for executing action |
| `csync2_groups.actions.exec` |  | Command ro tun when action is executed |
| `csync2_groups.actions.do-local` | false | If defined, execute command localy |

Dependencies
------------

None

Example Playbook
----------------

An example of playbook with csync2 only

```
---
- name: Configure csync2
  hosts: front-web
  roles:
    - role: csync2-lsyncd
      csync2_hosts: "{{ groups['front-web'] }}"
      csync2_backup_generations: 3
      csync2_config_per_group: false
      csync2_bash_logout: true
      csync2_groups:
        - name: httpd
          auto: younger # Default: younger
          includes:
            - /var/www/application
            - /etc/http
          excludes:
            - /var/www/application/logs
          actions:
            - name: httpd
              pattern: '/etc/httpd/*'
              exec: 'service httpd reload'
              do_local: true
```

An example of playbook with lsyncd

```
---
- name: Configure csync2 + lsyncd
  hosts: front-web
  roles:
    - role: csync2-lsyncd
      csync2_hosts: "{{ groups['front-web'] }}"
      csync2_backup_generations: 3
      lsyncd_enabled: true # Default: false
      csync2_groups:
        - name: httpd
          includes:
            - /var/www/application
            - /etc/http
          excludes:
            - /var/www/application/logs
          actions:
            - name: httpd
              pattern: '/etc/httpd/*'
              exec: 'service httpd reload'
              do_local: true
```

License
-------

BSD

Author Information
------------------

jean-vincent KASSI: jekas@smile.ci
