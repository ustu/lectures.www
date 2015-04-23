Управление пакетами в Python
============================

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

   $ pip install git+https://github.com/pylons/pyramid   # Установка по ссылке
   $ pip install https://bitbucket.org/zzzeek/sqlalchemy # Установка по ссылке

Установка из исходных кодов
---------------------------

Копирует проект в PYTHONPAH

.. code-block:: bash

   $ git clone git@github.com:myint/rstcheck.git
   $ cd rstcheck
   $ python setup.py install

Симлинк на директорию. Требуется для разработки, что бы не устанавливать заново, после каждого изменения в проекте.

.. code-block:: bash

   $ git clone git@github.com:myint/rstcheck.git
   $ cd rstcheck
   $ python setup.py develop
