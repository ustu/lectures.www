def blog(environ, start_response):
    start_response(
        '200 OK',
        [('Content-Type', 'text/plain')]
    )
    return [b'Simple Blog', ]


if __name__ == '__main__':
    from paste.httpserver import serve
    serve(blog, host='0.0.0.0', port=8000)
