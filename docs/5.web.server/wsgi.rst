.. _wsgi:

WSGI (pep-333)
==============

.. seealso::

    * http://legacy.python.org/dev/peps/pep-0333/
    * https://ru.wikipedia.org/wiki/WSGI
    * http://docs.repoze.org/moonshining/pep333.html
    * http://pylonsbook.com/en/1.1/the-web-server-gateway-interface-wsgi.html
    * http://pylons-webframework.readthedocs.org/en/latest/concepts.html
    * http://www.docstoc.com/docs/69863691/WSGI-from-Start-to-Finish

.. figure:: /_static/6.www.sync/wsgi/wsgi.*
   :align: center
   :scale: 80


**WSGI** — стандарт взаимодействия между Python-программой, выполняющейся на стороне сервера, и самим веб-сервером, например, Apache.

**Идея:**

В Python существует большое количество различного рода веб-фреймворков, тулкитов и библиотек. Для каждого из них — собственный метод установки и настройки, они не умеют взаимодействовать между собой. Это может стать затруднением для тех, кто только начинает изучать Python, так как, например, выбор определённого фреймворка может ограничить выбор веб-сервера, и наоборот.

WSGI предоставляет простой и универсальный интерфейс между большинством веб-серверов и веб-приложениями или фреймворками.

.. figure:: /_static/6.www.sync/wsgi/wsgi_ianb.png
   :align: center

   Пример работы `WSGI` (автор Ян Бикинг)

Application
-----------

По стандарту, **WSGI-приложение** должно удовлетворять следующим требованиям:

* должно быть вызываемым (callable) объектом (обычно это функция или метод)
* принимать два параметра:

  + словарь переменных окружения (**environ**)
  + обработчик запроса (**start_response**)

* вызывать обработчик запроса с кодом HTTP-ответа и HTTP-заголовками
* возвращать итерируемый объект с телом ответа

Простейшим примером WSGI-приложения может служить такая функция-генератор:

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/1.cgi.app.py
   :language: python
   :pyobject: simple_app
   :linenos:

.. figure:: /_static/6.www.sync/wsgi/wsgi-app.png
   :align: center
   :width: 400pt

   `WSGI-приложение`

или то же самое в виде класса:

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/1.cgi.app.py
   :language: python
   :pyobject: AppClass
   :linenos:

Server/Gateway
--------------

Что бы запустить наше WSGI приложение нужен **WSGI сервер**.
Он запускает один раз `WSGI приложение`, при каждом HTTP запросе от клиента.

Задачи WSGI сервера:

* Сформировать переменные окружения (**environment**)
* Описать функцию обработчик запроса (**start_response**)
* Передать их в **WSGI приложение**
* Полученные данные **WSGI сервер** отправляет по HTTP клиенту
* а **WSGI шлюз** приводит к формату клиент-серверного протокола (CGI, FastCGI, SCGI, uWSGI, ...)
  и передает их на Веб-сервер (например выводит в stdout, stderr).

.. figure:: /_static/6.www.sync/wsgi/server-app.png
   :align: center
   :width: 400pt

   `WSGI-сервер`

Пример WSGI-шлюза к CGI-серверу.

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/cgi_gateway.py
   :language: python
   :linenos:

Environment
~~~~~~~~~~~

Всегда словарь

* ``environ`` это обычно копия переменных окружения ОС ``os.environ`` + стандартные CGI переменные.

  ``SCRIPT_NAME`` - содержит имя вызванного скрипта. Например: myapp.py

  ``PATH_INFO`` - путь к файлу ``/cgi-bin/myapp.py``

* также включает в себя дополнительные WSGI-специфичные переменные, наиболее важные из них:

  ``wsgi.input`` - представляет тело (body) HTTP запроса.

  ``wsgi.errors`` - указывает поток куда нужно выводить ошибки.

  ``wsgi.url_scheme`` - это просто "http" или "https".

start_response
~~~~~~~~~~~~~~

