Role Name
=========

This role allows you to configure a [Solr](http://lucene.apache.org/solr/) service on your system.

It mainly wraps the [ansible-genericservice](https://git.smile.fr/ansible/ansible-genericservice) role to ease its use.

Role Variables
--------------

The main variable of this role is `solr`.

Those variables are herited from `genericservice` :

Variable | Default value |Description
---------|---------------|--------------
`subpath` | Mandatory | Contains the name of the top-level directory inside the tar/zip, or the relative path in which the application is already extracted
`source_file` | None | If this parameter is given, a tar/zip file at this path will be copied and extracted to the server
`source_url` | None | If this parameter is given, a tar/zip file at this path will be downloaded and extracted to the server
`source_sha256` | None | This parameter is mandatory if `source_url` has been given. It contains the SHA-256 sum of the downloaded file
`config_directories`| None | This parameter contains configuration directories that should be copied into the Solr instance

Those variables are specific to this role :

Variable | Default value |Description
---------|---------------|--------------
`needed_libraries` | None | If this parameter is given, the list of libraries URL it contains will be downloaded and add to Solr libraries |


Additional variables you can define for this role, outside the `solr` one, are :

Variable | Default value |Description
---------|---------------|--------------
`solr_service_name` | solr | The name you want to give the application. By default it will be used to name the system service and the systems users

Requirements
------------

As stated earlier, this role heavily uses the [ansible-genericservice](https://git.smile.fr/ansible/ansible-genericservice) role.

```yml
- src: git@git.smile.fr:ansible/ansible-genericservice.git
  scm: git
- src: git@git.smile.fr:ansible/ansible-solr.git
  scm: git
```

Example Playbook
----------------

Here is how to quickly bootstrap a new Solr instance:

    - hosts: servers
      vars:
        solr:
          source_url: http://archive.apache.org/dist/lucene/solr/5.2.1/solr-5.2.1.tgz
          source_sha256sum: 3f54cec862da1376857f96f4a6f2044a5addcebc4df159b8797fd71f7ba8df86
          subpath: solr-5.2.1
          needed_libraries:
            - http://search.maven.org/remotecontent?filepath=mysql/mysql-connector-java/5.1.26/mysql-connector-java-5.1.26.jar
      roles:
        - role: ansible-solr

Note
----

For SolR 4.X, the example folder is copied in the server folder in which the solr service will be executed.

License
-------

BSD
