.. _dz3:

Закрепление материала "WSGI"
============================

Цель работы
-----------

Получить практические навыки по работе со спецификацией ``WSGI``.

Задания
-------

Описание заданий находится в разделе :ref:`dz1`.

Задание 1
^^^^^^^^^

* Написать `WSGI` приложение который отдает статикой файлы `index.html` и
  `about.html`.

* Написать `WSGI middleware` которое будет вставлять в `HTML` документ
  `JavaScript` и `CSS` файлы из списка типа:
  
  .. code-block:: python

    includes = [
        'app.js',
        'react.js',
        'leaflet.js',
        'D3.js',
        'moment.js',
        'math.js',
        'main.css',
        'bootstrap.css',
        'normalize.css',
    ]
  
  Следующим образом:

  .. code-block:: html
     :emphasize-lines: 6-8, 14-19

     <html>
     <head>

        ...

        <link rel="stylesheet" href="/_static/main.css"/>
        <link rel="stylesheet" href="/_static/bootstrap.css"/>
        <link rel="stylesheet" href="/_static/normalize.css"/>
     </head>
     <body>

        ...

        <script src="/_static/app.js"></script>
        <script src="/_static/react.js"></script>
        <script src="/_static/leaflet.js"></script>
        <script src="/_static/D3.js"></script>
        <script src="/_static/moment.js"></script>
        <script src="/_static/math.js"></script>
     </body>
     </html>

.. * Написать `WSGI middleware` которое будет вставлять в тело `HTML` страниц строки следующим образом:
..
..   .. code-block:: html
..      :emphasize-lines: 6, 10
..
..      <html>
..      <head>
..         ...
..      </head>
..      <body>
..         <div class='top'>Middleware TOP</div>
..
..         ...
..
..         <div class='botton'>Middleware BOTTOM</div>
..      </body>
..      </html>

Задание 2, 3, 4
^^^^^^^^^^^^^^^

Делать не надо.

Содержание отчета
-----------------

На каждое задание создать отчет, который должен быть оформлен в виде
репозитария на :l:`GitHub`. В отчете должно быть: исходный код программы,
описание последовательности действий, результат выполнения заданий и выводы по
работе.
