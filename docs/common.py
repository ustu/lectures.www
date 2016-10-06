BOOKS_LINKS = {
    'patterns of enterprise application architecture':
    'http://www.martinfowler.com/books/eaa.html',
}

PEOPLE_LINKS = {
    'ian bicking': 'http://www.ianbicking.org/',
    'martin flower': 'http://www.martinfowler.com/',
}

PYLONS_LINKS = {
    'webob': 'http://docs.webob.org/',
    'colander': 'http://docs.pylonsproject.org/projects/colander/en/latest/',
    'deform': 'http://deform.readthedocs.org/en/latest/',
    'chameleon': 'http://pyramid-chameleon.readthedocs.org/en/latest/',
    'peppercorn':
    'http://docs.pylonsproject.org/projects/peppercorn/en/latest/',
    'pyramid_jinja2':
    'http://docs.pylonsproject.org/projects/pyramid-jinja2/en/latest/',
    'cornice': 'http://cornice.rtfd.org',
    'pyramid_mailer': 'http://pyramid-mailer.readthedocs.org/en/latest/',
    'pyramid_tm': 'http://pyramid-tm.readthedocs.org/en/latest/',

    # Zope
    'transaction': 'http://zodb.readthedocs.org/en/latest/transactions.html',

    # Sacrud
    'pyramid_sacrud': 'https://github.com/sacrud/pyramid_sacrud',
}

DATABASE_LINKS = {
    # NoSQL
    'memcached': 'https://ru.wikipedia.org/wiki/Memcached',
    'redis': 'https://ru.wikipedia.org/wiki/Redis',

    # SQL
    'sqlite': 'http://sqlite.org/',
    'postgres': 'http://postgresql.org',
    'postgresql': 'http://postgresql.org',

    # Python
    'db-api': 'https://www.python.org/dev/peps/pep-0249/',
    'db-api 2.0': 'https://www.python.org/dev/peps/pep-0249/',
    'zodb': 'http://www.zodb.org/',
    'zeo': 'https://pypi.python.org/pypi/ZEO',

    # ORM
    'sqlalchemy': 'http://sqlalchemy.org/',
    'pyramid_sqlalchemy': 'http://pyramid-sqlalchemy.readthedocs.org',
    'sqlobject': 'http://www.sqlobject.org/index.html',
    'sqlbuilder': 'http://www.sqlobject.org/SQLBuilder.html',
    'hibernate': 'http://hibernate.org',
}

FRAMEWORK_LINKS = {
    'pyramid': 'http://pylonsproject.org/',
    'pylons':
    'http://docs.pylonsproject.org/projects/pylons-webframework/en/latest/',
    'repoze.bfg': 'http://bfg.repoze.org',
    'zope': 'http://www.zope.org/',
    'plone': 'https://plone.org/',
    'flask': 'http://flask.pocoo.org/',
    'turbogears': 'http://www.turbogears.org/',
    'django': 'https://www.djangoproject.com/',
    'web2py': 'http://web2py.com',
    'ruby on rails': 'http://rubyonrails.org/',

    # GUI
    'electron': 'http://electron.atom.io/',

    # Async
    'pulsar': 'http://pythonhosted.org/pulsar/',
    'tornado': 'http://www.tornadoweb.org/en/stable/',
}

JS_LINKS = {
    'requirejs': 'http://requirejs.org/',
    'webpack': 'https://webpack.github.io/',
}

OTHER_LINKS = {
    # OS
    'nix': 'http://nixos.org/nix/',
    'nixos': 'http://nixos.org/',

    # Web servers
    'nginx': 'http://nginx.org/',
    'paste': 'http://pythonpaste.org/',
    'waitress': 'https://waitress.readthedocs.org/',
    'gunicorn': 'http://docs.gunicorn.org/en/stable/',

    # Language
    'python': 'http://www.python.org/',
    'java': 'http://www.java.com',
    'nodejs': 'https://nodejs.org/en/',

    # Template engine
    'jinja': 'http://jinja.pocoo.org/',
    'jinja2': 'http://jinja.pocoo.org/',
    'mako': 'http://www.makotemplates.org/',

    # Forms
    'colanderalchemy': 'http://colanderalchemy.readthedocs.org/en/latest/',

    # Cache and Session
    'beaker': 'https://beaker.readthedocs.org/en/latest/',

    # SCV
    'git': 'http://git-scm.com/',

    # Async
    'gevent': 'http://www.gevent.org/',
    'asyncio': 'https://docs.python.org/3/library/asyncio.html',

    # Other
    'zenoss': 'www.zenoss.com/',
    'erp5': 'https://ru.wikipedia.org/wiki/ERP5',
    'numpy': 'http://www.numpy.org/',
    'vscode': 'https://code.visualstudio.com/',
    'visual studio code': 'https://code.visualstudio.com/',
    'wingware': 'https://wingware.com/',
    'qtcreator': 'https://www.qt.io/ide/',
}

ASYNC_LINKS = {
    'asyncio': 'https://docs.python.org/3/library/asyncio.html',
    'aiohttp': 'https://aiohttp.readthedocs.org/'
}

GLOBAL_LINKS = dict(
    list(PYLONS_LINKS.items()) +
    list(OTHER_LINKS.items()) +
    list(DATABASE_LINKS.items()) +
    list(FRAMEWORK_LINKS.items()) +
    list(PEOPLE_LINKS.items()) +
    list(BOOKS_LINKS.items()) +
    list(JS_LINKS.items()) +
    list(ASYNC_LINKS.items())
)
