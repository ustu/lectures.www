# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader, ModuleLoader

# Compile template
Environment(loader=FileSystemLoader('foopkg/templates'))\
    .compile_templates("foopkg/compiled/foopkg.zip",
                       py_compile=True)  # pyc generate

# Environment
env = Environment(loader=ModuleLoader("foopkg/compiled/foopkg.zip"))
template = env.get_template('0.hello.html')
print(template.render(name=u'Петя'))
