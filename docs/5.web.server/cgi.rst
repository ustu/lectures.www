CGI
===

.. seealso::

    * https://ru.wikipedia.org/wiki/CGI
    * http://www.ietf.org/rfc/rfc3875.txt
    * `Лекции ОмГТУ, кафедра АСОИУ <http://www.4stud.info/web-programming/cgi.html>`_
    * http://webpython.codepoint.net/cgi_tutorial

**CGI** (от англ. Common Gateway Interface — «общий интерфейс шлюза») — стандарт интерфейса, используемого для связи внешней программы с веб-сервером. Программу, которая работает по такому интерфейсу совместно с веб-сервером, принято называть шлюзом, хотя многие предпочитают названия «скрипт» (сценарий) или «CGI-программа».

Поскольку гипертекст статичен по своей природе, веб-страница не может непосредственно взаимодействовать с пользователем. До появления `JavaScript`, не было иной возможности отреагировать на действия пользователя, кроме как передать введенные им данные на веб-сервер для дальнейшей обработки. В случае CGI эта обработка осуществляется с помощью внешних программ и скриптов, обращение к которым выполняется через стандартизованный (см. RFC 3875: CGI Version 1.1) интерфейс — общий шлюз.

Упрощенная модель, иллюстрирующая работу CGI:

.. image:: /_static/5.web.server/cgi.*
   :width: 550pt
   :align: center

Сам интерфейс разработан таким образом, чтобы можно было использовать любой язык программирования, который может работать со стандартными устройствами ввода-вывода. Такими возможностями обладают даже скрипты для встроенных командных интерпретаторов операционных систем, поэтому в простых случаях могут использоваться даже командные скрипты.

Как работает CGI?
-----------------

Обобщенный алгоритм работы через CGI можно представить в следующем виде:

#. Клиент запрашивает CGI-приложение по его URI.
#. Веб-сервер принимает запрос и устанавливает переменные окружения, через них приложению передаются данные и служебная информация.
#. Веб-сервер перенаправляет запросы через стандартный поток ввода (stdin) на вход вызываемой программы.
#. CGI-приложение выполняет все необходимые операции и формирует результаты в виде HTML.
#. Сформированный гипертекст возвращается веб-серверу через стандартный поток вывода (stdout). Сообщения об ошибках передаются через stderr.
#. Веб-сервер передает результаты запроса клиенту.

Области применения CGI
----------------------

Наиболее частая задача, для решения которой применяется CGI — создание интерактивных страниц, содержание которых зависит от действий пользователя. Типичными примерами таких веб-страниц являются форма регистрации на сайте или форма для отправки комментария. Другая область применения CGI, остающаяся за кулисами взаимодействия с пользователем, связана со сбором и обработкой информации о клиенте: установка и чтение «печенюшек»-cookies; получение данных о браузере и операционной системе; подсчет количества посещений веб-страницы; мониторинг веб-трафика и т.п.

Эти возможности обеспечиваются тем, что CGI-скрипт может быть подключен к базе данных или обращаться к файловой системе сервера. Таким образом CGI-скрипт может сохранять информацию в таблицах БД или файлах и получать ее оттуда по запросу, чего нельзя сделать средствами HTML.

.. warning::

  CGI — это не язык программирования! Это простой протокол, позволяющий веб-серверу передавать данные через stdin и читать их из stdout. Поэтому, в качестве CGI-обработчика может ипользоваться любая серверная программа, способная работать со стандарными потоками ввода-вывода.

Примеры
-------

Пример на Python:

.. code-block:: python

   #!/usr/bin/python
   print("""Content-Type: text/plain

   Hello, world!""")

В этом коде строка ``#!/usr/bin/python`` указывает полный путь к интерпретатору Python.


Пример на Си:

.. code-block:: cpp

   #include <stdio.h>
   int main(void) {
     printf("Content-Type: text/plain\n\n");
     printf("Hello, world!\n\n");
     return 0;
   }

Строка ``Content-type: text/html\n\n`` — http-заголовок, задающий тип содержимого (mime-type). Удвоенный символ разрыва строки (\\n\\n) — обязателен, он отделяет заголовки от тела сообщения.

Все скрипты, как правило, помещают в каталог cgi (или cgi-bin) сервера, но это необязательно: скрипт может располагаться где угодно, но при этом большинство веб-серверов требуют специальной настройки. В веб-сервере Apache, например, такая настройка может производиться при помощи общего файла настроек httpd.conf или с помощью файла .htaccess в том каталоге, где содержится этот скрипт. Также скрипты должны иметь права на исполнение (``chmod +x hello.py``).

Переменные окружения
--------------------

Все CGI-приложения имеют доступ к переменным окружения, устанавливаемым веб-сервером. Эти переменные играют важную роль при написании CGI-программ. В таблице перечислены некоторые из переменных, доступных CGI.

