Logstash
=========

This role install a Logstash server.

Requirements
------------

No requirements

Role Variables
--------------

Default variables are defined in defaults/ and vars/ directory.

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `ls_worker` | num proc | Number of worker use to handle messages in filter and output |
| `ls_batch_size` | 10000 | Bulk of messages handle|
| `ls_heap_size_prct` | (90% RAM) | Memory reserved for Logstash JVM in percent |
| `ls_heap_size` | (90% RAM) | Memory reserved for Logstash JVM |
| `ls_nice` | 19 | CPU nice for logstash process |
| `ls_path_conf` | /etc/logstash | Default configuration directory |
| `ls_path_data` | /var/lib/logstash | Default data directory |
| `ls_path_logs` | /var/log/logstash | Default log directory |
| `ls_input_kafka` | false | Add kafka input section |
| `ls_output_kafka` | false | Add kafka output section |
| `ls_kafka_topic` | logstash | default kafka topic |
| `ls_kafka_hosts` | ['localhost']  | Kafka cluster hosts list to join |
| `ls_kafka_port` | 9092 | Port used to join Kafka cluster |
| `ls_kafka_zk_port` | 2181 | ZppKeeper port to join cluster |
| `ls_output_elasticsearch` | false | Add elasticsearch output section |
| `ls_elasticsearch_hosts` | ['localhost'] | Elasticsearch cluster hosts list to join |
| `firewall_setup` | True | Launch firewall task |
| `firewall_type` | "firewalld" | Open ports with firewalld |

Dependencies
------------

No dependencies

Examples Playbook
----------------

Simple example :

```YAML
---
- hosts: servers
  roles:
    - logstash
```

Complexe example :

```YAML
---
- hosts: logstash-shipper
  roles:
    - role: logstash
      ls_output_kafka: true
      ls_kafka_hosts: "{{ groups['kafka'] }}"
    
- hosts: logstash-indexer
  vars:
    es_heap_size_prct: 0.3
    es_plugins: []
  roles:
    - role: logstash
      ls_input_kafka: true
      ls_kafka_hosts: "{{ groups['kafka'] }}"
      ls_output_elasticsearch: true
      ls_elasticsearch_hosts: ['127.0.0.1']
      ls_nice: 19
      ls_heap_size_prct: 0.65
```

Note: Logstash run on server with elasticsearch client. So HEAP size must be reduce for all of them in order to avoid lack of memory.

