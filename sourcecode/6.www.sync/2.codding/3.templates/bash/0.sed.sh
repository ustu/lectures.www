#! /bin/bash
#
# nginx.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#

SRC_SERVER_PUB_IP=192.168.0.100
SRC_SERVER_LOCAL_IP=`hostname -I | cut -d' ' -f1`
FQDN=example.com

sed -e "s/{{ SRC_SERVER_PUB_IP }}/${SRC_SERVER_PUB_IP}/"\
  -e "s/{{ SRC_SERVER_LOCAL_IP }}/${SRC_SERVER_LOCAL_IP}/"\
  -e "s/{{ FQDN }}/${FQDN}/g" < 0.nginx_proxy_conf.tpl > proxy.nginx.conf
