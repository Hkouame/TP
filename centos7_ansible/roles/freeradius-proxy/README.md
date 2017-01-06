Freeradius-MySQL
=========

This role install and configure FreeRadius Proxy Serveur and load balance connexion on a pool of freeradius serveur.

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `freerad_prx_lb_type` | load-balance | Type of load balancing used (load-balance, fail-over) |
| `freerad_prx_rq_type` | auth+acct | Type of request to proxy. By default, both authentication and accounting |
| `freerad_prx_secret` | testing123 | Password use to initialize connexion with freeradius server |
| `freerad_prx_port` | 1812 | Freeradius default port for authentication |
| `freerad_prx_home_server` | ['localhost'] | Server list to forward request |


Dependencies
------------

freeradius

Example Playbook
----------------

Simple example :

```YAML
---
- hosts: freeradius-proxy
  roles:
     - role: freeradius-proxy
       freerad_client_vhost: proxy
       freerad_prx_home_server: "{{ groups['freeradius-server'] }}"
```

Complete example with freeradius serveur and freeradius proxy (freeradius-server must be deploy before proxy) :
```YAML
---
- hosts: freeradius-server
  roles:
     - freeradius

- hosts: freeradius-proxy
  roles:
     - role: freeradius
       freerad_client_vhost: proxy
     - role: freeradius-proxy
       freerad_prx_home_server: "{{ groups['freeradius-server'] }}"
```
