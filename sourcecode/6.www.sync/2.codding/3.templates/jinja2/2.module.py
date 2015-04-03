# -*- coding: utf-8 -*-
from jinja2 import Template

template = Template('{% macro foo() %}42{% endmacro %}23')
m = template.module
print(m)
print(m.foo())
