# HAProxy

This role install a HAProxy on RedHat/CentOS and Debian/Ubuntu Linux servers.

**Note**: This role _officially_ supports HAProxy versions 1.4 or 1.5. Future versions may require some rework.

## Requirements

None.

## Role Variables

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `haproxy_socket` | /var/lib/haproxy/stats | The socket through which HAProxy can communicate (for admin purposes or statistics). To disable/remove this directive, set `haproxy_socket: ''` (an empty string) |
| `haproxy_chroot` | /var/lib/haproxy | The jail directory where chroot() will be performed before dropping privileges. To disable/remove this directive, set `haproxy_chroot: ''` (an empty string). Only change this if you know what you're doing!  |
| `haproxy_admin_bind` | 127.0.0.1:8080 | Bind address:port for admin stats monitoring |
| `haproxy_admin_user` | admin | User to connect to HAProxy admin interface |
| `haproxy_admin_pass` | admin | Password used to connect to HAProxy admin interface |
| `haproxy_admin_state` | enable | Enable/Disable HAProxy admin interface |
| `haproxy_nagios_monitor` | true | Enable/Disable nagios to use socket to monitor HAProxy |
| `haproxy_mode` | http | Default HAProxy mode (http, tcp) |
| `haproxy_balance_method` | roundrobin | Number of shard per index |
| `haproxy_backend_servers` |  | A list of backend servers (name, address, check options) to which HAProxy will distribute requests |

## Dependencies

None.

## Example Playbook

Simple example :

```YAML
---
- hosts: all
  roles:
    - role: haproxy
      haproxy_pool_servers:
        - name: web
          vip: 192.168.122.6
          port: 80
          haproxy_backend_servers: 
            - { name: 'web-1', address: '192.168.122.25:80' }
            - { name: 'web-2', address: '192.168.122.26:80' }
```

Complexe example :

```YAML
---
- hosts: haproxy
  roles:
    - role: haproxy
      haproxy_admin_user: admin
      haproxy_admin_pass: admin
      haproxy_pool_servers:
        - name: web-server
          vip:
            - 172.18.0.81
            - 172.16.3.98
          port: 80
          haproxy_backend_servers: 
            - { name: 'web-server-1', address: '172.16.3.183:80' }
            - { name: 'web-server-2', address: '172.16.3.184:80' }
        - name: tomcat-server
          vip:
            - 172.18.0.82
            - 172.16.3.99
          port: 8081
          options:
            - 'option httpchk OPTIONS /stats'
            - 'balance url_param JSESSIONID check_post'
            - 'cookie  JSESSIONID prefix'
          haproxy_backend_servers: 
            - { name: 'tomcat-server-1', address: '172.16.3.179:8081' }
            - { name: 'tomcat-server-2', address: '172.16.3.180:8081' }
        - name: galera-server-rw
          vip:
            - 172.18.0.84
            - 172.16.3.109
          port: 3306
          mode: tcp
          haproxy_backend_servers: 
            - { name: 'galera-server-rw-1', address: '172.16.3.187:3306', options: 'check port 9200' }
            - { name: 'galera-server-ro-1', address: '172.16.3.188:3306', options: 'check port 9200 backup' }
            - { name: 'galera-server-ro-2', address: '172.16.3.189:3306', options: 'check port 9200 backup' }
        - name: galera-server-ro
          vip:
            - 172.18.0.85
            - 172.16.3.116
          port: 3306
          mode: tcp
          haproxy_backend_servers: 
            - { name: 'galera-server-rw-1', address: '172.16.3.187:3306', options: 'check port 9200 backup' }
            - { name: 'galera-server-ro-1', address: '172.16.3.188:3306', options: 'check port 9200' }
            - { name: 'galera-server-ro-2', address: '172.16.3.189:3306', options: 'check port 9200' }
```
