# Description and basic usage

This role allows to install the Nginx web server and to configure vhosts attached to the server.

Additionally, the role proceeds to some basic useful operations during it's execution :

- disabling the default vhosts shipped with Debian
- append rows with the localhost address for every vhosts server name and aliases :
```127.0.0.1 www.myservice.com alias1.myservice.com alias2.myservice.com```

You can basically use it by appending the role to your ansible project :

```yml
- hosts : fronts
  roles:
    - { role: ansible-nginx }
```

# Documentation

## Available variables

### Global configuration

Variable | Default value |Description
---------|---------------|--------------
nginx_packages | apache2 <br/> libapache2-modsecurity| List of packages installed by the role
nginx_extra_packages |  | This variable is intended to allow you to append additional packages to be installed from your playbooks without rewriting the whole apache2_packages variable
nginx_disabled_default | default <br /> | List of default website to be disabled
nginx_port| 80 | Default HTTP port |
nginx_ssl_port| 443 | |Default HTTPs port
nginx_use_ssl | False | |Default HTTPs port

### Managing vhosts

You can manage vhost by using the *nginx_vhosts* variable :

```yml
nginx_vhosts:
  my_app_vhost:
    document_root: /var/www/my_app
    server_name: www.myservice.com
    server_aliases:
      - alias1.myservice.com
      - alias1.myservice.com
  my_other_app_vhost:
    vhost_name: name_of_the_vhost
    template: templates/nginx/magento_vhost.conf.j2
    document_root: /var/www/my_other_app
    create_document_root: false
    server_name: www.anotherdomain.com
    ssl:
        enabled: True
        certificate_key_file: "/etc/ssl/private/ssl-cert-snakeoil.key"
        certificate_file: "/etc/ssl/certs/ssl-cert-snakeoil.pem"
    php:
        enabled: True
        socket: "unix:/var/run/php5-fpm.sock"
```

The following variables are mandatory either set to a default value for each vhosts :

Variable | Default value |Description
---------|---------------|--------------
document_root | | The document root of the vhosts
create_document_root | true | Create the document root automatically if not exists. Set it to false if you plan to use a release process based on symlinks by example.
server_name | | This is a required value allowing to set the ServerName directive
server_aliases | | An optional list of additional domain we can build a list of ServerAlias directives with
vhost_name | The same value as the key of the vhost into nginx_vhosts dictionary| Allow to keep control on the name of the file containing the vhost. By example you can inject the environment name into the filename. So the resulting file will be called **my_app_vhost_dev.conf** instead of **my_app_vhost.conf**.
template|default_vhost.j2|The template used to build the vhost. <br/>**Warning :** If the template is into your playbook you need to prefix it with **templates/** (eg templates/myapp_vhost.conf.j2). It is not the case if you are using template bundled into the role.

Every other variables set here are accessible into the templates through **{{item.value.my_custom_var}}**. You can see an example into the **default_vhost.j2** shipped with the role.

## Available tags

* **install** :  Run everything. Only present since some playbook uses it.
* **update_config** :  Run everything except the vhosts installation / configuration.
* **update_app** : Run every tasks related to vhosts. Additionally new packages and modules are installed and configured since they may be required by the vhosts

## Available handlers

This role provides two handlers which restart or reload Nginx. You can use it in your own task through :

```yml
- hosts : fronts
  tasks:
    - name: "Useless task that will restart Nginx on changed"
      debug: msg="My super dumb task"
      notify: "Reload Nginx"
  roles:
    - { role: ansible-nginx }
```
