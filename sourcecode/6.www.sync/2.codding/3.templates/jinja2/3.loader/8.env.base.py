# -*- coding: utf-8 -*-
from os.path import exists, getmtime, join

from jinja2 import BaseLoader, Environment, TemplateNotFound


class FoopkgLoader(BaseLoader):

    def __init__(self, path="foopkg/templates"):
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with open(path) as f:
            source = f.read().decode('utf-8')
        return source, path, lambda: mtime == getmtime(path)

# Environment
env = Environment(loader=FoopkgLoader())
template = env.get_template('0.hello.html')
print(template.render(name=u'Петя'))
