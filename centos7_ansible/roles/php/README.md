# Description and basic usage

This role allows to install and configure PHP.

You can basically use it by appending the role to your ansible project :

```yml
- hosts : fronts
  roles:
    - { role: ansible-php }
```

# Documentation

## Available variables


The role provides the following variables :

Variable | Default value |Description
---------|---------------|------------
`php_packages` | *Depends on distribution* | What PHP packages will be installed
`php_extension_packages`| | The PHP extensions installed packages. You should override in your playbook vars to enable some additional extensions
`php_extras_packages`| | This variable is present to allows installing extension only on some environment basis by overriding it into the inventory vars. By example, you should use it to enable xhprof and xdebug only in the dev environment.
`php_settings_all`| | PHP configuration variables to set for both CLI and Apache2
`php_settings_cli`| | PHP configuration variables to set only for CLI (Debian Only)
`php_settings_apache2`| | PHP configuration variables to set only for Apache2 (Debian Only)


## Available tags

This role has no special tags management. Classical tags have been added to the role and allows the role to be compatible with playbooks that are using them :

* **install**
* **update_config**
* **update_app**

## Available handlers

This role does not provides any handler.
