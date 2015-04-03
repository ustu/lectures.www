# -*- coding: utf-8 -*-
from jinja2 import Template

template = Template('Hello {{ name }}!')
print(template.render(name=u'Вася'))
