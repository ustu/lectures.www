.. _dz3:

Закрепление материала "WSGI"
============================

Цель работы
-----------

Получить практические навыки по работе со спецификацией ``WSGI``.

Замечания к выполнению
----------------------

Пример `WSGI middleware` которое вставляет в тело `HTML` страниц строки
следующим образом:

.. code-block:: html
   :emphasize-lines: 6, 10

   <html>
   <head>
      ...
   </head>
   <body>
      <div class='top'>Middleware TOP</div>

      ...

      <div class='botton'>Middleware BOTTOM</div>
   </body>
   </html>

Пример реализации:

.. code-block:: python

    from paste.httpserver import serve

    TOP = "<div class='top'>Middleware TOP</div>"
    BOTTOM = "<div class='botton'>Middleware BOTTOM</div>"


    class WsgiTopBottomMiddleware(object):
        '''
        WSGI Midlewere которое добавляет TOP, BOTTOM в HTML документ
        '''

        def __init__(self, app):
            self.app = app

        def __call__(self, environ, start_response):
            response = self.app(environ, start_response).decode()  # bytes to str
            if response.find('<body>') > -1:
                header, body = response.split('<body>')
                data, htmlend = body.split('</body>')
                data = '<body>' + TOP + data + BOTTOM+'</body>'
                yield (header + data + htmlend).encode()  # str to bytes
            else:
                yield (TOP + response + BOTTOM).encode()  # str to bytes


    def app(environ, start_response):
        '''
        WSGI приложение которое отдает HTML документ
        '''
        response_code = '200 OK'
        response_type = ('Content-Type', 'text/HTML')
        start_response(response_code, [response_type])
        return '''
    <!DOCTYPE html>
    <html>
       <head>
          <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
          <title>HTML Document</title>
       </head>
       <body>
          <p>
             <b>
                Этот текст будет полужирным,
                <i>а этот — ещё и курсивным</i>
             </b>
          </p>
       </body>
    </html>
        '''.encode()  # str to bytes


    # Оборачиваем WSGI приложение в middleware
    app = WsgiTopBottomMiddleware(app)

    # Запускаем сервер
    serve(app, host='localhost', port=8000)

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

Задание 2, 3, 4
^^^^^^^^^^^^^^^

Делать не надо.

Содержание отчета
-----------------

На каждое задание создать отчет, который должен быть оформлен в виде
репозитария на :l:`GitHub`. В отчете должно быть: исходный код программы,
описание последовательности действий, результат выполнения заданий и выводы по
работе.
