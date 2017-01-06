#!/bin/sh
semodule -i /var/tmp/bacula-fd.pp
mkdir /var/run/bacula/
/sbin/semanage fcontext -a -t bacula_store_t /srv/backups\(/.*\)
if [ -d /srv/backups ]; then
	/sbin/restorecon -Rv /srv/backups
fi
