#! /bin/bash
#
# nginx.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#


# render a template configuration file
# expand variables + preserve formatting
render_template() {
  eval "echo \"$(cat $1)\""
}

SRC_SERVER_PUB_IP=192.168.0.100
SRC_SERVER_LOCAL_IP=`hostname -I | cut -d' ' -f1`
FQDN=example.com

render_template 1.nginx_proxy_conf.tpl > proxy.nginx.conf
