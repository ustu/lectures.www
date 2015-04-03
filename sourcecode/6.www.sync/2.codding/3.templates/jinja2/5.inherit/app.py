# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('index.html')
print(template.render(name=u'Петя'))
