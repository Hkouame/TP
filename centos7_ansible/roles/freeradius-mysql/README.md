Freeradius-MySQL
=========

This role install and configure FreeRadius MySQL module backend and create user/database/access in MySQL server.

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `freerad_db_driver` | mysql | Drive use bu FreeRADIUS to access database backend |
| `freerad_db_host` | localhost | host used by FreeRADIUS module to access MySQL database |
| `freerad_db_port` | 3306 | port used by FreeRADIUS module to connect to MySQL database |
| `freerad_db_user` | radius | username used by FreeRADIUS module to access MySQL database |
| `freerad_db_pass` | changeme | password used by FreeRADIUS module to access MySQL database |
| `freerad_db_name` | radius | MySQL database name use by FreeRADIUS module |
| `freerad_db_remote_host` | localhost | Ansible use delegate\_to option to provision MySQL database (create user, database, table and user access) on a remote host |
| `freerad_db_admin_user` | root | MySQL admin user used to connect to database localy for creation operations |
| `freerad_db_admin_pass` | changeme | MySQL admin password to connect to database localy for creation operations |


Dependencies
------------

freeradius

Example Playbook
----------------

Simple example :

```YAML
---
- hosts: freeradius-server
  roles:
     - freeradius
     - role: freeradius-mysql
       freeradius_db_host: 192.168.122.52
```

Complexe example :

```YAML
---
- hosts: freeradius-server
  roles:
     - role: freeradius
       freerad_enable_serverstatus: true
       freerad_server_thread_start: 32
       freerad_server_thread_max: 64
       freerad_server_thread_minspare: 10
       freerad_server_thread_maxspare: 20
     - role: freeradius-mysql
       # MySQL account used to access freeradius database by SQL module
       freerad_db_driver: mysql
       freerad_db_host: freeradius-db
       freerad_db_port: 3306
       freerad_db_user: radius-ffth
       freerad_db_pass: jCYFWdOONlgo8RSA
       freerad_db_name: radius_ftth
       # MySQL admin account used to init freeradius database
       freerad_db_remote_host: freeradius-db
       freerad_db_admin_user: root
```
