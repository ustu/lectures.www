DNS
===

В сети используются системы доменных имен (DNS),
для преобразования имени сайта (например lectureswww.readthedocs.org)
в серии из 4-х цифр (для IPv4). Первое что нужно сделать программисту
это преобразовать доменное имя в IP адрес. В языке программирования Python
это можно сделать при помощи модуля `socket`.

Переводим имя хоста в IP адрес
------------------------------

.. note::

    * https://docs.python.org/2/library/socket.html#socket.gethostbyname
    * http://man7.org/linux/man-pages/man3/gethostbyname.3.html
    * https://msdn.microsoft.com/en-us/library/windows/desktop/ms738524(v=vs.85).aspx

.. code-block:: python

    import socket
    print(socket.gethostbyname('localhost'))    # результат из hosts файла
    print(socket.gethostbyname('google.com'))   # ваша ОС отправит запрос на удаленный DNS сервер

::

    127.0.0.1
    213.180.204.3

Расширенное представление

.. code-block:: python

    import socket
    print(socket.gethgstgyname_ex("localhost"))
    print(socket.gethostbyname_ex("google.com"))
    print(socket.gethostbyname_ex("www.google.com"))
    print(socket.gethostbyname_ex("www.python.org"))

Вернет (hostname, aliaslist, ipaddrlist) где hostname основное имя хоста по этому IP,
aliaslist список (может быть пустым) альтернативных имен на этом IP, ipaddrlist список IPv4 адресов прикрепленных к этому домену (часто не множество IP).

::

    ('localhost', [], ['127.0.0.1'])
    ('google.com', [], ['213.180.204.3'])
    ('www.google.com', [], ['195.64.213.53', '195.64.213.42', '195.64.213.44', '195.64.213.59', '195.64.213.49', '195.64.213.38', '195.64.213.29', '195.64.213.27', '195.64.213.23', '195.64.213.15', '195.64.213.19', '195.64.213.34', '195.64.213.45', '195.64.213.30', '195.64.213.57'])
    ('python.map.fastly.net', ['www.python.org'], ['23.235.43.223'])

В реальных программах нужно использовать перехват исключений

.. code-block:: python

    import socket
    name = "www.python.org"
    try:
        host = socket.gethostbyname(name)
        print(host)
    except socket.gaierror, err:
        print("cannot resolve hostname: %s %s" % (name, err))

Пример DNS обращений к текущим лекциям (lectureswww.readthedocs.org)

.. no-code-block:: python

    In [1]: print socket.gethostbyname('lectureswww.readthedocs.org')
    162.209.114.75

    In [2]: print socket.gethostbyname_ex('lectureswww.readthedocs.org')
    ('lectureswww.readthedocs.org', [], ['162.209.114.75'])

    In [3]: print socket.gethostbyaddr('162.209.114.75')
    ('readthedocs.org', [], ['162.209.114.75'])

Локальное имя машины
--------------------

.. code-block:: python

    import socket
    print(socket.gethostname())

::

    my-laptop

Получаем fqdn (fully qualified domain name)
-------------------------------------------

.. note::

    * http://ru.wikipedia.org/wiki/FQDN


.. no-code-block:: python

    In [1]: import socket

    In [2]: print socket.getfqdn("8.8.8.8")
    google-public-dns-a.google.com

    In [3]: print socket.getfqdn("193.107.218.31")
    193.107.218.31

    In [4]: print socket.getfqdn("127.0.0.1")
    localhost

    In [5]: print socket.getfqdn("8.8.4.4")
    google-public-dns-b.google.com
