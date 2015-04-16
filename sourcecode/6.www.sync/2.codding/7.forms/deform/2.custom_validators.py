import colander
import deform
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


def month_validator(node, month):
    if month.isdigit():
        int_month = int(month)
        if not 0 < int_month < 13:
            raise colander.Invalid(node,
                                   'Please enter a number between 1 and 12')
    else:
        raise colander.Invalid(node, 'Please enter a number')


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
    start_month = colander.SchemaNode(colander.String(), title='Start month',
                                      validator=month_validator)


def custom_validator_form(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    from webob import Request
    request = Request(environ)

    form = deform.Form(Business(), buttons=('submit',))
    template = env.get_template('simple_with_css.html')
    if request.POST:
        submitted = request.POST.items()
        try:
            form.validate(submitted)
        except deform.ValidationFailure as e:
            return template.render(form=e.render()).encode("utf-8")
    return template.render(form=form.render()).encode("utf-8")


if __name__ == '__main__':
    from paste.httpserver import serve

    serve(custom_validator_form, host='0.0.0.0', port=8000)
