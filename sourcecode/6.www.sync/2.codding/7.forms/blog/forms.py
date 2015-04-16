import deform
import colander

from common import get_csrf_token, get_session


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


class CreateArticle(CSRFSchema):
    title = colander.SchemaNode(colander.String())
    content = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(
            css_class="blog-form-field__textarea")
    )
