Jinja2
======

.. seealso::

   * http://jinja.pocoo.org/
   * https://ru.wikipedia.org/wiki/Jinja

**Jinja2** — самый популярный шаблонизатор в языке программирования Python.
Автор `Armin Ronacher` из команды `<http://www.pocoo.org/>`_, не раз
приезжал на конференции в `Екатеринбург` с докладами о своих продуктах.

Синтаксис `Jinja2` сильно похож на `Django`-шаблонизатор, но при этом дает
возможность использовать чистые `Python` выражения и поддерживает гибкую
систему расширений.

Hello {{ name }}!
-----------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/0.hello.py
   :language: python
   :linenos:

Hello Вася!

{# Комментарии #}
-----------------

.. todo:: добавить описание

.. code-block:: jinja

   {# Это кусок кода который стал временно не ненужен, но удалять жалко
       {% for user in users %}
           ...
       {% endfor %}
   #}

{{ Выражения }}
---------------

.. seealso::

   * `<https://ru.wikipedia.org/wiki/Выражение_(информатика)>`_

.. todo:: добавить описание

{% Операторы %}
---------------

.. seealso::

   * `<https://ru.wikipedia.org/wiki/Оператор_(программирование)>`_

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/1.statements/0.hello.py
   :language: python
   :linenos:

Hello Вася! Hello Вася! Hello Вася! Hello Вася! Hello Вася!

Модули
------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/1.statements/1.set.py
   :language: python
   :linenos:

| foo
| фуу
| föö

Макросы
-------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/2.module.py
   :language: python
   :linenos:

| 23
| 42

Чтение из файла
---------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/foopkg/templates/0.hello.html
   :language: jinja
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/0.file.py
   :language: python
   :linenos:
   :name: 0.file.py
   :caption: ``jinja2/3.loader/0.file.py`` - чтение шаблона из файла

.. code-block:: html
   :name: hello_petya
   :caption: Результат рендинга шаблона ``jinja2/3.loader/foopkg/templates/0.hello.html``

   <!DOCTYPE html>
   <html>
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
     </head>
     <body>

         Hello Петя!

         Hello Петя!

         Hello Петя!

         Hello Петя!

         Hello Петя!

     </body>
   </html>

Окружение (Environment)
-----------------------

.. seealso::

   * http://jinja.pocoo.org/docs/dev/api/#loaders
   * http://jinja.pocoo.org/docs/dev/api/#jinja2.Environment

.. todo:: добавить описание

Настройки
~~~~~~~~~

.. todo:: добавить описание

Загрузчики шаблонов (Loaders)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FileSystemLoader
""""""""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/1.env.file.py
   :language: python
   :emphasize-lines: 4
   :linenos:

:ref:`hello_petya`

PackageLoader
"""""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/2.env.pkg.py
   :language: python
   :emphasize-lines: 4
   :linenos:

:ref:`hello_petya`

DictLoader
""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/3.env.dict.py
   :language: python
   :emphasize-lines: 17
   :linenos:

:ref:`hello_petya`

FunctionLoader
""""""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/4.env.func.py
   :language: python
   :emphasize-lines: 22
   :linenos:

:ref:`hello_petya`

PrefixLoader
""""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/5.env.prefix.py
   :language: python
   :emphasize-lines: 22
   :linenos:

:ref:`hello_petya`

ChoiceLoader
""""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/6.env.choice.py
   :language: python
   :emphasize-lines: 22
   :linenos:

:ref:`hello_petya`

ModuleLoader
""""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/7.env.compile.py
   :language: python
   :emphasize-lines: 10
   :linenos:

:ref:`hello_petya`

BaseLoader
""""""""""

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/3.loader/8.env.base.py
   :language: python
   :emphasize-lines: 7-19
   :linenos:

:ref:`hello_petya`

Шаблон конфига Nginx
--------------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/4.nginx/nginx_proxy_conf.tpl
   :language: jinja
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/4.nginx/do_proxy.py
   :language: python
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/4.nginx/proxy.nginx.conf
   :language: nginx
   :linenos:

{% extends "Наследование" %}
----------------------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/5.inherit/base.html
   :language: html+jinja
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/5.inherit/index.html
   :language: html+jinja
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/5.inherit/app.py
   :language: python
   :linenos:

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en">
   <head>


       <link rel="stylesheet" href="style.css" />
       <title>Index - My Webpage</title>
       <meta charset='utf-8'>

       <style type="text/css">
           .important { color: #336699; }
       </style>

   </head>
   <body>
       <div id="content">
       <h1>Index</h1>
       <p class="important">
         Welcome Петя to my awesome homepage.
       </p>
   </div>
       <div id="footer">

           &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.

       </div>
   </body>
   </html>

.. figure:: /_static/6.www.sync/3.templates/inherit.png

Блог
----

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/6.blog/templates/base.html
   :language: html+jinja
   :linenos:
   :caption: templates/base.html - базовый шаблон.

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/6.blog/templates/index.html
   :language: html+jinja
   :linenos:
   :caption: Главня страница templates/index.html наследуется от templates/base.html

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/6.blog/templates/create.html
   :language: html+jinja
   :linenos:
   :caption: templates/create.html наследуется от базового шаблона.

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/6.blog/templates/read.html
   :language: html+jinja
   :linenos:
   :caption: templates/read.html наслудуется от базового шаблона.

.. literalinclude:: /../examples/wsgi/3.templates/jinja2/6.blog/views.py
   :language: python
   :linenos:
   :emphasize-lines: 5, 31, 55, 69, 87
   :caption: views.py - окружение Jinja2.
