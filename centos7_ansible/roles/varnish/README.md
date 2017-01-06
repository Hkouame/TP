Varnish
=======

This role install a Varnish server

Role Variables
--------------

* `varnish_defaults_template` : local path of the template for the defaults file
* `varnish_vcl_template`: local path of the VCL template
* `varnish_vcl_name`: name of the VCL file the template will be expanded to
* `varnish_port`: Port Varnish will listen on
* `varnish_backend_host`: IP address of the backend
* `varnish_backend_port`: port of the backend
* `varnish_memory_mb`: Megabytes of memory to be used by Varnish
* `varnish_forwarded_ip_in_logs`: Whether or not include the forwarded ip in logs [false]
* `varnish_additional_opts`: Additional options you want to add on the startup command line, for example "-p connect_timeout=20" []
* `varnish_version` : Automatically set by ansible, you can use it in templates if you want to take multiple versions of Varnish into account
* `varnish_use_repo` : Install varnish from official Varnish repository instead of distro repository. Possible values : 3.0, 4.0, 4.1


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-varnish, varnish_port:80, varnish_backend_port: 81 }

License
-------

BSD

