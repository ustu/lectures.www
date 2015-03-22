FastCGI
=======

.. seealso::

   * `<http://dev-lab.info/2012/10/пример-простого-fastcgi-сервера-и-fastcgi-клиента/>`_
   * https://ru.wikipedia.org/wiki/FastCGI

.. image:: /_static/FastCGI_vs_CGI.svg
   :width: 800px

Что такое FastCGI
-----------------

В отличие от **CGI**, **FastCGI** использует постоянно запущенные процессы для обработки множества запросов.

**CGI-программы** взаимодействуют с сервером через **STIN** и **STDOUT** запущенного процесса.

**FastCGI-процессы** используют для связи с сервером **Unix Domain Sockets** или **TCP/IP** . Это даёт следующее преимущество над обычными CGI-программами: FastCGI-программы могут быть запущены не только на этом же сервере, но и где угодно в сети. Также возможна обработка запросов несколькими FastCGI-процессами, работающими параллельно. Можно использовать несколько FastCGI-серверов, распределяя нагрузку между ними с помощью **nginx** или **lighttpd**.

После установления соединения **FastCGI-процесса** с **web-сервером**, между ними начинается обмен данными, с использованием простого протокола, решающего две задачи: организация двунаправленного обмена в рамках одного соединения (для эмуляции **STDIN**, **STDOUT**, **STDERR**) и организация нескольких независимых FastCGI-сессий в рамках одного соединения.

Все передаваемые данные оборачиваются в **FastCGI-записи** — единицу данных протокола. **FastCGI-записи** служат для организации двунаправленного обмена и мультиплексирования нескольких сессий в рамках одного соединения.

**FastCGI-запись** состоит из заголовка фиксированной длины, следующего за ним содержимого и выравнивающих данных переменной длины. Каждая запись содержит 7 элементов.

Пример
------

.. seealso::

   * http://chriswu.me/blog/writing-hello-world-in-fcgi-with-c-plus-plus/

**Nginx**

.. note:: `Nginx` доступен по адресу http://localhost:8080/

.. literalinclude:: /../sourcecode/nginx/sites-enabled/default.nginx
   :language: nginx
   :linenos:

.. literalinclude:: /../sourcecode/nginx/includes/fcgi.nginx
   :language: nginx
   :linenos:

fastcgi_param

.. code-block:: nginx

      fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
      fastcgi_param  SERVER_SOFTWARE    nginx;
      fastcgi_param  QUERY_STRING       $query_string;
      fastcgi_param  REQUEST_METHOD     $request_method;
      fastcgi_param  CONTENT_TYPE       $content_type;
      fastcgi_param  CONTENT_LENGTH     $content_length;
      fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
      fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
      fastcgi_param  REQUEST_URI        $request_uri;
      fastcgi_param  DOCUMENT_URI       $document_uri;
      fastcgi_param  DOCUMENT_ROOT      $document_root;
      fastcgi_param  SERVER_PROTOCOL    $server_protocol;
      fastcgi_param  REMOTE_ADDR        $remote_addr;
      fastcgi_param  REMOTE_PORT        $remote_port;
      fastcgi_param  SERVER_ADDR        $server_addr;
      fastcgi_param  SERVER_PORT        $server_port;
      fastcgi_param  SERVER_NAME        $server_name;

**С++**

.. note::

   Компиляция ``g++ -o hello.fcgi hello.cpp -lfcgi++ -lfcgi``

.. literalinclude:: /../sourcecode/fcgi/hello.cpp
   :language: cpp
   :linenos:

Запуск fcgi сервера на 5000 порту

.. code-block:: bash

   spawn-fcgi -p 5000 -n hello.fcgi

.. note:: Пример доступен по адресу http://localhost:8080/fastcgi_hello
