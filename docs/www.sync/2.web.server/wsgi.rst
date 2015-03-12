WSGI (pep-333)
==============

.. seealso::

    * http://legacy.python.org/dev/peps/pep-0333/
    * http://pylonsbook.com/en/1.1/the-web-server-gateway-interface-wsgi.html#testing-the-gzip-middleware
    * http://pylons-webframework.readthedocs.org/en/latest/concepts.html
    * http://lucumr.pocoo.org/2007/5/21/getting-staRTED-with-wsgi/

.. image:: /_static/wsgi.svg
   :width: 800px

**WSGI** — стандарт взаимодействия между Python-программой, выполняющейся на стороне сервера, и самим веб-сервером, например, Apache.

**Идея:**

В Python существует большое количество различного рода веб-фреймворков, тулкитов и библиотек. Для каждого из них — собственный метод установки и настройки, они не умеют взаимодействовать между собой. Это может стать затруднением для тех, кто только начинает изучать Python, так как, например, выбор определённого фреймворка может ограничить выбор веб-сервера, и наоборот.

WSGI предоставляет простой и универсальный интерфейс между большинством веб-серверов и веб-приложениями или фреймворками.

Приложение
----------

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
   :language: python
   :pyobject: AppClass
   :linenos:

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
   :language: python
   :pyobject: simple_app
   :linenos:

Сервер
------

Middleware
----------

.. image:: /_static/wsgi_as_onion.png
