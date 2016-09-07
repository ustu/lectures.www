Visual Studio Code
==================

:l:`Visual Studio Code` отличный выбор для начинающего программиста,
имеет необходимый минимум:

* неплохую документацию
* автодополнение кода (с использованием `IntelliSense
  <https://ru.wikipedia.org/wiki/IntelliSense>`_)
* подсветка синтаксиса
* встроенный отладчик
* расширение функционала за счет плагинов
* управление системой контроля версий git
* кроссплатформенный
* бесплатный, с открытым исходным кодом

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

   <video muted="" width=600px controls="" loop="" autoplay=""
   poster="/images/python_python-linting-placeholder.png"
   src="https://az754404.vo.msecnd.net/public/python-linting.mp4"
   id="python-linting-video"></video>

Проверка синтаксиса
~~~~~~~~~~~~~~~~~~~

Показывает ошибки в коде:

.. raw:: html

    <video muted="" width=600px controls="" loop="" autoplay=""
    poster="/images/python_python-linting-placeholder.png"
    src="https://az754404.vo.msecnd.net/public/python-linting.mp4"
    id="python-linting-video"></video>

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

    <video muted="" width=600px controls="" loop="" autoplay=""
    poster="/images/python_python-debugging-placeholder.png"
    src="https://az754404.vo.msecnd.net/public/python-debugging.mp4"
    id="python-debugging-video"></video>

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

Python скрипты
--------------

.. seealso::

    http://trypyramid.com

:l:`Visual Studio Code` требует для отладки открывать не просто файл, а
директорию. Это необходимо, что бы в этом каталоге сохранить локальные
настройки редактора. Такая директория будет считаться проектом для редактора.

Для примера, создадим директорию `hello1` и откроем в редакторе ``File->Open
Folder...``.

Создадим в этой директории файл `myapp.py`:

.. image:: /_static/999.additions/texteditor/vscode_add_file.png

Добавим в файл пример с сайта http://trypyramid.com

.. code-block:: python

    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    from pyramid.response import Response

    def hello_world(request):
        return Response('Hello %(name)s!' % request.matchdict)

    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

Для запуска приложения, заходим в режим отладки по нажатию на кнопку:

.. image:: /_static/999.additions/texteditor/vscode_debugicon.png

.

.. image:: /_static/999.additions/texteditor/vscode_debug_noconfig.png
   :width: 600px
   :align: center

Пока у нас нет никаких настроек отладки/запуска проекта, но при первом
запуске редактор предложит их выбрать из существующих шаблонов.

.. image:: /_static/999.additions/texteditor/vscode_chose_dbg_template.png

Шаблон `Python` создает настройки в файле `launch.json` в локальной директории,
которые выглядят примерно так:

.. code-block:: json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python",
                "type": "python",
                "request": "launch",
                "stopOnEntry": true,
                "pythonPath": "${config.python.pythonPath}",
                "program": "${file}",
                "debugOptions": [
                    "WaitOnAbnormalExit",
                    "WaitOnNormalExit",
                    "RedirectOutput"
                ]
            },
            {
                "name": "Python Console App",
                "type": "python",
                "request": "launch",
                "stopOnEntry": true,
                "pythonPath": "${config.python.pythonPath}",
                "program": "${file}",
                "externalConsole": true,
                "debugOptions": [
                    "WaitOnAbnormalExit",
                    "WaitOnNormalExit"
                ]
            },
            {
                "name": "Django",
                "type": "python",
                "request": "launch",
                "stopOnEntry": true,
                "pythonPath": "${config.python.pythonPath}",
                "program": "${workspaceRoot}/manage.py",
                "args": [
                    "runserver",
                    "--noreload"
                ],
                "debugOptions": [
                    "WaitOnAbnormalExit",
                    "WaitOnNormalExit",
                    "RedirectOutput",
                    "DjangoDebugging"
                ]
            },
            {
                "name": "Watson",
                "type": "python",
                "request": "launch",
                "stopOnEntry": true,
                "pythonPath": "${config.python.pythonPath}",
                "program": "${workspaceRoot}/console.py",
                "args": [
                    "dev",
                    "runserver",
                    "--noreload=True"
                ],
                "debugOptions": [
                    "WaitOnAbnormalExit",
                    "WaitOnNormalExit",
                    "RedirectOutput"
                ]
            },
            {
                "name": "Attach",
                "type": "python",
                "request": "attach",
                "localRoot": "${workspaceRoot}",
                "remoteRoot": "${workspaceRoot}",
                "port": 3000,
                "secret": "my_secret",
                "host": "localhost"
            }
        ]
    }

