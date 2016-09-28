from middlewares.urldispatch import RegexDispatch


class BaseBlog(object):

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response


class BlogIndex(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog'


class BlogCreate(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog -> CREATE'


class BlogRead(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog -> READ'


class BlogUpdate(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog -> UPDATE'


class BlogDelete(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog -> DELETE'


# URL dispatching middleware
app_list = [
    ('/', BlogIndex),
    ('/article/add', BlogCreate),
    (r'^/article/(?P<id>\d+)/$', BlogRead),
    (r'^/article/(?P<id>\d+)/edit/$', BlogUpdate),
    (r'^/article/(?P<id>\d+)/delete/$', BlogDelete),
]
dispatch = RegexDispatch(app_list)

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(dispatch, host='0.0.0.0', port=8000)
