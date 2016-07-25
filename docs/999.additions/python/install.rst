Установка Python
================

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

Выбираем ветку ``3.5`` (cpython версии 3.5):

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

Укажем виртуальному окружению где находится интерпретатор cpython:

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

Склонируем репозитарий админки https://github.com/ITCase/pyramid_sacrud.git в
директорию ``/home/user/Projects``.

.. code-block:: bash

   $ cd /home/user/Projects/
   $ git clone https://github.com/ITCase/pyramid_sacrud.git

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


Windows
-------

Установка интерпретатора CPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Все версии CPython можно найти по адресу https://www.python.org/downloads/

.. figure:: /_static/999.additions/python/install/windows/python_org_downloads.png
   :align: center
   :width: 500pt

Выберем, например, версию 2.7.10 для 32 битной операционной системы.

.. figure:: /_static/999.additions/python/install/windows/cpython_2.7.10_32_download.png
   :align: center
   :width: 500pt

Запускаем инсталятор:

.. figure:: /_static/999.additions/python/install/windows/python_setup.png
   :align: center

По умолчанию Python устанавливается в директорию ``C:\Python27\``.

.. figure:: /_static/999.additions/python/install/windows/python_setup2.png
   :align: center

Выбираем опцию "добавить python.exe в окружение".

.. figure:: /_static/999.additions/python/install/windows/python_setup3.png
   :align: center

Теперь интерпретатор Python доступен из консоли.

.. figure:: /_static/999.additions/python/install/windows/python_setup4.png
   :align: center

Пример Hello Word!.

.. figure:: /_static/999.additions/python/install/windows/cmd_python.png
   :align: center

Пакетный менеджер pip
~~~~~~~~~~~~~~~~~~~~~

После установки CPython в окружении появится утилита ``easy_install``. С
помощью нее можно установит `pip`, следующим образом:

.. code-block:: bash

   $ easy_install pip

Или при помощи скрипта ``get-pip.py``.
Скрипт можно скачать по прямой ссылке
https://raw.github.com/pypa/pip/master/contrib/get-pip.py

.. figure:: /_static/999.additions/python/install/windows/get_pip.png
   :align: center

Запускается скрипт как обычная Python программа.

.. figure:: /_static/999.additions/python/install/windows/cmd_get_pip.png
   :align: center

Теперь можно устанавливать Python пакеты.

.. figure:: /_static/999.additions/python/install/windows/pip_install.png
   :align: center

Виртуальное окружение Virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/999.additions/python/install/windows/install_virtualenv.png
   :align: center

Зададим переменную окружения ``WORKON_HOME`` которая указывает где будут
хранится изолированные окружения.

.. figure:: /_static/999.additions/python/install/windows/workon_home.png
   :align: center

Теперь можно создавать изолированные окружения для каждого проекта.

.. figure:: /_static/999.additions/python/install/windows/workon.png
   :align: center

Компиляция пакетов
~~~~~~~~~~~~~~~~~~

Некоторые Python пакеты написаны с использование языка программирования Си,
поэтому при установке они требуют компиляции. Если у вас не установлен
компилятор, пакет не будет установлен.

Попробуем установить :l:`NumPy` без компилятора.

.. code-block:: bash

   $ pip install numpy

.. figure:: /_static/999.additions/python/install/windows/fail_build.png
   :align: center

После установки следующих приложений для Windows:

| Microsoft .NET Framework 2.0 с пакетом обновления 2 (SP2)
| https://www.microsoft.com/en-us/download/details.aspx?id=1639

| Microsoft Visual C++ Compiler for Python 2.7
| http://www.microsoft.com/en-us/download/details.aspx?id=44266

Компиляция пройдет успешно:

.. figure:: /_static/999.additions/python/install/windows/compile.png
   :align: center

Установка git
~~~~~~~~~~~~~

Скачайте и запустите инсталятор по ссылке http://git-scm.com/download/win.

.. figure:: /_static/999.additions/python/install/windows/git_1.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_2.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_3.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_4.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_5.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_6.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_7.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_8.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/git_9.png
   :align: center

Пример
~~~~~~

Склонируем репозитарий админки https://github.com/ITCase/pyramid_sacrud.git в
директорию ``C:\Projects``.

.. code-block:: bash

   $ git clone https://github.com/ITCase/pyramid_sacrud.git

.. figure:: /_static/999.additions/python/install/windows/git_clone.png
   :align: center

Установим :l:`pyramid_sacrud` из исходных кодов.

.. code-block:: bash

   $ cd C:\Projects\pyramid_sacrud
   $ mkvirtualenv pyramid_sacrud
   $ python setup.py develop

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud_install.png
   :align: center

Далее установим пример ``pyramid_sacrud/example``

.. code-block:: bash

   $ cd C:\Projects\pyramid_sacrud\example
   $ workon pyramid_sacrud
   $ python setup.py develop

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud_example_install.png
   :align: center

Пакеты устанавливаются в виртуальное окружение с названием ``pyramid_sacrud``.

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud_pip_list.png
   :align: center

Установим дополнительные пакеты ``six``, ``pyramid_jinja2==1.10`` и ``iso8601``:

.. code-block:: bash

   $ pip install six iso8601 pyramid_jinja2==1.10

Теперь можно запустить пример:

.. code-block:: bash

   $ cd C:\Projects\pyramid_sacrud\example
   $ workon pyramid_sacrud
   $ pserve development.ini

.. figure:: /_static/999.additions/python/install/windows/run_example.png
   :align: center

Заходим на http://localhost:6543/admin/

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud.png
   :align: center

.. figure:: /_static/999.additions/python/install/windows/pyramid_sacrud2.png
   :align: center


MacOS
------

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

Склонируем репозитарий админки https://github.com/ITCase/pyramid_sacrud.git в
директорию ``/home/user/Projects``.

.. code-block:: bash

   $ cd /home/user/Projects/
   $ git clone https://github.com/ITCase/pyramid_sacrud.git

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
