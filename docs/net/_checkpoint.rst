.. _dz1:

Закрепление материала "Протокол HTTP"
=====================================

.. seealso::

   * telnet
   * curl
   * http://hurl.quickblox.com.
   * https://gist.github.com/


Задание 1
---------

.. note::

   Оформить в виде репозитария на github.

* Создать проект со следующей структурой:

::

   myproject/
   ├── about
   │   └── aboutme.html
   └── index.html

* В файле index.html написать 2 ссылки с прямым и абсолютным обращением
  к aboutme.html. В файле aboutme.html создать такие же ссылки на файл index.html.

Задание 2
---------

.. note::

   Оформить в виде заметок на сервисе `Gist` от `GitHub`.

Подключиться по telnet к http://wikipedia.org и отправить запрос:

::

   GET /wiki/страница HTTP/1.1
   Host: ru.wikipedia.org
   User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509
   Firefox/3.0b5
   Accept: text/html
   Connection: close
   (пустая строка)

Проанализировать ответ сервера. Описать работу HTTP протокола в данном случае.

Задание 3
---------

.. note::

   Оформить в виде заметок на сервисе `Gist` от `GitHub`.

Отправить запросы на http://httpbin.org, проанализировать ответ и код состояния.
Описать работу HTTP протокола в каждом запросе.

::

   GET /ip HTTP/1.1
   Host: httpbin.org
   Accept: */*

::

   GET /get?foo=bar&1=2&2/0&error=True HTTP/1.1
   Host: httpbin.org
   Accept: */*

::

   POST /post HTTP/1.1
   Host: httpbin.org
   Accept: */*
   Content-Length: 35
   Content-Type: application/x-www-form-urlencoded

   foo=bar&1=2&2%2F0=&error=True

::

   GET /cookies/set?country=Ru HTTP/1.1
   Host: httpbin.org
   Accept: */*

::

   GET /cookies HTTP/1.1
   Host: httpbin.org
   Accept: */*

::

   GET /redirect/4 HTTP/1.1
   Host: httpbin.org
   Accept: */*

Задание 4
---------

.. note::

   Оформить в виде заметок на сервисе `Gist` от `GitHub`.

* Создать HTML форму c action="http://httpbin.org/post" method="POST" и enctype="multipart/form-data"
* Добавить в форму поля firstname, lastname, group, message (textarea), myimg (file).
* Проверить результат отправки данных формы.

Проанализировать ответ. Описать работу HTTP протокола в данном случае.
