# SSL Certs

Generate and/or deploy SSL certificate

## Requirements

None.

## Role Variables

Default variables are defined in defaults/ and vars/ directory :

| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| `ssl_certs_country` | CI | Country Code |
| `ssl_certs_locality` | Abidjan | Locality |
| `ssl_certs_organization` | Smile | Compagny name |
| `ssl_certs_state` | Ivory Coast | Country Name |
| `ssl_certs_common_name` | {{ansible_fqdn}} | Certificate domain name |
| `ssl_certs_days` | 3650 | Certificate validity in days |
| `ssl_certs_fields` | "/C={{ ssl_certs_country }}/ST={{ ssl_certs_state }}/L={{ ssl_certs_locality }}/O={{ ssl_certs_organization }}/CN={{ ssl_certs_common_name }}" | Certifcate fields |
| `ssl_certs_path` | "/etc/ssl/{{ ssl_certs_common_name }}" | Path where CSR, CERT and Key will be place |
| `ssl_certs_path_owner` | root | Generated files owner |
| `ssl_certs_path_group` | root | Generated files group |
| `ssl_certs_mode` | 0700 | Generated files mode |
| `ssl_certs_privkey_path` | "{{ ssl_certs_path }}/{{ ssl_certs_common_name }}.key" | Private key file |
| `ssl_certs_cert_path` | "{{ ssl_certs_path }}/{{ ssl_certs_common_name }}.pem" | Certificate file |
| `ssl_certs_csr_path` | "{{ ssl_certs_path }}/{{ ssl_certs_common_name }}.csr" | CSR file |
| `ssl_certs_dhparam_path` | "{{ ssl_certs_path }}/dhparam.pem" | Diffie Helman parameters file |
| `ssl_certs_local_privkey_path` | "{{ inventory_dir|default(playbook_dir) }}/files/ssl/{{ ssl_certs_common_name }}.key" | Local private key file path to deploy on server if exists |
| `ssl_certs_local_cert_path` | "{{ inventory_dir|default(playbook_dir) }}/files/ssl/{{ ssl_certs_common_name }}.pem" | Local certificate file path to deploy on server if exists |
| `ssl_certs_generate_self_signed` | true | Generated an Self Signed certificat |
| `ssl_certs_key_size` | 4096 | Key size |
| `ssl_certs_generate_dh_param` | false | Enable DH parameter generation |
| `ssl_certs_dhparam_size` | 2048 | DH parameter size |

## Dependencies                                                                                                      
                                                                                                                     
## Examples

Example to generate a self-signed SSL certificate

```YAML
 - hosts: all
   roles:
     - ssl-certs
```

This will create certificate and private key in:

- `/etc/ssl/myserver.mydomain.com.key`
- `/etc/ssl/myserver.mydomain.com.pem`

Example to deploy a SSL certificate

```YAML
 - hosts: all
   roles:
    - role: ssl-certs
      ssl_certs_common_name: "labs.lan"
```

The certificate has to be placed in `files/ssl/labs.lan.key` and `files/ssl/labs.lan.pem`. If
they don't exist, the key and a **self-signed** certificate will be generated at
`/etc/ssl/labs.lan/labs.lan.key` and `/etc/ssl/labs.lan/labs.lan.pem` using the provided common name.


Example to deploy a SSL certificate using local key/pem files

```YAML
 - hosts: all
   roles:
    - role: ssl-certs
      ssl_certs_local_privkey_path: '/path/to/labs.lan.key'
      ssl_certs_local_cert_path: '/path/to/labs.lan.pem'
```

Example to deploy a SSL certificate stored in variables

An SSL certificate and key are just text that can be stored as a variable, which is useful when
using ansible vault.

Example variable data, note how the text blob is indented. This is needed to correctly insert the
text via the template module.

```YAML
ssl_certs_local_privkey_data: |
  -----BEGIN RSA PRIVATE KEY-----
  MIIEpQIBAAKCAQEAu2uhv2cjoN4F3arUZ5cDrwuxf3koCwrKSK75as0WZoxYrpyw
  Lyx9ldyD4nGabVep0R/uAgQ/HqEf2jC7WIvGcEq8bHB9PyEEWzT8IjKQX0YTc//4
  gkHBkpyU0fVrj5nkc30EIbcbH4RHRDwye4VhP/iCPchDG7OqvCyOdm8=
  -----END RSA PRIVATE KEY-----
ssl_certs_local_cert_data: |
  -----BEGIN CERTIFICATE-----
  MIIDmzCCAoOgAwIBAgIJAKWMlgLwrBzXMA0GCSqGSIb3DQEBCwUAMGQxCzAJBgNV
  QAL3naEfBSZBl0tBohuxn8Xd3yLPuKGUOk3pSL1IJy0Ca6p+QwjkaZUd9X3gf1V2
  SEfYSaGPvfIlSuHIshno
  -----END CERTIFICATE-----
```

Then simply include the role as in the first example.
