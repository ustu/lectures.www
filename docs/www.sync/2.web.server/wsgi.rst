WSGI (pep-333)
==============

.. seealso::

    * http://legacy.python.org/dev/peps/pep-0333/
    * https://ru.wikipedia.org/wiki/WSGI
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

По стандарту, WSGI-приложение должно удовлетворять следующим требованиям:

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

или WSGI-приложение в виде класса:

.. literalinclude:: /../sourcecode/wsgi/1.cgi.app.py
   :language: python
   :pyobject: AppClass
   :linenos:

Server/Gateway
--------------

Middleware
----------

.. image:: /_static/wsgi_as_onion.png
