#!/bin/bash

state=`cat {{ keepalived_tempdir }}/cluster.state 2>/dev/null`
[[ -z $state ]] && state="slave"

systemctl status keepalived >/dev/null 2>&1 && echo "$state" || echo "slave*"

exit 0
