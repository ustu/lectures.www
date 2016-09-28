from middlewares.urldispatch import URLDispatch


def blog(environ, start_response):
    start_response(
        '200 OK',
        [('Content-Type', 'text/plain')]
    )
    return [b'Simple Blog', ]


# URL dispatching middleware
app_list = [
    ('/', blog),
]
dispatch = URLDispatch(app_list)

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(dispatch, host='0.0.0.0', port=8000)