.. seealso::

   * `Реализация в mod_wsgi для Apache <https://code.google.com/p/modwsgi/source/browse/mod_wsgi/mod_wsgi.c#2678>`_

Функция ``start_response`` принимает два обязательных аргумента:

* ``status`` - строка содержащая статус HTTP ответа, например ``200 OK``.
* ``response_headers`` - список кортежей, которые содержат заголовки ответа, например
  ``[('Content-Type', 'text/html'), ('Content-Length', '15')``.

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/1.cgi.app.py
   :language: python
   :pyobject: simple_app
   :emphasize-lines: 2-4
   :linenos:

``start_response`` возвращает вызываемый объект, обычно "write".
``write`` выводит тело ответа в поток вывода, используется при необычных обстоятельствах.

.. warning::

   Обратный вызов ``write`` плохо поддерживается серверами и веб-фреймворками,
   поэтому рекомендуется проектировать свои приложения без его вызова.

Обычно данные возвращаются, таким образом:

.. code-block:: python

   def application(environ, start_response):
       start_response(status, headers)
       return ['content block 1',
               'content block 2',
               'content block 3']

Но можно делать и так:

.. code-block:: python

   def application(environ, start_response):
       write = start_response(status, headers)
       write('content block 1')
       return ['content block 2',
               'content block 3']

Запуск нашего приложения через WSGI-шлюз к CGI

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/1.cgi.app.py
   :language: python
   :linenos:

Результат выполнения:

.. code-block:: bash

   $ python 1.cgi.app.py
   Status: 200 OK
   Content-type: text/plain

   Hello world!

.. note:: В исходных кодах к лекциям  ``cgiserver.py``, делает этот пример доступным по адресу
   http://localhost:8000/wsgi/1.cgi.app.py

Middleware
----------

.. figure:: /_static/6.www.sync/wsgi/server-middleware-app.png
   :align: center
   :width: 500pt

   `WSGI-middleware`

Помимо приложений и серверов, стандарт дает определение **middleware-компонентов**, предоставляющих интерфейсы как приложению, так и серверу. То есть для сервера middleware является приложением, а для приложения — сервером. Это позволяет составлять «цепочки» WSGI-совместимых middleware.

Middleware могут брать на себя следующие функции (но не ограничиваются этим):

* обработка сессий
* аутентификация/авторизация
* управление URL (маршрутизация запросов)
* балансировка нагрузки
* пост-обработка выходных данных (например, проверка на валидность)

Мы рассмотри пример, приложения которое считает количество обращений и использует
следующие middleware:

* Обработчик исключений
* Сессии
* Сжатие Gzip
* Пони

.. figure:: /_static/vector/wsgi_as_onion.*

Приложение
~~~~~~~~~~

.. figure:: /_static/6.www.sync/wsgi/wsgi_as_onion_app.png
   :width: 400pt
   :align: left

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/3.http.middleware.py
   :language: python
   :pyobject: app
   :linenos:

.. raw:: html

   <br clear="all" />

Приложение выводи число 1 при первом обращении, записывает его в сессию и при каждом
последующем обращении увеличивает число на 1.

.. figure:: /_static/6.www.sync/wsgi/wsgi_example.png

Т.к. протокол HTTP не сохраняет предыдущего состояния, то при обновлении страницы число не увеличится. Что бы это произошло нужно реализовать механизм сессии.

Обработчик исключений
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/6.www.sync/wsgi/wsgi_as_onion_evalexception.png
   :width: 400pt
   :align: left

.. code-block:: python
   :linenos:

   from paste.evalexception.middleware import EvalException
   app = EvalException(app)

.. raw:: html

   <br clear="all" />

``EvalException`` позволяет нам отлавливать ошибки и выводить их в браузере.
Если мы перейдем по адресу http://localhost:8000/Errors_500, наше приложение
найдет слово `error` в пути и искусственно вызовет исключение.

.. figure:: /_static/6.www.sync/wsgi/wsgi_example_error.png

Сессии
~~~~~~

.. figure:: /_static/6.www.sync/wsgi/wsgi_as_onion_session.png
   :width: 400pt
   :align: left

.. code-block:: python
   :linenos:

   from paste.session import SessionMiddleware
   app = SessionMiddleware(app)

.. raw:: html

   <br clear="all" />

``SessionMiddleware`` добавляет cookie клиенту с ключом `_SID_` и номером сессии.

Например ``_SID_=20150313142600-d18ec118fff970ad4fb3628fbf530bc4``

Для каждой сессии на сервере в директории ``/tmp/`` (по умолчанию) создается файл с таким же именем.

.. no-code-block:: bash
   :emphasize-lines: 4

   $ tree /tmp/
   /tmp/
   |-- 20150313094744-5d2e448000e6312d7c0b8a02ed954d22
   `-- 20150313142600-d18ec118fff970ad4fb3628fbf530bc4

   1 directory, 2 files

В этот файл записывается значение ``count`` для нашей сессии. При каждом обращении клиента
``SessionMiddleware`` находит файл с таким же именем как у cookie ``_SID_`` десереализует
объекты в нем и присваивает переменной окружения ``paste.session.factory``. Таким образом
мы можем хранить состояние сессии и при каждом обновлении будет отдаваться значение увеличенное на 1.

.. figure:: /_static/6.www.sync/wsgi/wsgi_example_count.png

Сжатие Gzip
~~~~~~~~~~~

.. figure:: /_static/6.www.sync/wsgi/wsgi_as_onion_gzip.png
   :width: 400pt
   :align: left

.. code-block:: python
   :linenos:

   from paste.gzipper import middleware as GzipMiddleware
   app = GzipMiddleware(app)

.. raw:: html

   <br clear="all" />

``GzipMiddleware`` сжимает ответ методом gzip

.. figure:: /_static/6.www.sync/wsgi/wsgi_example_gzip.png

Pony
~~~~

.. figure:: /_static/6.www.sync/wsgi/wsgi_as_onion_pony.png
   :width: 400pt
   :align: left

.. code-block:: python
   :linenos:

   from paste.pony import PonyMiddleware
   app = PonyMiddleware(app)

.. raw:: html

   <br clear="all" />

Это самое важное расширение в WSGI. Доступно по адресу http://localhost:8000/pony.

.. figure:: /_static/6.www.sync/wsgi/wsgi_example_pony.png

Полный пример
~~~~~~~~~~~~~

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/wsgi/3.http.middleware.py
   :language: python
   :linenos:

Свой middleware
~~~~~~~~~~~~~~~

.. code-block:: python
   :linenos:

   class GoogleRefMiddleware(object):
       def __init__(self, app):
           self.app = app

       def __call__(self, environ, start_response):
           environ['google'] = False
           if 'HTTP_REFERER' in environ:
               if environ['HTTP_REFERER'].startswith('http://google.com'):
                   environ['google'] = True
           return self.app(environ, start_response)

   app = GoogleRefMiddleware(app)

``GoogleRefMiddleware`` добавляет переменную окружения ``google`` и если бы мы перешли
на наш сайт из поиска ``google.com``, тo это значение было бы ``True``.

Кто использует WSGI?
--------------------

* BlueBream
* bobo
* Bottle
* CherryPy
* Django
* Eventlet
* Flask
* Google App Engine's webapp2
* Gunicorn
* prestans
* mod_wsgi для Apache
* MoinMoin
* netius
* Plone
* Pylons
* Pyramid
* repoze
* restlite
* Tornado
* Trac
* TurboGears
* Uliweb
* webpy
* Falcon
* web2py
* weblayer
* Werkzeug
* Zope
* и многие другие

Аналоги
-------

* `Rack <https://en.wikipedia.org/wiki/Rack_(web_server_interface)>`_ – Ruby web server interface
* `PSGI <https://en.wikipedia.org/wiki/PSGI>`_ – Perl Web Server Gateway Interface
* `JSGI <https://en.wikipedia.org/wiki/JSGI>`_ – JavaScript web server gateway interface
