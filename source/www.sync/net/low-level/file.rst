Передача данных через файл
==========================

.. note::

    `<https://ru.wikipedia.org/wiki/Перенаправление_ввода-вывода>`_

Создадим файл, через который будет происходить обмен.

.. code-block:: bash

    $ touch pipe.txt

Будем получать данные (смотреть изменение) с помощью команды tail.

.. code-block:: bash

    $ tail -f pipe.txt

Отправим данные обычным редактированием файла.

.. code-block:: bash

    $ echo 'Привет' >> pipe.txt
    $ echo 'файловая труба!' >> pipe.txt

Результат:

.. code-block:: bash

    $ # Полученные данные
    $ tail -f pipe.txt
    Привет
    файловая труба!

    $ # Записанные данные в файле
    $ cat pipe.txt
    Привет
    файловая труба!

Реализация `tail -f` на Python

.. code-block:: python

    import time

    # Open a file
    file = open("pipe.txt", "r")
    print "Name of the file: ", file.name

    while True:
        where = file.tell()
        line = file.readline()
        if not line:
            time.sleep(1)
            file.seek(where)
        else:
            print line,  # already has newline
