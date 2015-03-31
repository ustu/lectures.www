Встроенный сервер
=================

.. seealso::

   * http://golang.org/pkg/net/http/

.. figure:: /_static/5.web.server/reverse_proxy.*
   :width: 500pt
   :align: center

В некоторых языках, например `Go`, уже существует встроенный Веб-сервер, который можно использовать в вашем приложении.

Go FastCGI
----------

.. seealso::

   * http://golang.org/pkg/net/http/fcgi/

В этом случае не нужно запускать отдельно fcgi сервер,
например ``spawn-fcgi``.

.. note::

   Компиляция ``go build -o hello.go.fcgi hello.go``

.. literalinclude:: /../sourcecode/5.web.server/fcgi/hello.go
   :language: go
   :linenos:

Запуск go fcgi сервера на 5000 порту (Без компиляции).

.. code-block:: bash

   go run hello.go

Или скомпилированный файл.

.. code-block:: bash

   ./hello.go.fcgi

Настройка Nginx

.. literalinclude:: /../sourcecode/nginx/includes/fcgi.nginx
   :language: nginx
   :linenos:

::

   Client Request ----> Nginx (Reverse-Proxy) ----> App. FastCGI Server I. 127.0.0.1:5000

либо с балансировкой на несколько серверов:

.. code-block:: nginx
   :linenos:

   # Nginx
   upstream myapp1 {
       server 127.0.0.1:5000;
       server 127.0.0.1:5001;
       server 127.0.0.1:5002;
   }

   server {
       listen 80;

       location /some/path {
           fastcgi_pass http://myapp1;
       }
   }

::

   Client Request ----> Nginx (Reverse-Proxy)
                           |
                          /|\
                         | | `-> App. FastCGI Server I.   127.0.0.1:5000
                         |  `--> App. FastCGI Server II.  127.0.0.1:5001
                          `----> App. FastCGI Server III. 127.0.0.1:5002

Go HTTP
-------

Запуск напрямую без CGI и FastCGI.

.. note::

   Компиляция ``go build -o hello.go.http hello.go``

.. literalinclude:: /../sourcecode/5.web.server/httpserver/hello.go
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
   :linenos:

   # Nginx

   location /some/path/ {
       proxy_pass http://127.0.0.1:8000;
   }

::

   Client Request ----> Nginx (Reverse-Proxy) ----> App. HTTP Server I. 127.0.0.1:8000

либо с балансировкой на несколько серверов:

.. code-block:: nginx
   :linenos:

   # Nginx
   upstream myapp1 {
       server 127.0.0.1:8000;
       server 127.0.0.1:8001;
       server 127.0.0.1:8002;
   }

   server {
       listen 80;

       location /some/path {
           proxy_pass http://myapp1;
       }
   }


::

   Client Request ----> Nginx (Reverse-Proxy)
                           |
                          /|\
                         | | `-> App. HTTP Server I.   127.0.0.1:8000
                         |  `--> App. HTTP Server II.  127.0.0.1:8001
                          `----> App. HTTP Server III. 127.0.0.1:8002
