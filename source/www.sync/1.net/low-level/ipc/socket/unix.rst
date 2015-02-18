Передача данных через UNIX сокеты
=================================

.. note::

    `<https://ru.wikipedia.org/wiki/Сокет_домена_UNIX>`_

Сокет домена Unix (англ. Unix domain socket, UDS) или IPC-сокет (сокет межпроцессного взаимодействия) — конечная точка обмена данными, подобная Интернет-сокету, но не использующая сетевой протокол для взаимодействия (обмена данными). Используется в операционных системах, поддерживающих стандарт POSIX, для межпроцессного взаимодействия.

Доменные соединения Unix являются по сути байтовыми потоками, сильно напоминая сетевые соединения, но при этом все данные остаются внутри одного компьютера (то есть обмен данными происходит локально). UDS используют файловую систему как адресное пространство имен, то есть они представляются процессами как иноды в файловой системе. Это позволяет двум различным процессам открывать один и тот же сокет для взаимодействия между собой. Однако, конкретное взаимодействие, обмен данными, не использует файловую систему, а только буферы памяти ядра.

Пример передачи в одну сторону
------------------------------

Сервер
~~~~~~

.. code-block:: python

    # server.py
    import os
    import os.path
    import socket

    SOCKET_FILE = './echo.socket'

    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)

    print("Открываем UNIX сокет...")
    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind(SOCKET_FILE)

    print("Слушаем...")
    while True:
        datagram = server.recv(1024)
        if not datagram:
            break
        else:
            print("-" * 20)
        print(datagram)
        if "DONE" == datagram:
            break
    print("-" * 20)
    print("Выключение...")
    server.close()
    os.remove(SOCKET_FILE)
    print("Выполнено")

Клиент
~~~~~~

.. code-block:: python

    # client.py
    import socket
    import os
    import os.path

    SOCKET_FILE = './echo.socket'

    print("Подключение...")
    if os.path.exists(SOCKET_FILE):
        client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        client.connect(SOCKET_FILE)
        print("Выполнено.")
        print("Ctrl-C что бы выйти.")
        print("Отправьте 'DONE' что бы выключить сервер.")
        while True:
            try:
                x = raw_input("> ")
                if "" != x:
                    print("ОТПРАВЛЕНО: %s" % x)
                    client.send(x)
                    if "DONE" == x:
                        print("Выключение.")
                        break
            except KeyboardInterrupt, k:
                print("Выключение.")
                break
        client.close()
    else:
        print("Не могу соединиться!")
    print("Выполнено")

Пример работы
~~~~~~~~~~~~~

.. image:: /_static/unix_socket.gif
   :align: center

Схематичное отображение
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /_static/socket_unix.svg
   :align: center
   :width: 600px
