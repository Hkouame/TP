Role Name
=========

This role allows you to configure a [Tomcat](http://tomcat.apache.org/) service on your system.
It also allow you to deploy a webapp and its configuration.

Role Variables
--------------

To bootstrap a new Tomcat instance, the main variable of this role is `tomcat7`.

Variable | Default value |Description
---------|---------------|--------------
`tomcat_use_mysql` | None | Set to true if you want to install the MySQL JDBC driver
`tomcat_conf_files` | None | List of templates to be put in tomcat configuration dir
`tomcat_env_vars` | None | Tomcat service configuration dictionary
`tomcat_service_name` | tomcat7 | Tomcat service configuration file name

To deploy a new webapp, the main variable of this role is `java_app`.

Variable | Default value |Description
---------|---------------|--------------
`name` | Mandatory | Name of the context
`conf_files` | None | Settings files list
`log_file` | Mandatory | Path to the application log file
`logrotate_conf` | None |
`tomcat_user` | Mandatory | System user in charge of Tomcat process
`context` | None | Path to the application context file
`war` | Mandatory | Path to the application war file

Example Playbook
----------------

Here is how to bootstrap a new Tomcat instance:

    - hosts: servers
      vars:
        tomcat_use_mysql: true
        tomcat_env_vars:
          JAVA_OPTS: '"-Djava.awt.headless=true -Xmx512m -XX:MaxPermSize=128m"'
      roles:
        - role: ansible-tomcat

Here is how to deploy a new webapp:

    - hosts: servers
      vars:
        java_app:
          name: my-super-app
          conf_files:
            - conf/app/conf-file-1-ext.properties
            - conf/app/conf-file-2-ext.properties
          log_file: /var/log/my-super-app/my-super-app.log
          logrotate_conf: conf/my-super-app.logrotate
          tomcat_user: tomcat7
          context: conf/context.xml.j2
          war: PATH/TO/WAR/FILE
      roles:
        - role: ansible-tomcat

License
-------

BSD
