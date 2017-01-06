#!/bin/sh
/sbin/setsebool -P nagios_run_sudo 1
/sbin/semanage fcontext -a -t etc_t /etc/nagios/nrpe.d\(/.*\)
/sbin/semodule -i /var/tmp/nrpe.pp
/sbin/semodule -i /var/tmp/nrpe-named.pp
/sbin/restorecon -Rv /etc/nrpe.d/*
