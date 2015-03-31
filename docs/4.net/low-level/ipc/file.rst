Передача данных через файл
==========================

.. seealso::

    * `<https://ru.wikipedia.org/wiki/Перенаправление_ввода-вывода>`_

Конвейер
--------

.. seealso::

    * `<https://ru.wikipedia.org/wiki/Конвейер_(UNIX)>`_
    * http://pymotw.com/2/pipes/index.html

.. code:: bash

    $ fortune | cowsay -f `cowsay -l | sed '1,1d' | sed 's/ /\n/g' | shuf -n 1`
     ____________________________________
    / Лучше ничего не делать, чем делать \
    | ничего.                            |
    |                                    |
    \ -- Л.Н.Толстой                     /
     ------------------------------------
         \         __------~~-,
          \      ,'            ,
                /               \
               /                :
              |                  '
              |                  |
              |                  |
               |   _--           |
               _| =-.     .-.   ||
               o|/o/       _.   |
               /  ~          \ |
             (____@)  ___~    |
                |_===~~~.`    |
             _______.--~     |
             \________       |
                      \      |
                    __/-___-- -__
                   /            _ \

Именованный канал
-----------------

.. seealso::

    * `<https://ru.wikipedia.org/wiki/Именованный_канал>`_

В программировании именованный канал или именованный конвейер (англ. named pipe) — один из методов межпроцессного взаимодействия, расширение понятия конвейера в Unix и подобных ОС.

Именованный канал позволяет различным процессам обмениваться данными, даже если программы, выполняющиеся в этих процессах, изначально не были написаны для взаимодействия с другими программами.

Пример передачи "Hello World"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: not latex

   .. image:: /_static/4.net/pipe.gif
      :align: center

Создаем именованный канал при помощи утилиты `mkfifo`

.. code-block:: bash

   mkfifo pipe

Проверяем тип файла

.. no-code-block:: bash

   $ file pipe
   pipe: fifo (named pipe)

Слушаем канал

.. code-block:: bash

   cat < pipe

.. code-block:: bash

   echo "Hello World" > pipe

"Hello World" на Python
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    # sender.py

    import os

    path = "/tmp/my_program.fifo"
    os.mkfifo(path)

    fifo = open(path, "w")
    fifo.write("Hello World!\n")
    fifo.close()

.. code-block:: python
   :linenos:

   # receiver.py

   import os
   import sys

   path = "/tmp/my_program.fifo"
   fifo = open(path, "r")
   for line in fifo:
       print("Полученно: %s" % line)
   fifo.close()

.. code:: bash

   Полученно: Hello World!

Пример сжатия полученных данных
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Можно создать канал и настроить gzip на сжатие того, что туда попадает:

.. code-block:: bash

   mkfifo pipe
   gzip -9 -c < pipe > out

.. code-block:: bash

    cat file > pipe

В файле out запишутся переданные данные в сжатом виде.

Обычный файл как транспорт
--------------------------

В отличии от каналов, обычные файлы используют жесткий диск, а не ОЗУ
что гораздо медленнее.

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
   :linenos:

   import time

   # Open a file
   file = open("pipe.txt", "r")
   print("Name of the file: %s" % file.name)

   while True:
       where = file.tell()
       line = file.readline()
       if not line:
           time.sleep(1)
           file.seek(where)
       else:
           print(line)  # already has newline
