Role Name
=========

This role install a Kafka cluster with ZooKeeper

Requirements
------------

No requirements

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory.

ZooKeeper variables :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `zk_client_port` | 2181 | Default ZK port |
| `zk_follower_port` | 2888 | Port use for zookeeper cluster communication |
| `zk_election_port` | 3888 | Port use for zookeeper cluster communication |
| `zk_max_client_connexions` | 0 |  |
| `zk_autopurge_snapRetainCount` | 3 | Retention snapshot and log count |
| `zk_autopurge_purgeInterval` | 24 | Purge task interval execution |
| `zk_data_dir` | /var/lib/zookeeper | Data directory of Zookeeper |
| `zk_tickTime` | 3000 | Number of milliseconds of each tick |
| `zk_initLimit` | 10 | Number of ticks that the initial synchronization phase can take |
| `zk_syncLimit` | 5 | Number of ticks that can pass between sending a request and getting an acknowledgement<Paste> |
| `zk_hosts` | localhost | Zookeeper cluster node |

Kafka variables :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `kafka_scala_version` | 2.11.7 | Scala version |
| `kafka_broker_id` | 0 | ID of broker in cluster group |
| `kafka_port` | 9092 | Default port use by kafka |
| `kafka_data_dir` | /var/lib/kafka | Kafka data directory |
| `kafka_log_retention_hour` | 48 | Data retention in hour before deletion |
| `kafka_log_retention_bytes` | 1073741824 | Data retention in byte before deletion |
| `kafka_log_segment_bytes` | 1073741824 | Data segment in byte before rotation |
| `kafka_num_partitions` | 1 | Sharding of data |
| `kafka_default_replication_factor` | 1 | Replication factor |
| `kafka_num_network_threads` | 8 |  |
| `kafka_num_io_threads` | 8 |  |
| `kafka_socket_send_buffer_bytes` | 1048576 | Sending buffer in bytes |
| `kafka_socket_receive_buffer_bytes` | 1048576 | Receiving buffer in bytes |
| `kafka_socket_request_max_bytes` | 104857600 |  |
| `kafka_topics` | | var who can create one or more kafka topics|
| `firewall_setup` | True | Launch firewall task |
| `firewall_type` | "firewalld" | Open ports with firewalld |

**Important**: In kafka cluster broker id (`kafka_broker_id`) must be different on each node ! Set variables in `inventory/host_vars/`.

Dependencies
------------

No dependencies

Example Playbook
----------------

Simple example:

```YAML
---
- hosts: kafka
  roles:
    - kafka
```

Example for cluster with 3 nodes using zookeeper :

```YAML
---
- hosts: kafka
  roles:
    - role: kafka
      zk_hosts: "{{ groups['kafka'] }}"
      kafka_num_partitions: 3
      kafka_default_replication_factor: 2
```

Example with retention snapshot and log definition :

```YAML
---
- hosts:
  roles:
   - kafka
     kafka_log_dir: /srv/kafka/log
     zk_data_dir: /srv/zookeeper/data
     zk_hosts: "{{ groups['kafka'] }}"
     kafka_num_partitions: 64
     kafka_default_replication_factor: 3
     kafka_log_retention_bytes: 536870912
     kafka_log_segment_bytes: 536870912
```


Topic creation example:

```YAML
---
- hosts: kafka
  vars:
   kafka_topics:
    test:
      zookeeper: "localhost:2181"
      replication_factor: 1
      partition: 4
  roles:
   - kafka
```
