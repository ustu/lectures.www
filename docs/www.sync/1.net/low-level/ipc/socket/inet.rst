Передача данных через INET сокеты
=================================

.. image:: /_static/socket.svg
   :width: 600px

TCP пример
----------

.. seealso::

    * https://wiki.python.org/moin/TcpCommunication

Это простой пример эхо-сервера при помощи TCP.

.. image:: /_static/tcp_socket.gif
   :align: center

TCP клиент
~~~~~~~~~~

.. literalinclude:: /../sourcecode/net/socket/inet/1.tcp_client.py
   :language: python
   :linenos:

В роли клиента может выступать утилита `telnet`

.. code-block:: bash

   $ telnet localhost 5005

TCP сервер
~~~~~~~~~~

.. literalinclude:: /../sourcecode/net/socket/inet/1.tcp_server.py
   :language: python
   :linenos:

Способы определения длины сообщения:

#. Передать отдельно
#. Читать до разделителя (в http это пустая строка)
#. Передать в заголовке (в  http это content-length)
#. Договориться что размер будет фиксированным (как в примере)
#. Читать данные пока не вернется 0

UDP пример
----------

.. seealso::

    * https://wiki.python.org/moin/UdpCommunication

Это простой пример приемо-передачи сообщений при помощи UDP.

.. image:: /_static/udp_socket.gif
   :align: center

UDP клиент
~~~~~~~~~~

.. literalinclude:: /../sourcecode/net/socket/inet/1.udp_client.py
   :language: python
   :linenos:

В роли клиента может выступать утилита `netcat`

.. code-block:: bash

   $ nc localhost 5005 -u

UDP сервер
~~~~~~~~~~

.. literalinclude:: /../sourcecode/net/socket/inet/1.udp_server.py
   :language: python
   :linenos:

Сырые сокеты
------------

.. seealso::

    * `<https://ru.wikipedia.org/wiki/Сырой_сокет>`_
    * https://github.com/YingquanYuan/raw_sockets
    * http://stackoverflow.com/questions/24415294/python-arp-sniffing-raw-socket-no-reply-packets
    * http://www.binarytides.com/python-packet-sniffer-code-linux

**Сырой сокет** - разновидность сокетов Беркли, позволяющий собирать TCP/IP-пакеты, контролируя каждый бит заголовка и отправляя в сеть нестандартные пакеты.

.. literalinclude:: /../sourcecode/net/socket/inet/1.raw_socket_sniff.py
   :language: python
   :linenos:

.. code-block:: bash

    # python 1.raw_socket_sniff.py
    ****************_ETHERNET_FRAME_****************
    Dest MAC:         ffffffffffff
    Source MAC:       0024b2841922
    Type:             0806
    ************************************************
    ******************_ARP_HEADER_******************
    Hardware type:    0001
    Protocol type:    0800
    Hardware size:    06
    Protocol size:    04
    Opcode:           0001
    Source MAC:       0024b2841922
    Source IP:        192.168.1.1
    Dest MAC:         000000000000
    Dest IP:          192.168.1.27
    *************************************************

    ****************_ETHERNET_FRAME_****************
    Dest MAC:         ffffffffffff
    Source MAC:       0024b2841922
    Type:             0806
    ************************************************
    ******************_ARP_HEADER_******************
    Hardware type:    0001
    Protocol type:    0800
    Hardware size:    06
    Protocol size:    04
    Opcode:           0001
    Source MAC:       0024b2841922
    Source IP:        192.168.1.1
    Dest MAC:         000000000000
    Dest IP:          192.168.1.27
    *************************************************

HTTP клиент
-----------

.. literalinclude:: /../sourcecode/net/socket/inet/1.http_socket.py
   :language: python
   :linenos:

.. code-block:: bash

    $ python 1.http_socket.py
    HTTP/1.1 200 OK
    Server: nginx
    Date: Thu, 19 Feb 2015 12:50:07 GMT
    Content-Type: application/json
    Content-Length: 32
    Connection: close
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Credentials: true

    {
      "origin": "82.186.14.112"
    }
