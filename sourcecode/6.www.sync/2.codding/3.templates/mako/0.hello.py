# -*- coding: utf-8 -*-
from mako.template import Template

template = Template('Hello ${ name }!')
print(template.render(name=u'Вася'))
