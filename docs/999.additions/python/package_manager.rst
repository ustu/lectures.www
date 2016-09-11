Управление пакетами в Python
============================

Установка pip в Ubuntu
----------------------

.. seealso::

   * https://ru.wikipedia.org/wiki/Advanced_Packaging_Tool
   * `<http://help.ubuntu.ru/wiki/руководство_по_ubuntu_server/управление_пакетами/apt-get>`_

   * https://pip.pypa.io/en/latest/installing.html
   * http://en.wikipedia.org/wiki/Pip_(package_manager)

Новые версии Ubuntu
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ sudo apt-get install python-pip python-dev build-essential
   $ sudo pip install --upgrade pip
   $ sudo pip install pyramid
   $ pcreate -t alchemy MyProgect

Старые версии Ubuntu
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ sudo apt-get install python-setuptools python-dev build-essential
   $ sudo easy_install pip
   $ sudo pip install --upgrade pip
   $ sudo pip install pyramid
   $ pcreate -t alchemy MyProgect

Пакетный менеджер pip
---------------------

.. code-block:: bash

   $ pip uninstall django # Удаление пакета
   $ pip install pyramid  # Установка пакета

.. code-block:: bash

   $ pip install pyramid -U # Обновление
   $ pip install pyramid --upgrade
   $ pip install pip -U # Обновление самого pip

.. code-block:: bash

   $ pip install pyramid --user # Установка локально, для этого пользователя

.. code-block:: bash

   $ pip install -r requirements.txt # Установка из файла

.. code-block:: bash

   $ pip install git+https://github.com/pylons/pyramid       # Установка по ссылке
   $ pip install git+https://bitbucket.org/zzzeek/sqlalchemy # Установка по ссылке

Установка пакетов из исходных кодов
-----------------------------------

Копирует проект в PYTHONPAH

.. code-block:: bash

   $ git clone git@github.com:myint/rstcheck.git
   $ cd rstcheck
   $ pip install .

Симлинк на директорию. Требуется для разработки, что бы не устанавливать
заново, после каждого изменения в проекте.

.. code-block:: bash

   $ git clone git@github.com:myint/rstcheck.git
   $ cd rstcheck
   $ pip install -e .
