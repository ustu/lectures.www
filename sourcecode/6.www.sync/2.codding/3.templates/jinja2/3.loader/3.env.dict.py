# -*- coding: utf-8 -*-
from jinja2 import Environment, DictLoader

html = '''<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  </head>
  <body>
    {% for item in range(5) %}
      Hello {{ name }}!
    {% endfor %}
  </body>
</html>
'''

env = Environment(loader=DictLoader({'index.html': html}))
template = env.get_template('index.html')
print(template.render(name=u'Петя'))
