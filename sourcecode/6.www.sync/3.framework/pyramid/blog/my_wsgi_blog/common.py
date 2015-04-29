def get_session(request):
    return request.environ.get('paste.session.factory', lambda: {})()


def get_csrf_token(session):
    if 'csrf' not in session:
        from uuid import uuid4
        session['csrf'] = uuid4().hex
    return session['csrf']
