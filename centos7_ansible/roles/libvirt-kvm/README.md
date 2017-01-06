Role Name
=========

Install KVM + Libvirt and permit de create iface and pool object.

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `libvirt_network` |  | Create libvirt network interface and bridge on VLAN ID |
| `libvirt_network.client` |  | Client identity |
| `libvirt_network.vlanid` |  | VLAN ID |
| `libvirt_network.netif`  |  | Physical network interface on host attach to bridge |
| `libvirt_network.netif`  |  | Physical network interface on host attach to bridge |
| `libvirt_network.ipaddr`  |  | Host IP address to set on bridge |
| `libvirt_network.prefix`  |  | Host IP prefix to set en bridge |
| `libvirt_pools` |  | Create Pool |
| `libvirt_pools.name` |  | Pool name |
| `libvirt_pools.path` |  | Pool directory on host |


Dependencies
------------

None.

Example Playbook
----------------

Simple example :

```YAML
---
- hosts: all
  roles:
    - role: libvirt-kvm
```

Network playbook example :

```YAML
---
- hosts: all
  roles:
    - role: libvirt-kvm
      libvirt_networks:
        - client: smile
          vlanid: 201
          netif:  eth1
          ipaddr: 10.2.1.22
          prefix: 24
        - client: sfl
          vlanid: 202
          netif:  eth1
        - client: scs
          vlanid: 203
          netif:  eth1
```

Pool playbook example :

```YAML
---
- hosts: all
  roles:
    - role: libvirt-kvm
      libvirt_pools:
        - name: hdd
          path: /var/lib/libvirt/pool/hdd
        - name: ssd
          path: /var/lib/libvirt/pool/ssd
```

