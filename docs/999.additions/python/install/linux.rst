Установка Python в ОС Linux
===========================

Сборка из исходников (UNIX)
---------------------------

Скачиваем
~~~~~~~~~

.. note::

   В `оф. документации
   <https://docs.python.org/devguide/setup.html#getting-the-source-code>`_
   предлагают скачать ртутью с фирменного сайта:

   .. code-block:: bash

      $ hg clone https://hg.python.org/cpython
      $ hg update 3.5

Скачиваем с гитхаба :github:`python/cpython`:

.. code-block:: bash

   git clone https://github.com/python/cpython.git

Выбираем ветку ``3.5`` (`cpython` версии 3.5):

.. code-block:: bash

   git checkout 3.5

Собираем
~~~~~~~~

Укажем локальную директорию для сборки:

.. code-block:: bash

   ./configure --prefix=$HOME/Projects/bin/python3.5

Скомпилируем:

.. code-block:: bash

   make && make install

Теперь можно запускать:

.. code-block:: pycon

  $ $HOME/Projects/bin/python3.5/bin/python3
  Python 3.5.0+ (default, Oct 10 2015, 13:35:25)
  [GCC 4.9.2] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

.. code-block:: pycon

  >>> {*range(4), 4, *(5, 6, 7)}
  {0, 1, 2, 3, 4, 5, 6, 7}
  >>> import asyncio
  >>> async def foo(bar): await asyncio.sleep(42)

virtualenv
~~~~~~~~~~

Укажем виртуальному окружению где находится интерпретатор `cpython`:

.. code-block:: bash

   $ mkvirtualenv --python=$HOME/Projects/bin/python3.5/bin/python3 python35_env
   Running virtualenv with interpreter /home/uralbash/Projects/bin/python3.5/bin/python3
   Using base prefix '/home/uralbash/Projects/bin/python3.5'
   New python executable in aiohttp/bin/python3
   Also creating executable in aiohttp/bin/python
   Installing setuptools, pip, wheel...done.

Linux
-----

Установка интерпретатора CPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ sudo apt-get install python

Пакетный менеджер pip
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ sudo apt-get install python-setuptools python-dev build-essential
   $ sudo easy_install pip

Виртуальное окружение Virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ sudo pip install virtualenv virtualenvwrapper
   $ source /usr/local/bin/virtualenvwrapper.sh

Компиляция пакетов
~~~~~~~~~~~~~~~~~~

Некоторые Python пакеты написаны с использование языка программирования Си,
поэтому при установке они требуют компиляции. Если у вас не установлен
компилятор, пакет не будет установлен.

.. code-block:: bash

   $ sudo apt-get install gcc python-dev

Установка git
~~~~~~~~~~~~~

.. code-block:: bash

   $ sudo apt-get intall git

Пример
~~~~~~

Склонируем репозитарий админки https://github.com/sacrud/pyramid_sacrud.git в
директорию ``/home/user/Projects``.

.. code-block:: bash

   $ cd /home/user/Projects/
   $ git clone https://github.com/sacrud/pyramid_sacrud.git

Установим :l:`pyramid_sacrud` из исходных кодов.

.. code-block:: bash

   $ cd /home/user/Projects/pyramid_sacrud
   $ mkvirtualenv pyramid_sacrud
   $ python setup.py develop

Далее установим пример ``pyramid_sacrud/example``

.. code-block:: bash

   $ cd /home/user/Projects/pyramid_sacrud/example
   $ workon pyramid_sacrud
   $ python setup.py develop

Пакеты устанавливаются в виртуальное окружение с названием ``pyramid_sacrud``.

Теперь можно запустить пример:

.. code-block:: bash

   $ cd /home/user/Projects/pyramid_sacrud/example
   $ workon pyramid_sacrud
   $ pserve development.ini

Заходим на http://localhost:6543/admin/

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud_linux.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud2_linux.png
   :align: center


