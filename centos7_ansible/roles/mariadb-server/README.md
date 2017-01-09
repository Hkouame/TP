# Description and basic usage

This role allows to install and configure the MySQL on your server

This role is used by appending it to your ansible playbook :

```yml
- hosts : fronts
  roles:
    - { role: mariadb-server }
```

Additionally this role can init databases and user associated to them and manage data into these databases.

# Documentation

## Available variables

Configuration variables have been splitted in two categories :

* **Dangerous settings :** Variables that can only be set while installing the server for the first time. Changing them is considered as dangerous since it requires to drop all the databases and reimporting them from a previous dump.

* **Dynamic settings :** Variables that can be changed with a simple MySQL server restart.

These settings have default values that should be tuned specifically project by project and environment by environment. It should mainly be considered as an inventory variables that are important to care about and an easier way to update it.

### Install time settings (a.k.a dangerous settings)

| Variable | Default value | MySQL variable |
| ---------|---------------|-------------- |
| `mysql_config_innodb_file_per_table` | 1 | innodb_file_per_table |
| `mysql_config_innodb_log_file_size:` | 32M | innodb_log_file_size |
| `mysql_config_innodb_log_buffer_size` | 4M | innodb_log_buffer_size |
| `mysql_config_innodb_data_file_path` | "ibdata1:256M:autoextend" | innodb_data_file_path |
| `mysql_config_innodb_autoextend_increment` | 64 | innodb_autoextend_increment |

All the variables are set into the `/etc/mysql/conf.d/01-dangerous-settings.cnf` file.

### Other settings (a.k.a dynamic settings)

| Variable | Default value | MySQL variable |
| ---------|---------------|---------------- |
| `mysql_config_bind_address` | 0.0.0.0 | bind-address |
| `mysql_config_bind_port` | 3306 | port |
| `mysql_config_skip_name_resolve` | 1 | skip-name-resolve |
| `mysql_config_key_buffer` | 64M | key_buffer |
| `mysql_config_max_allowed_packet` | 16M | max_allowed_packet |
| `mysql_config_thread_stack` | 192K | thread_stack |
| `mysql_config_thread_cache_size` | 0 | thread_cache_size |
| `mysql_config_query_cache_type` | 1 | query_cache_type |
| `mysql_config_query_cache_limit` | 1M | query_cache_limit |
| `mysql_config_query_cache_size` | 32MB | query_cache_size |
| `mysql_config_innodb_buffer_pool_size_prct` | 0.8 | innodb_buffer_pool_size percent of server memory |
| `mysql_config_innodb_buffer_pool_size` | 2G | innodb_buffer_pool_size |
| `mysql_config_innodb_additional_mem_pool_size` | 4M | innodb_additional_mem_pool_size |
| `mysql_config_innodb_flush_log_at_trx_commit` | 1 | innodb_flush_log_at_trx_commit |
| `mysql_config_slow_query_log` | 1 | slow_query_log |
| `mysql_slow_query_log_file` | /var/log/mysql/mysql-slow.log  | slow_query_log_file |
| `mysql_config_slow_long_query_time` | 2 | slow_long_query_time |
| `mysql_config_log_bin` | /var/log/mysql/mysql-bin.log | log_bin |
| `mysql_config_binlog_format` | ROW | binlog_format |
| `mysql_config_expire_logs_days` | 8 | expire_logs_days |
| `manage_by_cluster` | False | Variable set to true if service state must be managed by a cluster solution (like PCS)  |



In the end there is a little set of variables that are related to the role itself :

