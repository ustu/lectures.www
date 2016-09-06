Visual Studio Code
==================

:l:`Visual Studio Code` отличный выбор для начинающего программиста,
имеет необходимый минимум:

* неплохую документацию
* автодополнение кода
* подсветка синтаксиса
* встроенный отладчик
* расширение функционала за счет плагинов
* управление системой контроля версий git
* кроссплатформенный
* бесплатный с открытым исходным кодом

Также редактор адаптирован для Веб-разработки и вполне подойдет для серьезных
проектов как основной инструмент редактирования кода.

Установка
---------

.. seealso::

    https://code.visualstudio.com/docs/setup/setup-overview

Linux
~~~~~

.. seealso::

    https://code.visualstudio.com/docs/setup/linux

1. Скачиваем дистрибутив для своей ОС https://code.visualstudio.com/download
2. Для Linux существуют два типа пакетов, самых популярных форматов, rpm и deb.

   Установка в Ubuntu/Debian:

   .. code-block:: bash

       $ sudo dpkg -i <file>.deb

   CentOS/Fedora:

   .. code-block:: bash

       $ sudo yum install <file>.rpm

   Fedora > 22 версии:

   .. code-block:: bash

       $ sudo dnf install <file>.rpm

3. После установки можно запустить редактор следующей командой:

   .. code-block:: bash

       $ code

Nix
~~~

Пакетный менеджер :l:`Nix` работает на любом Linux дистрибутиве, содержит
богатую базу уже готовых пакетов, в том числе и :l:`vscode`.

1. Установка пакетного менеджера:

   .. code-block:: bash

       $ curl https://nixos.org/nix/install | sh

2. Установка :l:`Visual Studio Code`:

   .. code-block:: bash

       $ nix-env -i vscode

Плагины
-------

.. seealso::

    https://code.visualstudio.com/docs/editor/extension-gallery

Редактор имеет возможность расширения функционала за счет плагинов и удобный
интерфейс их установки, доступный по нажатию кнопки:

.. image::
    /_static/999.additions/texteditor/extension-gallery_extensions-view-icon.png

Из списка можно выбрать любой плагин и установить, после чего он применит свои
настройки к редактору.

.. image::
    /_static/999.additions/texteditor/extension-gallery_extensions-popular.png
    :width: 600px
    :align: center

Расширения можно искать введя название или ключевые слова в строке поиска,
например `Python`.

.. image::
    /_static/999.additions/texteditor/extension-gallery_extensions-python.png
    :width: 600px
    :align: center

Существует огромное количество расширений для `Go`, `C#`, `C/C++`, `Nix`,
`Haskell`, `Python`, `JS`, `TypeScript` и др.

Python
------

.. seealso::

    https://code.visualstudio.com/docs/languages/python

После установки плагина `Python` нам становятся доступны многие функции:

* Автодополнение кода
* Проверка синтаксиса
* Отладка
* Подсказки
* Переход к определению функции, класса и прочее

Автодополнение
~~~~~~~~~~~~~~

Работает при наборе по нажатию :kbd:`Ctrl` + :kbd:`Space`.

.. raw:: html

   <video muted="" width=600px controls="" loop="" autoplay="" poster="/images/python_python-linting-placeholder.png" src="https://az754404.vo.msecnd.net/public/python-linting.mp4" id="python-linting-video"></video>

Проверка синтаксиса
~~~~~~~~~~~~~~~~~~~

Показывает ошибки в коде:

.. raw:: html

    <video muted="" width=600px controls="" loop="" autoplay="" poster="/images/python_python-linting-placeholder.png" src="https://az754404.vo.msecnd.net/public/python-linting.mp4" id="python-linting-video"></video>

Работает если установлены Python пакеты `Pylint`, `Pep8` или `Flake8`.

.. tip::

    .. code-block:: bash

        $ pip install -U --user pylint pep8 flake8

Отладка
~~~~~~~

.. seealso::

    https://code.visualstudio.com/docs/editor/debugging

Встроенный в редактор отладчик позволяет отлаживать код визуально,
устанавливать точки останова мышкой и просматривать переменный в отдельном
окне. Это похоже на отладку в различных IDE, таких как :l:`QtCreator` или
:l:`Wingware`.

.. raw:: html

    <video muted="" width=600px controls="" loop="" autoplay="" poster="/images/python_python-debugging-placeholder.png" src="https://az754404.vo.msecnd.net/public/python-debugging.mp4" id="python-debugging-video"></video>

Это избавляет программиста писать мучительные строки типа `printf` или `import
pdb;pdb.set_trace();`.

Настройки
---------

.. seealso::

    https://code.visualstudio.com/docs/customization/userandworkspace

Настройки хранятся в формате `JSON` и доступны из меню
``File->Preferences->User Settings``.

Шрифт
~~~~~

Шрифт задается в настройках ``File->Preferences->User Settings``:

.. code-block:: json
   :emphasize-lines: 4

    // Place your settings in this file to overwrite the default settings
    {
        // Controls the font size.
        "editor.fontSize": 16
    }

Автодополнение через <Tab>
~~~~~~~~~~~~~~~~~~~~~~~~~~

Более привычно дополнять код по клавише :kbd:`<Tab>`. Для этого необходимо
открыть настройки пользователя ``File->Preferences->User Settings`` и прописать
опцию ``editor.tabCompletion``:

.. code-block:: json
   :emphasize-lines: 6

    // Place your settings in this file to overwrite the default settings
    {
        // Controls the font size.
        "editor.fontSize": 16,
        // Insert snippets when their prefix matches. Works best when 'quickSuggestions' aren't enabled.
        "editor.tabCompletion": true
    }

Язык
~~~~

.. seealso::

    https://code.visualstudio.com/docs/customization/locales

1. Открываем командную строку :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`P`
2. Вводим команду `Configure Language`

   .. image::
       /_static/999.additions/texteditor/locales_configure-language-command.png
       :width: 600px
       :align: center

3. Меняем локаль на нужную, например ``ru``:

   .. image::
       /_static/999.additions/texteditor/locales_locale-intellisense.png
       :width: 600px
       :align: center

   .. code-block:: json

       {
           // Defines VS Code's display language.
           "locale": "ru"
       }

Тема
~~~~

Цветовое оформление задается в настройках ``File->Preferences->Color Theme``.

Git
---

.. seealso::

    https://code.visualstudio.com/docs/editor/versioncontrol

Умеет подсвечивать изменения в файлах с предыдущего коммита, выполнять команды
`git` и отслеживать состояние, например какая текущая ветка.

.. image:: /_static/999.additions/texteditor/versioncontrol_merge.png
   :width: 600px
   :align: center