+-----------------+-------------------------------------------------------------------------------------------------------------+
| Переменная      | Описание                                                                                                    |
+=================+=============================================================================================================+
| CONTENT_TYPE    | Тип данных, передаваемых на сервер. Используется, когда клиент отправляет данные, например, загружает файл. |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| CONTENT_LENGTH  | Размер содержимого запроса. Эта переменная определена для POST-запросов.                                    |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| HTTP_COOKIE     | Возвращает набор «куков» в виде пар «ключ значение».                                                        |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| HTTP_USER_AGENT | Информация об агенте пользователя (браузере).                                                               |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| PATH_INFO       | Путь к каталогу CGI.                                                                                        |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| QUERY_STRING    | Строка запроса (URL-encoded), передаваемая методом GET.                                                     |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| REMOTE_ADDR     | IP-адрес клиента, выполняющего запрос.                                                                      |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| REMOTE_HOST     | Полное имя (FQDN) клиента. (Если доступно)                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| REQUEST_METHOD  | Метод, которым выполняется запрос. Чаще всего GET или POST.                                                 |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| SCRIPT_FILENAME | Полный путь к запрашиваемому скрипту (в файловой системе сервера).                                          |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| SCRIPT_NAME     | Имя скрипта.                                                                                                |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| SERVER_NAME     | Имя сервера.                                                                                                |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| SERVER_ADDR     | IP-адрес сервера.                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------+
| SERVER_SOFTWARE | Информация о серверном ПО.                                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------+

Пример вывода переменных окружения CGI-скрипта:

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/2.environment.py
   :language: python
   :linenos:

.. image:: /_static/5.web.server/cgi_env.png
   :width: 500pt
   :align: center

Преимущества CGI
----------------

* Процесс CGI скрипта не зависит от Веб-сервера и в случае падения ни как не отразится на работе последнего
* Может быть написан на любом языке программирования
* Поддерживается большинством Веб-серверов

Недостатки CGI
--------------

Самым большим недостатком этой технологии являются повышенные требования к производительности веб-сервера. Дело в том, что каждое обращение к CGI-приложению вызывает порождение нового процесса, со всеми вытекающими отсюда накладными расходами. Если же приложение написано с ошибками, то возможна ситуация, когда оно, например, зациклится. Браузер прервет соединение по истечении тайм-аута, но на серверной стороне процесс будет продолжаться, пока администратор не снимет его принудительно.

Альтернативы
------------

* FastCGI - дальнейшее развитие технологии CGI. Поддерживается
  многими Веб-серверами, например Nginx.
* Веб-сервера в которые уже встроена поддержка дополнительных,
  стандартов и протоколов, таких как WSGI (Gunicorn, waitress, uwsgi)
* Веб-сервер функционал которого расширяется через модули, например
  Apache (mod_wsgi, mod_php, mod_fastcgi)

Практика
--------

.. seealso::

   * https://docs.python.org/2/library/cgihttpserver.html
   * https://docs.python.org/3/library/http.server.html

Для запуска CGI сервера, необходимо перейти в директорию ``sourcecode``
и выполнить команду:

.. code-block:: bash

   python -m CGIHTTPServer 8000

или

.. code-block:: bash

   python3 -m http.server --cgi 8000

или ``cgiserver.py``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgiserver.py
   :language: python
   :linenos:

.. code-block:: bash

   python cgiserver.py

Теперь CGI-скрипты доступны на ``8000`` порту,
например по адресу `<http://localhost:8000/cgi-bin/1.hello.py>`_

* `Пример CGI скриптов на Python <http://www.tutorialspoint.com/python/python_cgi_programming.htm>`_
* `Пример CGI скриптов на C++ <http://www.tutorialspoint.com/cplusplus/cpp_web_programming.htm>`_

.. note::

   Для компиляции кода на C++ необходимо установить библиотеку cgi:

   .. code-block:: bash

       sudo apt-get install libcgicc5-dev

   Пример компиляции:

   .. code-block:: bash

       g++ -o 3.get.post.cgi 3.get.post.cpp -lcgicc

Hello World!
~~~~~~~~~~~~

.. note::

   * http://localhost:8000/cgi-bin/1.hello.cgi
   * http://localhost:8000/cgi-bin/1.hello.go.cgi
   * http://localhost:8000/cgi-bin/1.hello.py
   * http://localhost:8000/cgi-bin/1.hello.rb

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/1.hello.py
   :language: python
   :linenos:

Ruby

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/1.hello.rb
   :language: ruby
   :linenos:

C++

Для компиляции: ``make 1_hello``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/1.hello.cpp
   :language: cpp
   :linenos:

Go

Для компиляции: ``make 1_hello_go``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/1.hello.go
   :language: go
   :linenos:

Вывод пременных окружения
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   * http://localhost:8000/cgi-bin/2.environment.cgi
   * http://localhost:8000/cgi-bin/2.environment.py
   * http://localhost:8000/cgi-bin/2.environment.rb

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/2.environment.py
   :language: python
   :linenos:

Ruby

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/2.environment.rb
   :language: ruby
   :linenos:

C++

Для компиляции: ``make 2_environment``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/2.environment.cpp
   :language: cpp
   :linenos:

GET и POST запросы
~~~~~~~~~~~~~~~~~~

