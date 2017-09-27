Лекции
======

Установка
----------

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
