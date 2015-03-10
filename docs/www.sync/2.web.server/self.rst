Встроенный сервер
=================

.. seealso::

   * http://golang.org/pkg/net/http/

В некоторых языках, например `Go`, уже существует встроенный Веб-сервер, который можно использовать в вашем приложении.

Go FastCGI
----------

.. seealso::

   * http://golang.org/pkg/net/http/fcgi/

В этом случае не нужно запускать отдельно fcgi сервер,
например ``spawn-fcgi``.

.. note::

   Компиляция ``go build -o hello.go.fcgi hello.go``

.. literalinclude:: /../sourcecode/fcgi/hello.go
   :language: go
   :linenos:

Запуск go fcgi сервера на 5000 порту (Без компиляции).

.. code-block:: bash

   go run hello.go

Или скомпилированный файл.

.. code-block:: bash

   ./hello.go.fcgi

Go HTTP
-------

Запуск напрямую без CGI и FastCGI.

.. note::

   Компиляция ``go build -o hello.go.http hello.go``

.. literalinclude:: /../sourcecode/httpserver/hello.go
   :language: go
   :linenos:

Запуск go http сервера на 8000 порту (Без компиляции).

.. code-block:: bash

   go run hello.go

Или скомпилированный файл.

.. code-block:: bash

   ./hello.go.http

На такой сервер можно зайти напрямую по адресу http://localhost:8000/,
либо настроить обратный прокси сервер:

.. code-block:: nginx

   # Nginx

   location /some/path/ {
       proxy_pass http://127.0.0.1:8000;
   }
