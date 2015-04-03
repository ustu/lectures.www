# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('foopkg', 'templates'))

template = env.get_template('0.hello.html')
print(template.render(name=u'Петя'))
