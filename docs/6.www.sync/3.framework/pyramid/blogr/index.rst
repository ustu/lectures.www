Блог
====

.. seealso::

   * http://pyramid-blogr.readthedocs.org/en/latest/

Структура проекта
-----------------

Создадим структуру будущего блога.

.. code-block:: bash

   $ pcreate -t alchemy pyramid_blogr

.. no-code-block:: bash

   $ cd pyramid_blogr
   $ tree
   .
   ├── CHANGES.txt
   ├── development.ini  <- файл с настройками проекта
   ├── MANIFEST.in
   ├── production.ini
   ├── pyramid_blogr
   │   ├── __init__.py  <- точка входа нашего приложения, функция main.
   │   │                   Создает конфиг и возвращает WSGI-приложение.
   │   ├── models.py    <- описание схемы БД при помощи ORM SQLAlchemy
   │   ├── scripts
   │   │   ├── initializedb.py <- скрипт инициализации проекта
   │   │   └── __init__.py
   │   ├── static/      <- статические файлы (картинки, стили, javascript, ...)
   │   ├── templates/   <- шаблоны
   │   ├── tests.py
   │   └── views.py     <- вьюхи (бизнес-логика приложения)
   ├── README.txt
   └── setup.py

Базы данных
-----------

.. todo::

   * Описать работу ZopeTransactionExtension

В скаффолде ``alchemy``, который мы использовали для создания блога, уже существуют минимальные настройки для работы с БД.

Подключение к БД прописано в файле ``development.ini``.

.. code-block:: ini
   :emphasize-lines: 13

   [app:main]
   use = egg:pyramid_blogr

   pyramid.reload_templates = true
   pyramid.debug_authorization = false
   pyramid.debug_notfound = false
   pyramid.debug_routematch = false
   pyramid.default_locale_name = en
   pyramid.includes =
       pyramid_debugtoolbar
       pyramid_tm

   sqlalchemy.url = sqlite:///%(here)s/pyramid_blogr.sqlite

Объект сессии создается в файле ``pyramid_blogr/models.py``.
Там же находится базовый класс для моделей.

.. code-block:: python
   :emphasize-lines: 17,18

   from sqlalchemy import (
       Column,
       Index,
       Integer,
       Text,
       )

   from sqlalchemy.ext.declarative import declarative_base

   from sqlalchemy.orm import (
       scoped_session,
       sessionmaker,
       )

   from zope.sqlalchemy import ZopeTransactionExtension

   DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
   Base = declarative_base()


   class MyModel(Base):
       __tablename__ = 'models'
       id = Column(Integer, primary_key=True)
       name = Column(Text)
       value = Column(Integer)

   Index('my_index', MyModel.name, unique=True, mysql_length=255)

В главном файле проекта ``pyramid_blogr/__init__.py`` находится функция ``main``, которая вызывается при запуске команды ``pserve development.ini``. Причем, настройки из файла ``development.ini`` передаются в эту функцию через атрибут ``settings`` (``def main(global_config, **settings):``).

``pserve`` знает что нужно запустить функцию ``main``, потому что это указанно в самом файле настроек ``development.ini``.

.. code-block:: ini
   :emphasize-lines: 6

   ###
   # wsgi server configuration
   ###

   [server:main]
   use = egg:waitress#main
   host = 0.0.0.0
   port = 6543

Подключение к БД берется из настроек при помощи функции :func:`sqlalchemy.engine_from_config`. Далее объекту сессии и базовому классу указывается строка подключения.

.. code-block:: python
   :emphasize-lines: 13-15

   from pyramid.config import Configurator
   from sqlalchemy import engine_from_config

   from .models import (
       DBSession,
       Base,
       )


   def main(global_config, **settings):
       """ This function returns a Pyramid WSGI application.
       """
       engine = engine_from_config(settings, 'sqlalchemy.')
       DBSession.configure(bind=engine)
       Base.metadata.bind = engine
       config = Configurator(settings=settings)
       config.include('pyramid_chameleon')
       config.add_static_view('static', 'static', cache_max_age=3600)
       config.add_route('home', '/')
       config.scan()
       return config.make_wsgi_app()

pyramid_sqlalchemy
------------------

.. seealso::

   * http://pyramid-sqlalchemy.readthedocs.org/en/latest/

:l:`pyramid_sqlalchemy` - расширение для Pyramid которое делает многие настройки БД за вас.

Установка:

.. code-block:: bash

   $ pip install pyramid_sqlalchemy

Файл ``__init__.py`` стал значительно проще.

.. code-block:: python
   :emphasize-lines: 8

   from pyramid.config import Configurator


   def main(global_config, **settings):
       """ This function returns a Pyramid WSGI application.
       """
       config = Configurator(settings=settings)
       config.include('pyramid_sqlalchemy')
       config.include('pyramid_chameleon')
       config.add_static_view('static', 'static', cache_max_age=3600)
       config.add_route('home', '/')
       config.scan()
       return config.make_wsgi_app()

