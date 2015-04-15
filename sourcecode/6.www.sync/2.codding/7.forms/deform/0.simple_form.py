import colander
import deform
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


class Contact(colander.MappingSchema):
    email = colander.SchemaNode(colander.String(), validator=colander.Email())
    name = colander.SchemaNode(colander.String())
    message = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.TextAreaWidget())


def simple_form(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    from webob import Request
    request = Request(environ)

    form = deform.Form(Contact(), buttons=('submit',))
    if request.POST:
        submitted = request.POST.items()
        try:
            form.validate(submitted)
        except deform.ValidationFailure as e:
            return env.get_template('simple.html').render(form=e.render())
    data = {'email': 'jon.staley@fundingoptions.com',
            'name': 'Jon',
            'message': 'Hello World'}
    return env.get_template('simple.html').render(form=form.render(data))


if __name__ == '__main__':
    from paste.httpserver import serve

    serve(simple_form, host='0.0.0.0', port=8000)
