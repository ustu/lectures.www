# -*- coding: utf-8 -*-
from jinja2 import Template

html = open('foopkg/templates/0.hello.html').read()
template = Template(html)
print(template.render(name=u'Петя'))
