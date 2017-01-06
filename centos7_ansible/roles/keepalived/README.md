# KeepAlived

This role install a KeepAlived cluster on RedHat/CentOS Linux servers and configure SELinux and firewall.

## Requirements

None.

## Role Variables

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `keepalived_deploy_adminscript` | true | Deploy clutser-watch admin script and custom prompt |
| `keepalived_vrrp_instance` | none | Configure one or more VRRP instances |

VRRP Instance dictionnary variables (**keepalived_vrrp_instance**) :
 
| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| **key** | none | Name of instance |
| `interface` | none | Network interface used by VRRP instance  |
| `vrid` | none | **Unique** VRRP Identifier |
| `pass` | none | Secret shared between all hosts of this VRRP instance |
| `vip` | none | Virtual IP address list attach on this interface |


## Dependencies

None.

## Example Playbook

This playbook create a cluster VRRP instance on interface **eth1** with 2 VIP (**192.168.122.6** and **192.168.122.7**)

```YAML
---
- hosts: all
  roles:
    - role: keepalived
      keepalived_vrrp_instance:
        VERDURE:
          interface: eth1
          vrid: 10
          pass: S3cureP@ssw0rd
          vip:
            - 192.168.122.6
            - 192.168.122.7
```