| Variable` | Default value | Description |
| ---------|---------------|---------------- |
| `mysql_flavor` | mysql | The brand of MySQL server to install. Supported values : `mysql`, `percona` |
| `mysql_packages` | mysql-server,  python-mysqldb | List of the packages installed by the role. Can be used to changed the MySQL flavour installed (MariaDB, Percona, ...) if you have set up additional repositories. |
| `mysql_root_password` | changeme  | The root password of the database. **It should be set environment by environment.** A passwordless login to the dabatase is installed by the role for the root user of the server using this (into the `/root/.my.cnf` file). |
| `mysql_use_binlog` | False  | Set this variable if you intend to use binary logging. By default, binary logging will be disabled even if you set `mysql_config_log_bin` explicitely |

### Database management

This role allow you to create database and users allowed to connect to them.

#### Creating databases and users

Creating databases and an user allowed to connect to it can be done by filling the mysql_databases dictionary into your inventory or into var files of your playbook :

```yml
mysql_databases:
  first_database:
    db_name : magento
    collation: utf8_unicode_ci
    encoding: utf8
    user: magento
    password: changethepassword
  another_db:
    db_name : drupal
    collation: utf8_unicode_ci
    encoding: utf8
    user: drupal
    password: changethepassword
```

Available settings are those listed above. Note that encoding and collation are optional and their respective default values are `utf8` and `utf8_unicode_ci`.

You can note that the key foreach database is different from the database name. It is very important since you can then obtain the database name into your playbook by using :

```{{hostvars.dbserver.mysql_databases.first_database.db_name}}}```

It allows you to have different name by environment without changing playbook using the databases.

**Note :**
The host part of the user is not fine grained. You should think it just like an equivalent of running a GRANT command in MySQL with `'user'@'%'`.
While this is not fixed you have to consider additional security policies like firewalling (in fact you should even with it will be fixed !!!).

#### Init and update database with data

When bootstrapping a new environment you may will to have a database dump deployed automatically on it. This role allow you to get this achieved it by downloading a dump from a remote ssh server and getting it imported into the newly created database. Using this feature require you to declare a `sync_source` entry into the database setting :

```yml
mysql_databases:
  first_database:
    db_name : magento
    collation: utf8_unicode_ci
    encoding: utf8
    user: magento
    password: changethepassword
    sync_source:
      host: prod.myproject.smile.fr    # Host the dump is located on
      user: remote_user                # User used on the remote server
      path: /home/remote_user/db_name  # Path where to find the dump on the remote host
      file: magento_current.sql        # Dump file name on the remote host
```

The `sync_source` can also be the ansible client itself :

```yml
    sync_source:
      src: ../data/magento_current.sql # Source file on the Ansible machine
      file: magento_current.sql        # Destination filename on the remote server
```

Or an arbitrary URL (download will be done from the server)

```yml
    sync_source:
      url: http://myserver.eqx/dumps/magento_current.tgz # Source file on the Ansible machine
      file: magento_current.sql        # Destination filename on the remote server
```

The dump are downloaded into the `/data/dump/db_name` directory.

On the other side, environment data need to be periodically updated. One part of this data are located into MySQL databases. By default the dump is fetched from remotes and imported only for newly created databases. You can force it to be imported by adding an additional variable `allow_update_data` in your playbook execution command :

```
ansible-playbook myplaybook.yml --extras_vars "allow_update_data=1"
```

As a result the target database is dropped and a new one is created containing all the data. For some reason (e.g. avoiding an human error erasing all production data) you may want to forbid this to be executed on some environment. You can do this by appending the `forbid_update_data` into the hostvars of this environment (e.g. in `inventory/prod/group_vars/all`):

```
forbid_update_data: 1
```

The variable `forbid_update_data` has always precedence on `allow_update_data`. The only way to override it is to pass both variables to your playbook execution :

```
ansible-playbook myplaybook.yml --extras_vars "allow_update_data=1 forbid_update_data=0"
```

**Notes :**

 - Using this feature require you to be  allowed to access the sync server in SSH. Your private key have to be present on the sync server.

 - This feature will be completed by an additional layer providing a pluggable  mechanism of anonymization of the data very soon.

## Available tags

* **install** : Run everything. Only present since some playbook uses it.
* **update_config** : Update every configuration that are not marked as dangerous. Database users are also modified using this tag.
* **update_data** :  Only play the databases creation part of the role. Use this with 'allow_update_data=1` to refresh data.

## Available handlers

This role provides an handler which restart MySQL. You can use it in your own task through :

```yml
- hosts : db-servers
  tasks:
    - name: "Useless task that will restart MySQL on changed"
      debug: msg="My super dumb task"
      notify: "Restart MySQL"
  roles:
    - { role: mariadb-server }
```
