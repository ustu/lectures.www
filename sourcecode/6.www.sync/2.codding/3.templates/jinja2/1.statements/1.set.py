# -*- coding: utf-8 -*-
from jinja2 import Template
template = Template("{% set a, b, c = 'foo', 'фуу', 'föö' %}")
m = template.module
print(m.a)
print(m.b)
print(m.c)
