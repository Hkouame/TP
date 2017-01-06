# Description and basic usage

This role allows to install and configure mongodb.

You can basically use it by appending the role to your ansible project :

```yml
- hosts : fronts
  roles:
    - { role: ansible-mongodb }
```

# Documentation

## Available variables

Variable | Default value |Description
---------|---------------|--------------
`mongodb_config_template` | None | If this parameter is given, the template will be used as MongoDB configuration

## Available tags

This role has no special tags management. Classical tags have been added to the role and allows the role to be compatible with playbooks that are using them :

* **install**
* **update_config**
* **update_app**

## Available handlers

This role does not provides any handler.

## Requirements

No specific requirements
