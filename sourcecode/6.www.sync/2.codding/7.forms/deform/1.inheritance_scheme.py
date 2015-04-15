import colander
import deform
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


class AddressSchema(colander.MappingSchema):
    line1 = colander.SchemaNode(colander.String(), title='Address line 1')
    line2 = colander.SchemaNode(colander.String(), title='Address line 2',
                                missing=None)
    line3 = colander.SchemaNode(colander.String(), title='Address line 3',
                                missing=None)
    town = colander.SchemaNode(colander.String(), title='Town')
    postcode = colander.SchemaNode(colander.String(), title='Postcode')


class Business(AddressSchema):
    business_name = colander.SchemaNode(colander.String(),
                                        title='Business Name',
                                        insert_before='line1')


def inheritance_form(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    from webob import Request
    request = Request(environ)

    form = deform.Form(Business(), buttons=('submit',))
    if request.POST:
        submitted = request.POST.items()
        try:
            form.validate(submitted)
        except deform.ValidationFailure as e:
            return env.get_template('simple.html').render(form=e.render())
    return env.get_template('simple.html').render(form=form.render())


if __name__ == '__main__':
    from paste.httpserver import serve

    serve(inheritance_form, host='0.0.0.0', port=8000)