Это универсальный шаблон, который добавляет несколько вариантов запуска
приложений. Нас будет интересовать первый вариант ``Python``, просто
запускающий python файл.

.. image:: /_static/999.additions/texteditor/vscode_python_dbg.png

Запущенное приложение останавливается на первой строчке, что позволяет нам
продолжать выполнение программы по шагам.

.. image:: /_static/999.additions/texteditor/vscode_python_run.png
   :width: 600px
   :align: center

После выполнения второй строки, интерпретатор выдаст ошибку ``ImportError: No
module named pyramid.config``. Это происходит из-за того что в нашем `Python`
окружении не установлен модуль `pyramid`.

.. image:: /_static/999.additions/texteditor/vscode_python_dbg_import_error.png
   :width: 600px
   :align: center

Решить эту проблему можно двумя способами:

1. Установить `Pyramid` в глобальное окружение.

   .. code-block:: bash

       $ pip install --user pyramid

2. Создать виртуальное окружение, установить в нем `Pyramid` и прописать его в
   настройках :l:`Visual Studio Code`.

   .. seealso::

       Как создать :ref:`virtualenv`

   * Создаем виртуальное окружение:

     .. code-block:: bash

         $ cd /path/to/hello1/
         $ pyvenv hello1_env
         $ source ./hello1_env/bin/activate

   * Устанавливаем `Pyramid`:

     .. code-block:: bash

         (hello1_env)$ pip install pyramid

   * Прописываем путь до виртуального окружения в настройках проекта
     :l:`Visual Studio Code` (файл `launch.json`):

     .. image:: /_static/999.additions/texteditor/vscode_python_venv.png
        :width: 600px
        :align: center

     .. code-block:: json
         :emphasize-lines: 2,6

         {
             "name": "PythonVenv",
             "type": "python",
             "request": "launch",
             "stopOnEntry": true,
             "pythonPath": "${workspaceRoot}/hello1_env/bin/python",
             "program": "${file}",
             "debugOptions": [
                 "WaitOnAbnormalExit",
                 "WaitOnNormalExit",
                 "RedirectOutput"
             ]
         }

После этого появится возможность запускать наш скрипт в локальном виртуальном
окружении. Запущенная программа будет доступна по адресу
http://localhost:8080/hello/foo. В консоле отладчика можно наблюдать ее вывод.

.. image:: /_static/999.additions/texteditor/vscode_pyramid_run.png
   :width: 600px
   :align: center

Поставим точку останова внутри функции ``hello_world``, в строке 6. Это
позволит нам остановить программу при запуске этой функции. После запуска
программа будет нормально работать, пока мы не зайдем по адресу
http://localhost:8080/hello/foo, в этом случае запустится функция
``hello_world`` и выполнение программы прервется, до тех пор пока мы ее не
продолжим вручную.

.. image:: /_static/999.additions/texteditor/vscode_pyramid_breakpoint.png
   :width: 600px
   :align: center

Примерно так выглядит процесс разработки и отладки программ на `Python`.
Осталось только инициализировать `git` репозиторий и выложить проект на
https://github.com.

1. Инициализируем репозиторий:

   .. image:: /_static/999.additions/texteditor/vscode_git_init.png
      :width: 600px
      :align: center