Базовый класс и сессия импортируются прямо из библиотеки.

* :class:`pyramid_sqlalchemy.BaseObject`
* :class:`pyramid_sqlalchemy.Session`

Поэтому можно удалить ``Base`` и  ``DBSession`` из файла ``models.py``.

.. code-block:: python
   :emphasize-lines: 8

   from sqlalchemy import (
       Column,
       Index,
       Integer,
       Text,
       )

   from pyramid_sqlalchemy import BaseObject


   class MyModel(BaseObject):
       __tablename__ = 'models'
       id = Column(Integer, primary_key=True)
       name = Column(Text)
       value = Column(Integer)

   Index('my_index', MyModel.name, unique=True, mysql_length=255)

Сессии работаю аналогично. Пример ``views.py``.

.. code-block:: python
   :emphasize-lines: 6

   from pyramid.response import Response
   from pyramid.view import view_config

   from sqlalchemy.exc import DBAPIError

   from pyramid_sqlalchemy import Session as DBSession
   from .models import MyModel


   @view_config(route_name='home', renderer='templates/mytemplate.pt')
   def my_view(request):
       try:
           one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
       except DBAPIError:
           return Response(conn_err_msg, content_type='text/plain', status_int=500)
       return {'one': one, 'project': 'pyramid_blogr'}


   conn_err_msg = """\
   Pyramid is having a problem using your SQL database.  The problem
   might be caused by one of the following things:

   A.  You may need to run the "initialize_pyramid_blogr_db" script
       to initialize your database tables.  Check your virtual
       environment's "bin" directory for this script and try to run it.

   B.  Your database server may not be running.  Check that the
       database server referred to by the "sqlalchemy.url" setting in
       your "development.ini" file is running.

   After you fix the problem, please restart the Pyramid application to
   try it again.
   """

Таблицы блога
-------------

В файле ``models.py`` заменим ``MyModel`` на таблицы блога:

* User - для авторизации
* Article - статьи

.. code-block:: python

   import datetime

   from pyramid_sqlalchemy import BaseObject
   from sqlalchemy import Column, DateTime, Integer, Unicode, UnicodeText


   class User(BaseObject):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(Unicode(255), unique=True, nullable=False)
       password = Column(Unicode(255), nullable=False)
       last_logged = Column(DateTime, default=datetime.datetime.utcnow)


   class Article(BaseObject):
       __tablename__ = 'articles'
       id = Column(Integer, primary_key=True)
       title = Column(Unicode(255), unique=True, nullable=False)
       content = Column(UnicodeText, default=u'')
       created = Column(DateTime, default=datetime.datetime.utcnow)
       edited = Column(DateTime, default=datetime.datetime.utcnow)

Инициализация
-------------

В скаффорлде существует файл инициализации проекта ``pyramid_blogr/scripts/initializedb.py``. Его можно выполнить как команду окружения:

.. code-block:: bash

   $ initialize_pyramid_blogr_db development.ini

В окружение эта команда попадает после установки (``python setup.py develop``) пакета, т.к. прописана в настройках ``setup.py``.

.. code-block:: python
   :emphasize-lines: 24-25

   # ...
   setup(name='pyramid_blogr',
         version='0.0',
         description='pyramid_blogr',
         long_description=README + '\n\n' + CHANGES,
         classifiers=[
             "Programming Language :: Python",
             "Framework :: Pyramid",
             "Topic :: Internet :: WWW/HTTP",
             "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
         ],
         author='',
         author_email='',
         url='',
         keywords='web wsgi bfg pylons pyramid',
         packages=find_packages(),
         include_package_data=True,
         zip_safe=False,
         test_suite='pyramid_blogr',
         install_requires=requires,
         entry_points="""\
         [paste.app_factory]
         main = pyramid_blogr:main
         [console_scripts]
         initialize_pyramid_blogr_db = pyramid_blogr.scripts.initializedb:main
         """,
         )

Добавим в этот скрипт инициализации, создание новых таблиц, добавление пользователя "admin" и статей.

