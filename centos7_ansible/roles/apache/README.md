# Description and basic usage

This role allows to install the Apache web server and to configure vhosts attached to the server.

Additionally, the role proceeds to some basic useful operations during it's execution :

- disabling the default vhosts shipped with Debian
- set some security settings into /etc/apache2/conf.d/security
- append rows with the localhost address for every vhosts server name and aliases :
```127.0.0.1 www.myservice.com alias1.myservice.com alias2.myservice.com```

You can basically use it by appending the role to your ansible project :

```yml
- hosts : fronts
  roles:
    - apache
```

# Documentation

## Available variables

### Global configuration

Variable | Default value |Description
---------|---------------|--------------
apache2_packages | apache2 | List of packages installed by the role
apache2_extra_packages |  | This variable is intended to allow you to append additional packages to be installed from your playbooks without rewriting the whole apache2_packages variable
apache2_modules  | headers<br/> deflate <br/> rewrite <br/> ssl<br/> expires | List of apache module enabled by the role.
apache2_extra_modules | | This variable is intended to allow you to append additional modules to be enabled from your playbooks without rewriting the whole apache2_modules variable.
apache2_disabled_default | default.conf <br /> default_ssl.conf| List of default website to be disabled
apache2_user | www-data | User of the Apache service
apache2_group| www-data | Group of the Apache service
apache2_port| 80 | Default HTTP port |
apache2_ssl_port| 443 | |Default HTTPs port
apache2_version | *automatic* | This variable is set by ansible automatically. May be useful in vhost template to manage inconsistencies between Apache version and help to keep your playbook generic.

### Managing vhosts

You can manage vhost by using the *apache2_vhosts* variable :

```yml
apache2_vhosts:
  my_app_vhost:
    document_root: /var/www/my_app
    server_name: www.myservice.com
    server_aliases:
      - alias1.myservice.com
      - alias1.myservice.com
  my_other_app_vhost:
    vhost_name: name_of_the_vhost
    template: templates/apache/magento_vhost.conf.j2
    document_root: /var/www/my_other_app
    create_document_root: false
    server_name: www.anotherdomain.com
```

The following variables are mandatory (except for environment_vars) either set to a default value for each vhosts :

Variable | Default value |Description
---------|---------------|--------------
document_root | | The document root of the vhosts
create_document_root | true | Create the document root automatically if not exists. Set it to false if you plan to use a release process based on symlinks by example.
server_name | | This sets the ServerName directive, by default, its value is the FQDN of the server
server_aliases | | An optional list of additional domain we can build a list of ServerAlias directives with
environment_vars | | An optional dictionary containing environment variables names as keys, and their values
vhost_name | The same value as the key of the vhost into apache2_vhosts dictionary| Allow to keep control on the name of the file containing the vhost. By example you can inject the environment name into the filename. So the resulting file will be called **my_app_vhost_dev.conf** instead of **my_app_vhost.conf**.
template|default_vhost.j2|The template used to build the vhost. <br/>**Warning :** If the template is into your playbook you need to prefix it with **templates/** (eg templates/myapp_vhost.conf.j2). It is not the case if you are using template bundled into the role.

Every other variables set here are accessible into the templates through **{{item.value.my_custom_var}}**. You can see an example into the **default_vhost.j2** shipped with the role.

## Using PHP

If you intend on using PHP, the [php role](https://git.smile.fr/ansible/ansible-php) should take care of the necessary configuration, however, if you need to put PHP-specific configuration in your VHost files, you might need to add PHP to the `apache2_modules` list:

```yml
apache2_modules:
  - headers
  - deflate
  - rewrite
  - ssl
  - expires
  - php5
```

## Available tags

* **install** :  Run everything. Only present since some playbook uses it.
* **update_config** :  Run everything except the vhosts installation / configuration.
* **update_app** : Run every tasks related to vhosts. Additionally new packages and modules are installed and configured since they may be required by the vhosts

## Available handlers

This role provides an handler which restart Apache. You can use it in your own task through :

```yml
- hosts : fronts
  tasks:
    - name: "Useless task that will restart Apache on changed"
      debug: msg="My super dumb task"
      notify: "Restart Apache"
  roles:
    - { role: ansible-apache }
```