import deform
import colander


def get_session(request):
    return request.environ.get('paste.session.factory', lambda: {})()


def get_csrf_token(session):
    if 'csrf' not in session:
        from uuid import uuid4
        session['csrf'] = uuid4().hex
    return session['csrf']


def get_form(request):
    session = get_session(request)
    session['csrf'] = get_csrf_token(session)
    schema = CreateArticle().bind(request=request)
    submit = deform.Button(name='submit',
                           css_class='blog-form__button')
    return deform.Form(schema, buttons=(submit,))


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
                               widget=deform.widget.HiddenWidget(), )


class CreateArticle(colander.Schema):
    title = colander.SchemaNode(colander.String())
    content = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(
            css_class="blog-form-field__textarea")
    )
