import os

import colander
import deform
from jinja2 import Environment, FileSystemLoader
from pkg_resources import resource_filename

env = Environment(loader=FileSystemLoader('templates'))


deform_path = os.path.abspath('templates/deform')
deform_templates = resource_filename('deform', 'templates')
print(deform_templates)
print(deform_path)
search_path = (deform_path, deform_templates)
renderer = deform.ZPTRendererFactory(search_path)


class Contact(colander.MappingSchema):
    email = colander.SchemaNode(colander.String(), validator=colander.Email())
    name = colander.SchemaNode(colander.String())
    message = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.TextAreaWidget())


def custom_template_form(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    from webob import Request
    request = Request(environ)

    form = deform.Form(Contact(), buttons=('submit',), renderer=renderer)
    template = env.get_template('simple_with_css.html')
    if request.POST:
        submitted = request.POST.items()
        try:
            form.validate(submitted)
        except deform.ValidationFailure as e:
            return template.render(form=e.render()).encode("utf-8")
    data = {'email': 'jon.staley@fundingoptions.com',
            'name': 'Jon',
            'message': 'Hello World'}
    return template.render(form=form.render(data)).encode("utf-8")


if __name__ == '__main__':
    from paste.httpserver import serve

    serve(custom_template_form, host='0.0.0.0', port=8000)
