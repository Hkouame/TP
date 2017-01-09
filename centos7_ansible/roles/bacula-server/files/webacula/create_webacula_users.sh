#!/bin/sh


echo "update webacula_users set  role_id = '1' , pwd = '\$P\$Bii4p6OK7exg6YAdUl9oHtEUvpjKuE/' where id = 1000;"|/usr/bin/mysql --user=bacula --password=bacula bacula
