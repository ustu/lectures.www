#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('nginx_proxy_conf.tpl')

data = {
    "SRC_SERVER_PUB_IP": "192.168.0.100",
    "SRC_SERVER_LOCAL_IP": "10.0.3.100",
    "FQDN": "example.com"
}

conf = template.render(**data)
print(conf)

open("proxy.nginx.conf", "w").write(conf)
