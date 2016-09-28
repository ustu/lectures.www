from middlewares.urldispatch import RegexDispatch

ARTICLES = [
    {'id': 1, 'title': 'Lorem ipsum dolor sid amet!',
     'content': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     Curabitur vel tortor eleifend, sollicitudin nisl quis, lacinia augue.
     Duis quam est, laoreet sit amet justo vitae, viverra egestas sem.
     Maecenas pellentesque augue in nibh feugiat tincidunt. Nunc magna ante,
     mollis vitae ultricies eu, consectetur id ante. In ut libero eleifend,
     blandit ipsum a, ullamcorper nunc. Sed bibendum eget odio eget
     pellentesque. Curabitur elit felis, pellentesque id feugiat et, tincidunt
     ut mauris. Integer vitae vehicula nunc. Integer ullamcorper, nunc in
     volutpat auctor, elit leo convallis nulla, vitae varius mi nisl ac lorem.
     Sed a lacus mi. In hac habitasse platea dictumst. Cras in posuere velit,
     id dignissim nisl. Interdum et malesuada fames ac ante ipsum primis in
     faucibus. Nulla bibendum suscipit convallis.'''},
    {'id': 2, 'title': 'Hello', 'content': 'Test2'},
    {'id': 3, 'title': 'World', 'content': 'Test2'}, ]


class BaseBlog(object):

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response


class BaseArticle(BaseBlog):

    def __init__(self, *args):
        super(BaseArticle, self).__init__(*args)
        article_id = self.environ['url_params']['id']
        (self.index,
         self.article) = next(((i, art) for i, art in enumerate(ARTICLES)
                               if art['id'] == int(article_id)),
                              (None, None))


class BlogIndex(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/html')])
        yield b'<h1>Simple Blog</h1>'
        for article in ARTICLES:
            yield str.encode(
                '''
                {0} - <a href="/article/{0}">{1}</a>
                (<a href="/article/{0}/delete">delete</a>)<br/>
                '''.format(
                    article['id'],
                    article['title']
                )
            )


class BlogCreate(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog -> CREATE'


class BlogRead(BaseArticle):

    def __iter__(self):
        if not self.article:
            self.start('404 Not Found', [('content-type', 'text/plain')])
            yield b'not found'
            return

        self.start('200 OK', [('Content-Type', 'text/html')])
        yield b'<h1><a href="/">Simple Blog</a> -> READ</h1>'
        yield str.encode('<h2>{}</h2>'.format(self.article['title']))
        yield str.encode(self.article['content'])


class BlogUpdate(BaseArticle):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b'Simple Blog -> UPDATE'


class BlogDelete(BaseArticle):

    def __iter__(self):
        self.start('302 Found',  # '301 Moved Permanently',
                   [('Content-Type', 'text/html'),
                    ('Location', '/')])
        ARTICLES.pop(self.index)
        yield b''


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
