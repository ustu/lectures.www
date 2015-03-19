Paste
=====

.. seealso::

   * https://ru.wikipedia.org/wiki/Python_Paste

.. note::

   Исходный код данного примера лежит в директориии ``sourcecode/wsgi/blog/0.paster``

Python Paste, или просто Paste — набор программ для веб-разработки с использованием языка Python.
Включает в себя множество различных `middleware`, `WSGI-сервер` и другое.

Например, в нем есть готовая поддержка самых `разных способов аутентификации <http://pythonpaste.org/developer-features.html>`_ (Basic, Digest, form, signed cookie, auth_tkt), поддержка корректной и удобной генерации ответов и `заголовков <http://pythonpaste.org/modules/httpheaders.html>`_ (к примеру редиректы, Cache-control, Expires, `gzipper <http://pythonpaste.org/modules/gzipper.html>`_ и прочие). Различные базовые средства комбинации приложений (`URLMap <http://pythonpaste.org/modules/urlmap.html>`_, `Cascade <http://pythonpaste.org/modules/cascade.html>`_, `Recursive <http://pythonpaste.org/modules/recursive.html>`_), `статических данных <http://pythonpaste.org/modules/urlparser.html>`_ (с учетом Etag, If-Modified итп).

Некоторые возможности ``paste`` мы рассмотрели в разделе :ref:`wsgi`.

HTTP server
-----------

.. seealso::

   * http://pythonpaste.org/modules/httpserver.html#module-paste.httpserver

Создадим простое `WSGI-приложение` и запустим его при помощи `WSGI-HTTP-сервера` ``paste.httpserver``:

.. image:: /_static/wsgi/blog/1.0_step_dia.svg
   :width: 600px

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/0_step.py
   :language: python
   :linenos:

Теперь приложение доступно по адресу ``http://localhost:8000/``.

.. image:: /_static/wsgi/blog/1.0_step.png

.. note:: Стоит отметить что приложение будет доступно по любому пути этого адреса, например:

   * http://localhost:8000/
   * http://localhost:8000/foo
   * http://localhost:8000/foo/bar/
   * http://localhost:8000/foo/bar/baz
   * http://localhost:8000/no_good

URL диспетчеризация
-------------------

Для разделения путей напишем `WSGI-middleware` ``URLDispatch``.

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/middlewares/urldispatch.py
   :language: python
   :pyobject: URLDispatch
   :linenos:

Добавим настройки в наше приложение:

.. image:: /_static/wsgi/blog/1.1_step_dia.svg
   :width: 750px

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/1_step.py
   :language: python
   :emphasize-lines: 12, 20-24
   :linenos:

Теперь приложение ``blog`` доступно только по адресу http://localhost:8000/,
если мы попробуем зайти по другому пути, то получим `404 ошибку`.

.. image:: /_static/wsgi/blog/1.1_step.png

`Блог` будет состоять из следующих страниц:

.. list-table:: Страницы блога
   :header-rows: 1

   * - Название
     - URL
     - Описание
   * - Главная
     - \/
     - Показывает все записи в блоге, отсортированные по дате
   * - (**CREATE**)
        Добавление
     - /article/add
     - Форма добавления новой статьи
   * - (**READ**)
        Просмотр
     - /article/{id}
     - Показывает конкретную статью соответствующую {id}
   * - (**UPDATE**)
        Редактирование
     - /article/{id}/edit
     - Редактирование статьи по {id}
   * - (**DELETE**)
        Удаление
     - /article/{id}/delete
     - Удаление статьи по {id}

Добавим `WSGI-приложения` которые будут реализовывать `CRUD` и укажем им соответствующие адреса.

.. image:: /_static/wsgi/blog/1.2_step_dia.svg
   :width: 750px

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/2_step.py
   :language: python
   :emphasize-lines: 22-54
   :linenos:

.. note::

   Обратите внимание, что адреса доступны по следующим ссылкам:

   * http://localhost:8000/article/add
   * `<http://localhost:8000/article/{id}>`_
   * `<http://localhost:8000/article/{id}/edit>`_
   * `<http://localhost:8000/article/{id}/delete>`_

   Если вместо ``{id}`` подставить цифру, то вернется ``404 ошибка``.

Перепишем `WSGI-middleware` ``URLDispatch`` так, что бы он понимал регулярные выражения.

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/middlewares/urldispatch.py
   :language: python
   :pyobject: RegexDispatch
   :emphasize-lines: 11-14
   :linenos:

.. image:: /_static/wsgi/blog/1.3_step_dia.svg
   :width: 780px

И поменяем настройки:

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/3_step.py
   :language: python
   :emphasize-lines: 12, 60-62
   :linenos:

.. note::

   Теперь можно переходить по URL'ам с цифрами заместо {id}, например:

   * http://localhost:8000/article/1
   * http://localhost:8000/article/13/
   * http://localhost:8000/article/100500
   * http://localhost:8000/article/100500/edit
   * http://localhost:8000/article/100500/delete

Данные
------

Добавим базовые данные и функционал для их чтения, удаления.

.. literalinclude:: /../sourcecode/wsgi/blog/0.paster/4_step.py
   :language: python
   :emphasize-lines: 14-29, 39-47, 55-58, 72-80, 93-97
   :linenos:

.. image:: /_static/wsgi/blog/1.4_step.png
.. image:: /_static/wsgi/blog/1.4_step2.png
