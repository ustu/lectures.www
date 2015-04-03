# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('foopkg/templates'))
template = env.get_template('0.hello.html')
print(template.render(name='Петя'))
