Role Name
=========

Install and configuration DRBD replication between 2 hosts.

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `drbd_device` | /dev/drbd0 | Bloc device to use for access DRBD data |
| `drbd_disk` | /dev/data/srv | Disk or partition used by DRBD for replication (**/!\ All data of this device will be erased**) |
| `drbd_port` | 7788 | Replication port |
| `drbd_netif` | eth0 | Network interface used for replication |
| `drbd_hosts` | **Mandatory** | 2 hosts cluster list  |
| `drbd_primary_host` | drbd_hosts[0] | 2 hosts cluster list  |
| `drbd_res_name` | data | Resource name to configuration |
| `drbd_res_sync_proto` | C | Replication protocol to use (A, B or C) |
| `drbd_res_sync_rate` | 50M | Replication bloc speed between hosts |


Dependencies
------------

None.

Example Playbook
----------------

Simple example :

```YAML
---
- hosts: all
  - role: drbd
    drbd_hosts: ['srv1','srv2']
    drbd_disk: /dev/sdb
    drbd_netif: enp0s3
