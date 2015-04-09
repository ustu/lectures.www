from paste.urlparser import StaticURLParser
from paste import httpserver

static_app = StaticURLParser(".")

if __name__ == '__main__':
    httpserver.serve(static_app, host='0.0.0.0', port='8000')
