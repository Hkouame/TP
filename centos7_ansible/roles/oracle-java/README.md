Oracle-JAVA
=========

This role install and configure java jdk environment

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed in the metadata file.


Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

```
oracle_java_version: 8 # You can define the jav oracle version
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: servers
  roles:
   - role: oracle-java
     oracle_java_version: 8
```

License
-------

BSD

Author Information
------------------

* Jean-Vincent KASSI (jekas@smile.ci)
