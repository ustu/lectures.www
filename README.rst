Лекции
======

Технологии
----------

Лекции пишутся при помощи разметки `reStructuredText
<https://ru.wikipedia.org/wiki/ReStructuredText>`_. Собираются генератором
документации `Sphinx
<https://ru.wikipedia.org/wiki/Sphinx_(генератор_документации)>`_.

Редактирование
--------------

Файлы лекций имеют расширение ``.rst`` и расположены в директории ``docs``.
`GitHub` умеет корректно отображать содержимое файлов, пример
https://github.com/ustu/lectures.www/blob/master/docs/6.www.sync/2.codding/1.mvc.rst.

Редактировать текст можно встроенным редактором `GitHub` или любимым редактором
склонировав репозиторий локально.

Перейти на страницу для редактирования из лекций можно при помощи кнопки в
верхнем правом углу "edit on github", пример
http://lectureswww.readthedocs.io/6.www.sync/2.codding/1.mvc.html.

Установка
---------

1. Инициализация
^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ git submodule update --init --recursive

2. Сборка
^^^^^^^^^

Для сборки необходимо установить пакетный менеджер `Nix
<https://nixos.org/nix/>`_.

.. code-block:: bash

    $ curl https://nixos.org/nix/install | sh

После установки `Nix` сборка осуществляется командой `make`:

.. code-block:: bash

    $ make

3. Запуск
^^^^^^^^^

.. code-block:: bash

    $ firefox build/html/index.html
