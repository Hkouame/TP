Role Name
=========

Install Vagrant

Requirements
------------

None.

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `vagrant_version` | 1.8.7  | Vagrant version to install  |
| `vagrant_home` | ~/.vagrant.d | Vagrant home directory |
| `vagrant_deploy_scripts` | false | Deploy vagrant admin scripts (vagrant-ddns, vagrant-setmax*) |
| `vagrant_plugins` |  | Vagrant plugin list to install |


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
    - role: vagrant
```


Complexe example :

```YAML
---
- hosts: all
  roles:
    - role: vagrant
      vagrant_home: /srv/vagrant/.vagrant
      vagrant_deploy_scripts: true
      vagrant_plugins:
        - vagrant-libvirt
        - vagrant-triggers
```
