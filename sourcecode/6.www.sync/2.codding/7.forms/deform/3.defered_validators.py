import colander
import deform
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


def get_session(request):
    return request.environ.get('paste.session.factory', lambda: {})()


def get_csrf_token(session):
    if 'csrf' not in session:
        from uuid import uuid4
        session['csrf'] = uuid4().hex
    return session['csrf']


@colander.deferred
def deferred_csrf_default(node, kw):
    request = kw.get('request')
    session = get_session(request)
    csrf_token = get_csrf_token(session)
    return csrf_token


@colander.deferred
def deferred_csrf_validator(node, kw):
    def validate_csrf_token(node, value):
        request = kw.get('request')
        session = get_session(request)
        csrf_token = get_csrf_token(session)
        if value != csrf_token:
            raise colander.Invalid(node, 'Bad CSRF token')

    return validate_csrf_token


class CSRFSchema(colander.Schema):
    csrf = colander.SchemaNode(colander.String(),
                               default=deferred_csrf_default,
                               validator=deferred_csrf_validator,
                               # widget=deform.widget.HiddenWidget(), )
                               )


class Contact(CSRFSchema):
    email = colander.SchemaNode(colander.String(), validator=colander.Email())
    name = colander.SchemaNode(colander.String())
    message = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.TextAreaWidget())


def custom_validator_form(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    from webob import Request
    request = Request(environ)
    session = get_session(request)
    session['csrf'] = get_csrf_token(session)

    schema = Contact().bind(request=request)
    form = deform.Form(schema, buttons=('submit',))
    template = env.get_template('simple_with_css.html')
    if request.POST:
        submitted = request.POST.items()
        try:
            form.validate(submitted)
        except deform.ValidationFailure as e:
            return template.render(form=e.render()).encode("utf-8")
        session.pop('csrf')
        return template.render(form='OK')
    return template.render(form=form.render()).encode("utf-8")


if __name__ == '__main__':
    from paste.httpserver import serve
    from paste.session import SessionMiddleware

    app = SessionMiddleware(custom_validator_form)

    serve(app, host='0.0.0.0', port=8000)
