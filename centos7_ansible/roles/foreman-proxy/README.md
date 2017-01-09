Role Name
=========

Install and configure DNS foreman-proxy.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `foreman_server` | 127.0.0.1 | IP address of foreman server |
| `foreman_proxy_http_port` | 8000 | Default port used by server to connect to proxy |
| `foreman_proxy_dns_enable` | true | Enable DNS proxy |
| `foreman_proxy_dns_ttl` | 14400 | Default DNS TTL entry |
| `foreman_proxy_dns_key` | /etc/named/Knsupdate.key | Dynamic DNS Key to used by foreman |

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```YAML
- hosts: bind
  roles:
  - role: foreman-proxy
    foreman_server: katello.rp.smile.lan
```
