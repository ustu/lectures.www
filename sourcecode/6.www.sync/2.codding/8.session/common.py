from beaker.session import Session


def get_session(request={}, **kwargs):
    """A shortcut for creating :class:`Session` instance"""
    options = {}
    options.update(**kwargs)
    return Session(request, **options)
