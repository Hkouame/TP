ElasticSearch
=========

This role install a Elasticsearch server

Requirements
------------

No requirements

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `es_version` | 2.2 | ES version to install |
| `es_cluster_name` | default | ES cluster name |
| `es_network_host` | 0.0.0.0 | Interface list ES bind |
| `es_master_node` | true | Allow this node to become master node |
| `es_data_node` | true | Allow this node to store data |
| `es_path_data` | /var/lib/elasticsearch | Default data directory |
| `es_path_logs` | /var/log/elasticsearch | Default log directory |
| `es_path_repo` | /var/repo/elasticsearch | Default repository directory for backup |
| `es_shard_count` | 6 | Number of shard per index |
| `es_replica_count` | 1 | Number of replica per index |
| `es_script_inline` | false | Enable/Disable execution of inline script |
| `es_script_indexed` | false | Allow/Disallow to store scripts in internal index |
| `es_script_engine_groovy_inline_aggs` | off | Enable/Disable dynamic scripting |
| `es_install_curator` | false | Boolean for installing curator package |
| `es_install_admin_scripts` | false | Boolean for installing backups scripts |
| `es_max_openfiles` | 65536 | Limit for the number of open files on the OS (ulimit -n) |
| `es_heap_size` | (50% RAM) | Memory reserved for Elasticsearch JVM |
| `es_hosts` | localhost:9200 | Cluster host list |
| `es_plugins` | mobz/elasticsearch-head | Plugins list to install |
| `es_index_refresh_interval` | 30s | Interval before refresh for new document to be available in search |
| `vm_max_map_count` | 262144 | Operating system limits on mmap counts |
| `firewall_setup` | True | Define if rôle open elasticsearch port, firewall_type must be defined is True |
| `firewall_type` | firewalld | Define which firewall is configured |
| `es_install_prompt_scripts` | true | Customize prompt |

Dependencies
------------

No dependencies

Example Playbook
----------------

Very simple example for one ElasticSearch node :

```YAML
---
- hosts: servers
  roles:
    - role: elasticsearch
```

Simple example for 3 nodes ElasticSearch cluster :

```YAML
---
- hosts: servers
  roles:
    - role: elasticsearch
      es_cluster_name: clustername
      es_hosts: [ '192.168.122.213', '192.168.122.214', '192.168.122.215' ]
```

Complexe example with N client node, M master node and X data node :

```YAML
---
- hosts: elasticsearch-all
  roles:
    - role: elasticsearch
      es_cluster_name: elasticsearch
      es_hosts: "{{ groups['elasticsearch-master'] }}"
      es_path_data: '/srv/elasticsearch/data'
      es_path_logs: '/srv/elasticsearch/logs'
      es_path_repo: '/srv/elasticsearch/repo'

- hosts: elasticsearch-client
  roles:
    - role: elasticsearch
      es_master_node: "false"
      es_data_node: "false"

- hosts: elasticsearch-master
  roles:
    - role: elasticsearch
      es_data_node: "false"
      es_install_curator: true
      es_install_admin_scripts: true

- hosts: elasticsearch-data
  roles:
    - role: elasticsearch
      es_master_node: "false"
      es_shard_count: 3
```