2. Добавим файл ``.gitignore``:

   Для этого нам потребуется скопировать содержимое
   https://www.gitignore.io/api/visualstudiocode,python в файл ``.gitignore``
   и добавить туда директорию ``hello1_env``, что бы она не участвовала в
   процессе создания версий.

   .. image:: /_static/999.additions/texteditor/vscode_gitignore.png
      :width: 600px
      :align: center

   .. code-block:: text
       :emphasize-lines: 3

       # Created by https://www.gitignore.io/api/visualstudiocode,python

       hello1_env

       ### VisualStudioCode ###
       .vscode/*
       !.vscode/settings.json
       !.vscode/tasks.json
       !.vscode/launch.json


       ### Python ###
       # Byte-compiled / optimized / DLL files
       __pycache__/
       *.py[cod]

       ...

3. Создаем первый коммит

   Для создания коммита требуется ввести комментарий и нажать на кнопку в виде
   галочки.

   .. image:: /_static/999.additions/texteditor/vscode_git_commit.png
      :width: 600px
      :align: center

4. Отправляем изменения на https://github.com

   * Добавляем плагин `Git Easy` в проект
   * Создаем репозиторий на :l:`GitHub`

   .. image:: /_static/999.additions/texteditor/github_create_repo.png

   * Прописываем путь до гитхаба в нашем проекте, при помощи команды ``Git
     Easy:Add Orign``

     .. image::
         /_static/999.additions/texteditor/vscode_giteasy_add_orign.png

     .. image::
         /_static/999.additions/texteditor/vscode_git_origin.png

   * Отправляем изменения на `GitHub`, при помощи команды
     ``Git Easy:Push Current Branch to Origin``

     .. image::
         /_static/999.additions/texteditor/vscode_git_push.png

     При успешном выполнении команды, мы должны увидеть сообщение типа:

     .. code-block:: text

         To github.com:uralbash/hello1.git
         * [new branch]      master -> master

     .. image::
         /_static/999.additions/texteditor/vscode_git_push_ok.png
         :width: 600px
         :align: center

     Файлы будут доступны по адресу https://github.com/uralbash/hello1

     .. image::
         /_static/999.additions/texteditor/github_hello1.png
         :width: 600px
         :align: center

Pyramid
-------

.. seealso::

    http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html

Фреймворк `Pyramid` имеет несколько стартовых шаблонов, которые нужны для того,
что бы не начинать писать код с нуля. Рассмотрим как создать шаблон с БД
`sqlite` + `SQLAlchemy` и настроить его в :l:`Visual Studio Code`.

Для начала создадим директорию `hello2` и виртуальное окружение `hello2_env`:

.. code-block:: bash

   $ mkdir hello2
   $ cd hello2/
   $ pyvenv hello2_env
   $ source hello2_env/bin/activate
   $ pip install pyramid

.. seealso::

    http://docs.pylonsproject.org/projects/pyramid/en/latest/pscripts/index.html

После установки `Pyramid`, в окружении появляется команда ``pcreate``. С ее
помощью создадим проект по шаблону:

.. code-block:: bash

   $ pcreate -t alchemy .
   $ ls
   CHANGES.txt  development.ini  hello2  hello2_env  MANIFEST.in  production.ini  pytest.ini  README.txt  setup.py

Устанавливаем его как `Python` пакет:

.. code-block:: bash

   $ pip install -e .
   $ pserve development.ini
   Starting server in PID 17311.
   Serving on http://localhost:6543

После запуска, становится доступен адрес http://localhost:6543

.. image:: /_static/999.additions/texteditor/pyramid_home.png

Но так-как БД еще не создана, отображается страница с подсказкой как ее
инициализировать:

.. code-block:: bash

    $ initialize_hello2_db development.ini

Теперь мы увидим стартовую страницу шаблона `alchemy`.

.. image:: /_static/999.additions/texteditor/pyramid_home2.png
   :width: 600px
   :align: center

Проект на пирамиде запускается при помощи утилиты ``pserve``. Добавим
конфигурацию для `Pyramid` в файл настроек ``launch.json``, что бы можно было
запускать/отлаживать приложение из редактора:

.. code-block:: json
    :emphasize-lines: 4-15

    {
        "version": "0.2.0",
        "configurations": [{
            "name": "Pyramid",
            "type": "python",
            "request": "launch",
            "stopOnEntry": true,
            "pythonPath": "${workspaceRoot}/hello2_env/bin/python",
            "program": "${workspaceRoot}/hello2_env/bin/pserve",
            "args": ["${workspaceRoot}/development.ini"],
            "debugOptions": [
                "WaitOnNormalExit",
                "RedirectOutput"
            ]
        }]
    }

Попробуем запустить:

.. image:: /_static/999.additions/texteditor/vscode_pserve_run.png
   :width: 600px
   :align: center

Поставим точку останова в функции ``my_view`` в файле
``hello2/views/default.py``.

.. image:: /_static/999.additions/texteditor/vscode_pyramid_dbg.png
   :width: 600px
   :align: center

После обновления страницы http://localhost:6543 в браузере, программа остановит
свое выполнение в этой точке, а браузер будет ждать пока мы не закончим отладку
и не продолжим выполнение вручную.

JavaScript
----------

.. image:: /_static/999.additions/texteditor/vscode_js.png
   :width: 600px
   :align: center
