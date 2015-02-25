Веб-сервер
==========

.. seealso::

    * https://docs.python.org/3.5/howto/webservers.html
    * https://gist.github.com/willurd/5720255

Статика
-------

CGI
---

.. seealso::

    * https://ru.wikipedia.org/wiki/CGI

`Пример CGI скриптов на C++ <http://www.tutorialspoint.com/cplusplus/cpp_web_programming.htm>`_

Для работы нужно поставить библиотеку cgi:

::

    sudo apt-get install libcgicc5-dev

`Пример CGI скриптов на Python <http://www.tutorialspoint.com/python/python_cgi_programming.htm>`_

Запуск локального web сервера:

::

    python -m CGIHTTPServer
    или
    python cgiserver.py

WSGI (pep-333)
--------------

.. seealso::

    * https://github.com/iitwebdev/lectures#wsgi
    * http://hlabs.org/development/python/wsgi.html


