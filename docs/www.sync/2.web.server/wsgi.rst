WSGI (pep-333)
==============

.. seealso::

    * http://legacy.python.org/dev/peps/pep-0333/
    * https://ru.wikipedia.org/wiki/WSGI
    * http://docs.repoze.org/moonshining/pep333.html
    * http://pylonsbook.com/en/1.1/the-web-server-gateway-interface-wsgi.html
    * http://pylons-webframework.readthedocs.org/en/latest/concepts.html

.. image:: /_static/wsgi.svg
   :width: 800px

**WSGI** — стандарт взаимодействия между Python-программой, выполняющейся на стороне сервера, и самим веб-сервером, например, Apache.

**Идея:**

В Python существует большое количество различного рода веб-фреймворков, тулкитов и библиотек. Для каждого из них — собственный метод установки и настройки, они не умеют взаимодействовать между собой. Это может стать затруднением для тех, кто только начинает изучать Python, так как, например, выбор определённого фреймворка может ограничить выбор веб-сервера, и наоборот.

WSGI предоставляет простой и универсальный интерфейс между большинством веб-серверов и веб-приложениями или фреймворками.

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

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
   :language: python
   :pyobject: simple_app
   :linenos:

или то же самое в виде класса:

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
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

Пример WSGI-шлюза к CGI-серверу.

.. literalinclude:: /../sourcecode/wsgi/cgi_gateway.py
   :language: python
   :linenos:

Environment
~~~~~~~~~~~

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

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
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

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
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

.. image:: /_static/vector/wsgi_as_onion.svg