.. no-code-block:: python
   :emphasize-lines: 8-9, 12, 32-
   :linenos:

   # -*- coding: utf-8 -*-
   import os
   import sys

   import transaction
   from pyramid.paster import get_appsettings, setup_logging
   from pyramid.scripts.common import parse_vars
   from pyramid_sqlalchemy import BaseObject as Base
   from pyramid_sqlalchemy import Session as DBSession
   from sqlalchemy import engine_from_config

   from ..models import Article, User


   def usage(argv):
       cmd = os.path.basename(argv[0])
       print('usage: %s <config_uri> [var=value]\n'
             '(example: "%s development.ini")' % (cmd, cmd))
       sys.exit(1)


   def main(argv=sys.argv):
       if len(argv) < 2:
           usage(argv)
       config_uri = argv[1]
       options = parse_vars(argv[2:])
       setup_logging(config_uri)
       settings = get_appsettings(config_uri, options=options)
       engine = engine_from_config(settings, 'sqlalchemy.')
       DBSession.configure(bind=engine)

       Base.metadata.drop_all(engine)
       Base.metadata.create_all(engine)
       with transaction.manager:
           model = User(name=u'admin', password=u'admin')
           DBSession.add(model)
           from jinja2.utils import generate_lorem_ipsum
           for id, article in enumerate(range(100), start=1):
               title = generate_lorem_ipsum(
                   n=1,         # Одно предложение
                   html=False,  # В виде обычного текста
                   min=2,       # Минимум 2 слова
                   max=5        # Максимум 5
               )
               content = generate_lorem_ipsum()
               article = Article(**{'title': title, 'content': content})
               DBSession.add(article)

Теперь при выполнении этого скрипта, наша БД будет пересоздаваться.

.. no-code-block:: bash

   $ initialize_pyramid_blogr_db development.ini

   CREATE TABLE articles (
           id INTEGER NOT NULL,
           title VARCHAR(255) NOT NULL,
           content TEXT,
           created DATETIME,
           edited DATETIME,
           PRIMARY KEY (id),
           UNIQUE (title)
   )


   2015-05-05 12:49:59,749 INFO  [sqlalchemy.engine.base.Engine][MainThread] ()
   2015-05-05 12:49:59,755 INFO  [sqlalchemy.engine.base.Engine][MainThread] COMMIT
   2015-05-05 12:49:59,755 INFO  [sqlalchemy.engine.base.Engine][MainThread]
   CREATE TABLE users (
           id INTEGER NOT NULL,
           name VARCHAR(255) NOT NULL,
           password VARCHAR(255) NOT NULL,
           last_logged DATETIME,
           PRIMARY KEY (id),
           UNIQUE (name)
   )


   2015-05-05 12:49:59,755 INFO  [sqlalchemy.engine.base.Engine][MainThread] ()
   2015-05-05 12:49:59,761 INFO  [sqlalchemy.engine.base.Engine][MainThread] COMMIT
   2015-05-05 12:49:59,764 INFO  [sqlalchemy.engine.base.Engine][MainThread] BEGIN (implicit)
   2015-05-05 12:49:59,766 INFO  [sqlalchemy.engine.base.Engine][MainThread] INSERT INTO users (name, password, last_logged) VALUES (?, ?, ?)
   2015-05-05 12:49:59,767 INFO  [sqlalchemy.engine.base.Engine][MainThread] (u'admin', u'admin', '2015-05-05 12:49:59.766198')
   2015-05-05 12:49:59,769 INFO  [sqlalchemy.engine.base.Engine][MainThread] COMMIT

URL маршруты
------------

.. tabularcolumns:: |p{6.5cm}|p{6.5cm}|
.. list-table:: URL маршруты для блога
   :header-rows: 1

   * - URL
     - Назначение
   * - \/
     - Главная страница со списком статей
   * - \/static/jquery.js
     - Статические файлы
   * - \/sign\/in
     - Вход под своей учетной записью
   * - \/sign\/out
     - Выход
   * - /add
     - Добавление новой статьи
   * - /article/13
     - Просмотр статьи с id=13
   * - /article/13/edit
     - Редактирование статьи с id=13
   * - /article/13/delete
     - Удаление статьи с id=13

Добавим пути в кофигуратор в файле ``__init__.py``.

.. code-block:: python
   :emphasize-lines: 11-15

   from pyramid.config import Configurator


   def main(global_config, **settings):
       """ This function returns a Pyramid WSGI application.
       """
       config = Configurator(settings=settings)
       config.include('pyramid_sqlalchemy')
       config.include('pyramid_chameleon')

       config.add_static_view('static', 'static', cache_max_age=3600)
       config.add_route('blog', '/')
       config.add_route('blog_article', '/article/{id:\d+}')
       config.add_route('blog_action', '/article/{id:\d+}/{action}')
       config.add_route('auth', '/sign/{action}')

       config.scan()
       return config.make_wsgi_app()

Views
-----

Создадим представления для нашего блога. Пока в виде "заглушек".

.. code-block:: python

   from pyramid.view import view_config


   @view_config(route_name='blog',
                renderer='blog/index.jinja2')
   def index_page(request):
       return {}


   @view_config(route_name='blog_article', renderer='blog/read.jinja2')
   def blog_view(request):
       return {}


   @view_config(route_name='blog_action', match_param='action=create',
                renderer='blog/edit.jinja2')
   def blog_create(request):
       return {}


   @view_config(route_name='blog_action', match_param='action=edit',
                renderer='blog/edit.jinja2')
   def blog_update(request):
       return {}


   @view_config(route_name='auth', match_param='action=in', renderer='string',
                request_method='POST')
   @view_config(route_name='auth', match_param='action=out', renderer='string')
   def sign_in_out(request):
       return {}

