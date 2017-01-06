MariaDB Galera Cluster
=========

An Ansible role to install/configure mariadb galera cluster https://mariadb.org/

Requirements
------------

None

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory.

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `monitoring_server_fqdn` | % | defines the remote monitoring server |
| `monitoring_db_password` | monitoringuser | defines the password for monitoring db... define here or globally in group_vars/all/accounts |
| `monitoring_db_user` | monitoringuser | defines the user for monitoring db... define here or globally in group_vars/all/accounts |
| `deb_db_password` | {{ mariadb_root_password }} | defines debian db password... generate using `echo password \| mkpasswd -s -m sha-512` |
| `email_notifications` | notifications@{{ smtp_domain_name }} | defines email address to receive notifications...define here or in group_vars/group |
| `enable_nagios_monitoring` | {{ enable_galera_monitoring }} | defines if monitoring should be enabled for mysql |
| `enable_galera_monitoring` | false | deploy galera monitoring scripts |
| `galera_allow_root_from_any` | false | defines if root logins should be allowed from any host |
| `galera_cluster_name` | galera-cluster | Define the name of the cluster...define here or in group_vars/group |
| `galera_cluster_bind_address` | 0.0.0.0 | define bind address for galera cluster...if running in Vagrant define this as...'{{ ansible_eth1.ipv4.address }} |
| `galera_cluster_nodes_group` | galera-cluster-nodes | defines groups nodes used to form cluster |
| `galera_monitor_script_name` | galeranotify.py | |
| `galera_monitor_script_path` | /etc/mysql | |
| `mariadb_debian_repo` | deb http://ftp.osuosl.org/pub/mariadb/repo/{{mariadb_version}}/{{ansible_distribution\|lower}} {{ansible_distribution_release\|lower }} main | |
| `mariadb_debian_repo_key` | 0xcbcb082a1bb943db | |
| `mariadb_debian_repo_keyserver` | keyserver.ubuntu.com | |
| `mariadb_redhat_repo` | http://yum.mariadb.org/{{mariadb_version}}/{{ansible_distribution\|lower}}{{ansible_distribution_major_version\|int}}-amd64 | |
| `mariadb_redhat_repo_key` | https://yum.mariadb.org/RPM-GPG-KEY-MariaDB | |
| `mariadb_version` | 10.1 | MariaDB version to used |
| `mariadb_master_node` | groups[galera_cluster_nodes_group][0] | Set master node to intialize cluster. If not defined used the first host on cluster node list |
| `mariadb_root_password` | root | defines mysql root password... generate using : echo password \| mkpasswd -s -m sha-512 |
| `notify_mail_from` | galeranotify@{{ smtp_domain_name }} | defines email address that cluster notifications will be sent from |
| `notify_mail_to` | {{ email_notifications }} |
| `notify_smtp_server` | {{ smtp_server }} | defines smtp server to send notifications through |
| `pri_domain_name` | example.org |  |
| `reconfigure_galera` | false | defines if the cluster should be reconfigured | |
| `smtp_domain_name` | {{ pri_domain_name }} | defines smtp domain for email... define here or globally in group_vars/all/email | |
| `smtp_server` | smtp.{{ pri_domain_name }} | defines smtp server to send email through...define here or globally in group_vars/all/servers | |
| `wsrep_sst_user` | wsrepuser | defines xtrabackup user | |
| `wsrep_sst_password` | dO9qygn8 | defines xtrabackup password | |

Dependencies
------------

None

Example Playbook
----------------

Simple example :

```YAML
---
- hosts: all
  roles:
    - role: ansible-mariadb-galera-cluster
      galera_cluster_nodes_group: galera
```

Complexe example :

```YAML
---
- hosts: all
  roles:
    - role: ansible-mariadb-galera-cluster
      galera_cluster_name: verdure-glra
      galera_cluster_nodes_group: verdure-glra
      mariadb_master_node: verdure-glra-rw-1
      enable_nagios_monitoring: true
      enable_galera_monitoring: true
      monitoring_db_user: nagios
      monitoring_db_password: N@gI05
      mariadb_root_password: S3cureP@ssW0rd
```
