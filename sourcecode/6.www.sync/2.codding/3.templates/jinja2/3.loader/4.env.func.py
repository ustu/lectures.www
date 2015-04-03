# -*- coding: utf-8 -*-
from jinja2 import Environment, FunctionLoader

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


def myloader(name):
    if name == 'index.html':
        return html

env = Environment(loader=FunctionLoader(myloader))
template = env.get_template('index.html')
print(template.render(name=u'Петя'))
