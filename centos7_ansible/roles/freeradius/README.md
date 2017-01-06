Freeradius
=========

This role install a FreeRADIUS server and deploy admin scripts.

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `freerad_deploy_admin_scripts` | true  | Deploy admin scripts (freeradius-debug, freeradius-checklog, etc) |
| `freerad_enable_controlsocket` | true | Flag to enable control socket listenner |
| `freerad_enable_serverstatus` | true | Flag to enable server status listenner |
| `freerad_client_ipaddr` | 127.0.0.1 | Default client IP used for local test |
| `freerad_client_secret` | testing123 | Default client secret used for local test |
| `freerad_client_vhost` | default | Default vhost used when a request is handle for this client |
| `freerad_log_destination` | syslog | Where to send log. Can be : files, syslog, stderr, stdout |
| `freerad_server_thread_start` | 32 | Number of thread to start initially |
| `freerad_server_thread_max` | 64 | Limit on the total number of servers running |
| `freerad_server_thread_minspare` | 10 | Minimum number of thread waiting for a connexion |
| `freerad_server_thread_maxspare` | 20 | Maximum number of thread waiting for a connexion |

Dependencies
------------

None.

Example Playbook
----------------

Simple example :

```YAML
---
- hosts: freeradius-server
  roles:
   - freeradius
```

Complete example with proxy, radius serveur using MariaDB backend with HAProxy forLoad balancing:
```YAML
---
- hosts: freeradius-proxy
  roles:
     - role: freeradius
       freerad_client_vhost: proxy
     - role: freeradius-proxy
       freerad_prx_home_server: "{{ groups['freeradius-server'] }}"

- hosts: freeradius-server
  roles:
     - freeradius
     - role: freeradius-mysql
       freerad_db_host: haproxy
       freerad_db_remote_host: glra-rw-1

- hosts: galera
  roles:
    - role: mariadb-galera-cluster
      galera_cluster_nodes_group: galera

- hosts: haproxy
  roles:
    - role: haproxy
      haproxy_mode: tcp
      haproxy_pool_servers:
        - name: galera
          vip:
            - 192.168.122.20
          port: 3306
          haproxy_backend_servers: 
            - { name: 'glra-rw-1', address: '192.168.122.23:3306', options: 'check port 9200' }
            - { name: 'glra-ro-1', address: '192.168.122.24:3306', options: 'check port 9200' }
            - { name: 'glra-ro-2', address: '192.168.122.25:3306', options: 'check port 9200' }
    - role: keepalived
      keepalived_vrrp_instance:
        GALERA:
          interface: eth1
          vrid: 128
          pass: changeme
          vip:
            - 192.168.122.20
```