Главная страница
~~~~~~~~~~~~~~~~

``views.py``

.. code-block:: python

   @view_config(route_name='blog',
                renderer='blog/index.jinja2')
   def index_page(request):
       page = int(request.params.get('page', 1))
       paginator = Article.get_paginator(request, page)
       return {'paginator': paginator}

``models.py`` ``Article``

.. code-block:: python

    @classmethod
    def get_paginator(cls, request, page=1):
        query = Session.query(Article).order_by(desc(Article.created))
        query_params = request.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)
        return SqlalchemyOrmPage(query, page, items_per_page=5,
                                 url_maker=url_maker)

Просмотр статей
~~~~~~~~~~~~~~~

``views.py``

.. code-block:: python

   @view_config(route_name='blog_article', renderer='blog/read.jinja2')
   def blog_view(request):
       id = int(request.matchdict.get('id', -1))
       article = Article.by_id(id)
       if not article:
           return HTTPNotFound()
       return {'article': article}

``models.py`` ``Article``

.. code-block:: python

    @classmethod
    def by_id(cls, id):
        return Session.query(Article).filter(Article.id == id).first()

Создание и редактирование
~~~~~~~~~~~~~~~~~~~~~~~~~

``views.py``

.. code-block:: python

   @view_config(route_name='blog_create',
                renderer='blog/edit.jinja2')
   @view_config(route_name='blog_action', match_param='action=edit',
                renderer='blog/edit.jinja2')
   def blog_create(request):
       form = get_form(request)
       if request.method == 'POST':
           try:
               values = form.validate(request.POST.items())
           except deform.ValidationFailure as e:
               return {'form': e.render(),
                       'action': request.matchdict.get('action')}
           if request.matchdict['action'] == 'edit':
               article = Session.query(Article)\
                   .filter_by(id=request.matchdict['id']).one()
               article.title = request.POST['title']
               article.content = request.POST['content']
           else:
               article = Article(**values)
           Session.add(article)
           return HTTPFound(location=request.route_url('blog'))
       values = {}
       if request.matchdict['action'] == 'edit':
           values = Session.query(Article)\
               .filter_by(id=request.matchdict['id']).one().__dict__
       return {'form': form.render(values),
               'action': request.matchdict.get('action')}

Полный код
~~~~~~~~~~

.. code-block:: python

   import deform
   from pyramid.httpexceptions import HTTPFound, HTTPNotFound
   from pyramid.view import view_config
   from pyramid_sqlalchemy import Session

   from .forms import get_form
   from .models import Article


   @view_config(route_name='blog',
                renderer='blog/index.jinja2')
   def index_page(request):
       page = int(request.params.get('page', 1))
       paginator = Article.get_paginator(request, page)
       return {'paginator': paginator}


   @view_config(route_name='blog_article', renderer='blog/read.jinja2')
   def blog_view(request):
       id = int(request.matchdict.get('id', -1))
       article = Article.by_id(id)
       if not article:
           return HTTPNotFound()
       return {'article': article}


   @view_config(route_name='blog_create',
                renderer='blog/edit.jinja2')
   @view_config(route_name='blog_action', match_param='action=edit',
                renderer='blog/edit.jinja2')
   def blog_create(request):
       form = get_form(request)
       if request.method == 'POST':
           try:
               values = form.validate(request.POST.items())
           except deform.ValidationFailure as e:
               return {'form': e.render(),
                       'action': request.matchdict.get('action')}
           if request.matchdict.get('action', '') == 'edit':
               article = Session.query(Article)\
                   .filter_by(id=request.matchdict['id']).one()
               article.title = request.POST['title']
               article.content = request.POST['content']
           else:
               article = Article(**values)
           Session.add(article)
           return HTTPFound(location=request.route_url('blog'))
       values = {}
       if request.matchdict.get('action', '') == 'edit':
           values = Session.query(Article)\
               .filter_by(id=request.matchdict['id']).one().__dict__
       return {'form': form.render(values),
               'action': request.matchdict.get('action')}


   @view_config(route_name='blog_action', match_param='action=delete')
   def blog_delete(request):
       article = Session.query(Article)\
           .filter_by(id=request.matchdict['id']).one()
       Session.delete(article)
       return HTTPFound(location=request.route_url('blog'))


   @view_config(route_name='auth', match_param='action=in', renderer='string',
                request_method='POST')
   @view_config(route_name='auth', match_param='action=out', renderer='string')
   def sign_in_out(request):
       return {}
