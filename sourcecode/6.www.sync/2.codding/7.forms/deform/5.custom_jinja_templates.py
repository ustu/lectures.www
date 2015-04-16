import os

import colander
import deform
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


def jinja2_renderer(template_name, **kw):
    kw['_'] = str  # Hook for translation string with gettext

    from jinja2 import Template
    deform_jinja_path = os.path.abspath('templates/deform_jinja2')
    jinja2_template = os.path.join(deform_jinja_path,
                                   template_name + '.jinja2')
    template = Template(open(jinja2_template).read())
    return template.render(**kw)


class Contact(colander.MappingSchema):
    email = colander.SchemaNode(colander.String(), validator=colander.Email())
    name = colander.SchemaNode(colander.String())
    message = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.TextAreaWidget())


def custom_template_form(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    from webob import Request
    request = Request(environ)

    form = deform.Form(Contact(), buttons=('submit',),
                       renderer=jinja2_renderer)
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