.. note::

   * http://localhost:8000/cgi-bin/3.get.post.cgi?first_name=Lev&last_name=Tolstoy
   * http://localhost:8000/cgi-bin/3.get.post.py?first_name=Lev&last_name=Tolstoy
   * http://localhost:8000/cgi-bin/3.get.post.rb?first_name=Lev&last_name=Tolstoy

* **GET** (action="http://localhost:8000/cgi-bin/3.get.post.cgi" method="get")

   .. todo:: Add LaTeX support

   .. raw:: html

        <form action="http://localhost:8000/cgi-bin/3.get.post.cgi"
              method="get" target="_blank">
            First Name: <input type="text" name="first_name"><br />
            Last Name: <input type="text" name="last_name" />

            <input type="submit" value="Submit" />
        </form>

* **POST** (action="http://localhost:8000/cgi-bin/3.get.post.cgi" method="post")

   .. todo:: Add LaTeX support

   .. raw:: html

        <form action="http://localhost:8000/cgi-bin/3.get.post.cgi"
              method="post" target="_blank">
            First Name: <input type="text" name="first_name"><br />
            Last Name: <input type="text" name="last_name" />

            <input type="submit" value="Submit" />
        </form>

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/3.get.post.py
   :language: python
   :linenos:

Ruby

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/3.get.post.rb
   :language: ruby
   :linenos:

C++

Для компиляции: ``make 3_get_post``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/3.get.post.cpp
   :language: cpp
   :linenos:

Checkbox
~~~~~~~~

.. todo:: Add LaTeX support

.. raw:: html

   <form action="http://localhost:8000/cgi-bin/4.checkbox.cgi" method="POST" target="_blank">
      <input type="checkbox" name="maths" value="on" /> Maths
      <input type="checkbox" name="physics" value="on" /> Physics
      <input type="submit" value="Select Subject" />
   </form>

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/4.checkbox.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 4_checkbox``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/4.checkbox.cpp
   :language: cpp
   :linenos:

Radio
~~~~~

.. todo:: Add LaTeX support

.. raw:: html

   <form action="http://localhost:8000/cgi-bin/5.radio.cgi" method="POST" target="_blank">
      <input type="radio" name="subject" value="maths"
                                          checked="checked"/> Maths
      <input type="radio" name="subject" value="physics" /> Physics
      <input type="submit" value="Select Subject" />
   </form>

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/5.radio.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 5_radio``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/5.radio.cpp
   :language: cpp
   :linenos:

TextArea
~~~~~~~~

.. todo:: Add LaTeX support

.. raw:: html

   <form action="http://localhost:8000/cgi-bin/6.textarea.cgi" method="POST" target="_blank">
      <textarea name="textcontent" cols="40" rows="4">
      Type your text here...
      </textarea>
      <input type="submit" value="Submit" />
   </form>

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/6.textarea.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 6_textarea``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/6.textarea.cpp
   :language: cpp
   :linenos:

Drop Down Box
~~~~~~~~~~~~~

.. todo:: Add LaTeX support

.. raw:: html

   <form action="http://localhost:8000/cgi-bin/7.dropdown.cgi" method="POST" target="_blank">
      <select name="dropdown">
      <option value="Maths" selected>Maths</option>
      <option value="Physics">Physics</option>
      </select>
      <input type="submit" value="Submit"/>
   </form>

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/7.dropdown.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 7_dropdown``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/7.dropdown.cpp
   :language: cpp
   :linenos:

Печать Cookie
~~~~~~~~~~~~~

.. note::

   * http://localhost:8000/cgi-bin/8.getcookie.cgi
   * http://localhost:8000/cgi-bin/8.getcookie.py

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/8.getcookie.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 8_getcookie``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/8.getcookie.cpp
   :language: cpp
   :linenos:

Установка Cookie
~~~~~~~~~~~~~~~~

.. note::

   * http://localhost:8000/cgi-bin/9.setcookie.cgi
   * http://localhost:8000/cgi-bin/9.setcookie.py

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/9.setcookie.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 9_setcookie``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/9.setcookie.cpp
   :language: cpp
   :linenos:

Загрузка файлов
~~~~~~~~~~~~~~~

.. todo:: Add LaTeX support

.. raw:: html

   <form action="http://localhost:8000/cgi-bin/10.fileupload.cgi" method="POST"
         target="_blank" enctype="multipart/form-data">
      <p>File: <input type="file" name="filename" /></p>
      <p><input type="submit" value="Upload" /></p>
   </form>

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/10.fileupload.py
   :language: python
   :linenos:

C++

Для компиляции: ``make 10_fileupload``

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/10.fileupload.cpp
   :language: cpp
   :linenos:

Отладка
~~~~~~~

.. seealso::

   * http://pymotw.com/2/cgitb/
   * https://docs.python.org/2/library/cgitb.html

.. note::

   * http://localhost:8000/cgi-bin/test.py

Python

.. literalinclude:: /../sourcecode/5.www.sync/1.web.server/cgi-bin/test.py
   :language: python
   :linenos:
   :emphasize-lines: 24

.. figure:: /_static/5.web.server/cgitb.png
   :align: center
   :Width: 400pt
