# -*- coding: utf-8 -*-
from jinja2 import Environment, FunctionLoader, PackageLoader, ChoiceLoader

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

env = Environment(loader=ChoiceLoader({
    FunctionLoader(myloader),
    PackageLoader('foopkg', 'templates')
}))
template1 = env.get_template('index.html')
template2 = env.get_template('0.hello.html')
print(template1.render(name=u'Петя'))
print(template2.render(name=u'Петя'))
