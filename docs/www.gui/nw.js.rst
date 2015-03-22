node.js + WebKit
================

.. seealso::

   * https://github.com/nwjs/nw.js

Установка:

.. code-block: bash

   npm install nw

Hello World
-----------

.. note:: исходный код примера:

   https://github.com/ustu/lectures.www/tree/master/sourcecode/gui/js/hello

Структура файлов:

.. code-block:: bash

   .
   ├── index.html
   └── package.json

   0 directories, 2 files

| index.html

.. literalinclude:: /../sourcecode/gui/js/hello/index.html
   :language: html
   :linenos:

| package.json

.. literalinclude:: /../sourcecode/gui/js/hello/package.json
   :language: json
   :linenos:

Запуск:

.. code-block: bash

   nw

.. image:: /_static/gui/hello_nw.js.png
