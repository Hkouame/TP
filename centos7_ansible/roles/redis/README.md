Ansible Redis role
==================

This role installs a Redis server

Role Variables
--------------

Variable | Default value |Description
---------|---------------|--------------
redis_packages | (depends on distribution) | List of packages to install
redis_setting_ulimit | 65536 | Limit for the number of open files on the OS (ulimit -n)
redis_setting_bind_address | 0.0.0.0 | Bind address for service
redis_setting_port | 6379 | Port for service
redis_setting_databases | 16 | Number of databases
redis_setting_save | [ "86400 1" ] | List of frequencies at which to save the redis database (see Redis doc.) 
redis_setting_appendonly | yes |
redis_setting_appendfsync | everysec | Other possible values are always or no
redis_setting_no_append_fsync_on_rewrite | 'yes' |
redis_setting_auto_aof_rewrite_percentage | 100 |
redis_setting_auto_aof_rewrite_min_size | 64mb |
redis_setting_maxmemory | 268435456  | Redis memory limit (bytes)
redis_setting_maxmemory_policy | volatile-ttl | Redis memory policy
redis_setting_maxmemory_samples | 20 |

Example Playbook
----------------

```YAML
---
- hosts: servers
  roles:
    - ansible-redis
```

License
-------

BSD

