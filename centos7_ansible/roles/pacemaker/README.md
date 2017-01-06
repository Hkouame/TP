Role Name
=========

Install and configure corosync/pacemaker cluster by defining resource for VIP, Servicex and DRBD

Requirements
------------

If using DRBD, resource must be already configure and a Primary node must be already set

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `pcmk_cluster_name` | pacemaker | Cluster name |
| `pcmk_hacluster_passwd` | changeme | Password for user hacluster |
| `pcmk_hosts` | **mandatory** | Cluster list of server |
| `pcmk_drbd_rsc` |  | DRBD resources declaration |
| `pcmk_vip_rsc` |  | VIP resources declaration |
| `pcmk_svc_rsc` |  | Service resources declaration |

Dependencies
------------

None.

Example Playbook
----------------

Simple example using VIP resource:

```YAML
---
- hosts: all
  roles:
    - role: pacemaker
      pcmk_hosts: "{{ groups['centos7-ha'] }}"                                                                         
      pcmk_hacluster_passwd: 'sigipsr'                                                     
      pcmk_vip_rsc:
        - interface: enp0s3
          address: 192.168.56.45
          netmask: 24
```

Simple example using Service resource:

```YAML
---
- hosts: all
  roles:
    - role: pacemaker
      pcmk_hosts: "{{ groups['centos7-ha'] }}"
      pcmk_svc_rsc:
        - mariadb
```

Simple example using DRBD resources:

```YAML
---
- hosts: all
  roles:
    - role: pacemaker
      pcmk_hosts: "{{ groups['centos7-ha'] }}"
      pcmk_drbd_rsc:
        rsc_name: data
        mnt_point: /srv
```

Complexe example for MySQL cluster. Use DRBD resource 'data', mount DRBD device on '/srv' directory, migrate '/var/lib/mysql' to '/srv/mysql', add VIP on cluster, and manage 'mariadb' services :

```YAML
---
- hosts: all
  roles:
    - role: pacemaker
      pcmk_hosts: "{{ groups['centos7-ha'] }}"
      pcmk_drbd_rsc:
        rsc_name: data
        mnt_point: /srv
        dir:
          - src_dir: /var/lib/mysql
            dst_dir: /srv/mysql
      pcmk_vip_rsc: 
        - interface: enp0s3
          address: 192.168.56.45
          netmask: 24
      pcmk_svc_rsc:
        - mariadb
```

Complexe example using multiple resources :

```YAML
---
- hosts: all
  roles:
    - role: pacemaker
      pcmk_hosts: "{{ groups['centos7-ha'] }}"
      pcmk_drbd_rsc:
        rsc_name: data
        mnt_point: /srv
        dir:
          - src_dir: /var/lib/mysql
            dst_dir: /srv/mysql
          - src_dir: /var/www
            dst_dir: /srv/www
      pcmk_vip_rsc: 
        - interface: enp0s3
          address: 192.168.56.45
          netmask: 24
        - interface: enp0s3
          address: 192.168.56.48
          netmask: 24
      pcmk_svc_rsc:
        - mariadb
        - httpd
```
