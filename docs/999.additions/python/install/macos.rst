Установка Python в ОС MacOS
===========================

.. topic:: Homebrew

    `Homebrew`_ является очень удобным пакетным менеджером для MacOS. Все дальнейшие манипуляции по установке пакетов будут осуществлены с его использованием (где это возможно, конечно).

    **Установка**

    .. code-block:: bash

        $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Установка интерпретатора CPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ brew install python

Пакетный менеджер pip
~~~~~~~~~~~~~~~~~~~~~

При использовании `Homebrew`_ для установки python'а pip поставится автоматически.

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

    $ brew install gcc

Для успешной установки GCC необходимо наличие установленного `XCode`_ в системе.

.. note::

    Для старых версий MacOS необходимо установить старую же версию XCode с диска, который поставляется вместе с Вашей операционной системой.

Установка git
~~~~~~~~~~~~~

.. code-block:: bash

   $ brew intall git

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

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud_macos.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud2_macos.png
   :align: center


.. _Homebrew: http://brew.sh/
.. _XCode: https://developer.apple.com/xcode/
