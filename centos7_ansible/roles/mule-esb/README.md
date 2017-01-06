Mule ESB
=========

This module download and configure service for mule esb standalone

Requirements
------------


This role requires Ansible 1.4 or higher, and platform requirements are listed in the metadata file.
You need also to have a jdk environment


Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

```
http_proxy:  http://repo.sva-orange.ci:3128  # Define a http proxy
https_proxy:  http://repo.sva-orange.ci:3128 # Define a https proxy
mule_esb_path_data: /srv                     # Mule esb data path 
mule_esb_path_logs: /var/log/mule-standalone # Mule esb logs path
mule_esb_version: 3.8  # Mule esb version

```



Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: all
  vars: You can define proxies
      http_proxy: http://repo.sva-orange.ci:3128 
      https_proxy: http://repo.sva-orange.ci:3128
  roles:
    - role: mule-esb
```

License
-------

BSD

Author Information
------------------

* Jean-Vincent KASSI (jekas@smile.ci)

