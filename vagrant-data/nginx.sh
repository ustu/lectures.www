#! /bin/bash
#
# nginx.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#

LECTURESWWW_IP=`hostname -I | cut -d' ' -f1`

cd ~/sourcecode/nginx/templates/
cat fcgi.nginx.template | sed -e "s/\${FASTCGI_HELLO}/${LECTURESWWW_IP}/" > \
    ~/sourcecode/nginx/includes/fcgi.nginx
