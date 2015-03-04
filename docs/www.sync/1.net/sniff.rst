Анализ трафика
==============

.. seealso::

    * `<https://ru.wikipedia.org/wiki/Анализатор_трафика>`_

Анализатор трафика, или сниффер (от англ. to sniff — нюхать) — сетевой анализатор трафика, программа или программно-аппаратное устройство, предназначенное для перехвата и последующего анализа, либо только анализа сетевого трафика, предназначенного для других узлов.

Сниффер может анализировать только то, что проходит через его сетевую карту. Внутри одного сегмента сети Ethernet все пакеты рассылаются всем машинам, из-за этого возможно перехватывать чужую информацию. Использование коммутаторов (switch, switch-hub) и их грамотная конфигурация уже является защитой от прослушивания. Между сегментами информация передаётся через коммутаторы. Коммутация пакетов — форма передачи, при которой данные, разбитые на отдельные пакеты, могут пересылаться из исходного пункта в пункт назначения разными маршрутами. Так что если кто-то в другом сегменте посылает внутри него какие-либо пакеты, то в ваш сегмент коммутатор эти данные не отправит.

Перехват трафика может осуществляться:

.. seealso::

   * `<https://ru.wikipedia.org/wiki/Network_tap>`_
   * `<https://ru.wikipedia.org/wiki/MAC-спуфинг>`_
   * `<https://ru.wikipedia.org/wiki/Спуфинг>`_

*  обычным «прослушиванием» сетевого интерфейса (метод эффективен при использовании в сегменте концентраторов (хабов) вместо коммутаторов (свитчей), в противном случае метод малоэффективен, поскольку на сниффер попадают лишь отдельные фреймы);
*  подключением сниффера в разрыв канала;
*  ответвлением (программным или аппаратным) трафика и направлением его копии на сниффер (Network tap);
*  через анализ побочных электромагнитных излучений и восстановление таким образом прослушиваемого трафика;
*  через атаку на канальном (2) (MAC-spoofing) или сетевом (3) уровне (IP-spoofing), приводящую к перенаправлению трафика жертвы или всего трафика сегмента на сниффер с последующим возвращением трафика в надлежащий адрес.

tcpdump
-------

.. seealso::

   * https://ru.wikipedia.org/wiki/Tcpdump

tcpdump — утилита UNIX (есть клон для Windows), позволяющая перехватывать и анализировать сетевой трафик, проходящий через компьютер, на котором запущена данная программа.

Основные назначения tcpdump:

* Отладка сетевых приложений.
* Отладка сети и сетевой конфигурации в целом.

Просмотр интерфейсов
~~~~~~~~~~~~~~~~~~~~

.. no-code-block:: bash

    $ sudo tcpdump -D
    1.wlan0 [Up, Running]
    2.docker0 [Up, Running]
    3.vboxnet0 [Up, Running]
    4.vboxnet1 [Up, Running]
    5.veth283f985 [Up, Running]
    6.any (Pseudo-device that captures on all interfaces) [Up, Running]
    7.lo [Up, Running, Loopback]
    8.eth0 [Up]
    9.bluetooth-monitor (Bluetooth Linux Monitor)
    10.nflog (Linux netfilter log (NFLOG) interface)
    11.nfqueue (Linux netfilter queue (NFQUEUE) interface)
    12.usbmon1 (USB bus number 1)
    13.usbmon2 (USB bus number 2)

Перехват всех запросов интерфейса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Если tcpdump запустить без параметров, он будет выводить информацию обо всех сетевых пакетах. С помощью параметра -i можно указать сетевой интерфейс, с которого следует принимать данные:

.. code-block:: bash

    $ sudo tcpdump -i 1

или

.. no-code-block:: bash

    $ sudo tcpdump -i wlan0
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlan0, link-type EN10MB (Ethernet), capture size 262144 bytes
    19:04:24.115872 STP 802.1d, Config, Flags [none], bridge-id 8000.bc:ae:c5:88:91:28.8001, length 35
    19:04:24.219665 IP Arkasha-PC.local.bootpc > 255.255.255.255.bootps: BOOTP/DHCP, Request from 00:1b:fc:6c:c2:42 (oui Unknown), length 300
    19:04:25.118303 IP x220t.local.32371 > google-public-dns-a.google.com.domain: 29524+ PTR? 255.255.255.255.in-addr.arpa. (46)
    19:04:25.186526 IP google-public-dns-a.google.com.domain > x220t.local.32371: 29524 NXDomain 0/1/0 (114)
    19:04:25.287550 IP6 fe80::120b:a9ff:fe0c:f638.mdns > ff02::fb.mdns: 0 PTR (QM)? 255.255.255.255.in-addr.arpa. (46)
    ^C19:04:25.287614 IP x220t.local.mdns > 224.0.0.251.mdns: 0 PTR (QM)? 255.255.255.255.in-addr.arpa. (46)

    6 packets captured
    50 packets received by filter
    0 packets dropped by kernel

Фильтр запросов по хосту
~~~~~~~~~~~~~~~~~~~~~~~~

Чтобы узнать получаемые или отправляемые пакеты от определенного хоста, необходимо его имя или IP-адрес указать после ключевого слова host:

.. no-code-block:: bash

    $ sudo tcpdump host readthedocs.org
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlan0, link-type EN10MB (Ethernet), capture size 262144 bytes
    19:08:24.734572 IP x220t.local.44169 > readthedocs.org.http: Flags [S], seq 1630487586, win 14600, options [mss 1460,sackOK,TS val 281681188 ecr 0,nop,wscale 7], length 0
    19:08:24.900671 IP readthedocs.org.http > x220t.local.44169: Flags [S.], seq 2780774205, ack 1630487587, win 14480, options [mss 1460,sackOK,TS val 1880995361 ecr 281681188,nop,wscale 9], length 0
    19:08:24.900718 IP x220t.local.44169 > readthedocs.org.http: Flags [.], ack 1, win 115, options [nop,nop,TS val 281681229 ecr 1880995361], length 0
    19:08:24.900812 IP x220t.local.44169 > readthedocs.org.http: Flags [P.], seq 1:733, ack 1, win 115, options [nop,nop,TS val 281681229 ecr 1880995361], length 732
    ...
      19:08:28.524595 IP readthedocs.org.https > x220t.local.37282: Flags [.], ack 2254, win 40, options [nop,nop,TS val 1880996266 ecr 281682094], length 0
    19:08:28.605826 IP x220t.local.37282 > readthedocs.org.https: Flags [.], ack 9767, win 296, options [nop,nop,TS val 281682155 ecr 1880996287], length 0
    ^C
    83 packets captured
    89 packets received by filter
    0 packets dropped by kernel

Фильтр по протоколу
~~~~~~~~~~~~~~~~~~~

.. no-code-block:: bash

    $ sudo tcpdump -n tcp

По назначению
~~~~~~~~~~~~~

Только те пакеты, которые адресованы хосту с IP 192.168.1.101

.. code-block:: bash

    $ sudo tcpdump -n 'src 192.168.1.101'

Показывает DNS запросы

.. no-code-block:: bash

    $ sudo tcpdump -n 'udp and dst port 53'
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlan0, link-type EN10MB (Ethernet), capture size 262144 bytes
    19:22:52.089174 IP 192.168.1.101.17166 > 8.8.8.8.53: 44241+ A? www.google.ru. (31)
    19:22:52.149972 IP 192.168.1.101.61715 > 8.8.8.8.53: 63972+ A? www.google.ru. (31)
    19:22:52.157017 IP 192.168.1.101.12023 > 8.8.8.8.53: 17412+ AAAA? www.google.ru. (31)
    19:22:52.860129 IP 192.168.1.101.1745 > 8.8.8.8.53: 59896+ A? ssl.gstatic.com. (33)
    19:22:52.860245 IP 192.168.1.101.4582 > 8.8.8.8.53: 28863+ AAAA? ssl.gstatic.com. (33)
    19:22:52.860388 IP 192.168.1.101.12181 > 8.8.8.8.53: 46772+ A? ssl.gstatic.com. (33)
    19:22:53.992159 IP 192.168.1.101.53803 > 8.8.8.8.53: 64496+ A? www.google.ru. (31)
    19:22:54.062859 IP 192.168.1.101.30447 > 8.8.8.8.53: 54230+ AAAA? www.google.ru. (31)
    ^C
    8 packets captured
    10 packets received by filter
    0 packets dropped by kernel

Пакеты между двумя хостами
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ищем хосты при помощи NetBIOS протокола.

.. seealso::

    * https://ru.wikipedia.org/wiki/NetBIOS


.. no-code-block:: bash

    $ nbtscan 192.168.1.0/24
    Doing NBT name scan for addresses from 192.168.1.0/24

    IP address       NetBIOS Name     Server    User             MAC address
    ------------------------------------------------------------------------------
    192.168.1.0     Sendto failed: Permission denied
    192.168.1.101    X220T            <server>  X220T            00:00:00:00:00:00
    192.168.1.23                      <server>                   00:00:00:00:00:00
    192.168.1.22     ARKASHA-PC       <server>  <unknown>        00:1b:fc:6c:c2:12
    192.168.1.255   Sendto failed: Permission denied

Или при помощи `nmap`

.. no-code-block:: bash

    $ nmap -sP 192.168.1.*

    Starting Nmap 6.46 ( http://nmap.org ) at 2015-02-02 20:56 YEKT
    Nmap scan report for 192.168.1.1
    Host is up (0.0068s latency).
    Nmap scan report for 192.168.1.20
    Host is up (0.018s latency).
    Nmap scan report for 192.168.1.21
    Host is up (0.016s latency).
    Nmap scan report for 192.168.1.22
    Host is up (0.028s latency).
    Nmap scan report for 192.168.1.24
    Host is up (0.017s latency).
    Nmap scan report for 192.168.1.26
    Host is up (0.032s latency).
    Nmap scan report for 192.168.1.28
    Host is up (0.0063s latency).
    Nmap scan report for 192.168.1.101
    Host is up (0.00020s latency).
    Nmap done: 256 IP addresses (8 hosts up) scanned in 4.28 seconds

Создаем трафик ICMP для хоста 192.168.1.23

.. no-code-block:: bash

    $ ping 192.168.1.23
    PING 192.168.1.23 (192.168.1.23) 56(84) bytes of data.
    64 bytes from 192.168.1.23: icmp_seq=1 ttl=64 time=1.90 ms
    64 bytes from 192.168.1.23: icmp_seq=2 ttl=64 time=1.27 ms
    64 bytes from 192.168.1.23: icmp_seq=3 ttl=64 time=1.28 ms
    64 bytes from 192.168.1.23: icmp_seq=4 ttl=64 time=1.23 ms
    ^C
    --- 192.168.1.23 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3003ms
    rtt min/avg/max/mdev = 1.236/1.423/1.900/0.279 ms

Смотрим пакеты

.. no-code-block:: bash

    $ sudo tcpdump 'src 192.168.1.101 and dst 192.168.1.23 and icmp'
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlan0, link-type EN10MB (Ethernet), capture size 262144 bytes
    19:36:45.340321 IP x220t.local > 192.168.1.23: ICMP echo request, id 10305, seq 1, length 64
    19:36:46.341472 IP x220t.local > 192.168.1.23: ICMP echo request, id 10305, seq 2, length 64
    19:36:47.342180 IP x220t.local > 192.168.1.23: ICMP echo request, id 10305, seq 3, length 64
    19:36:48.343557 IP x220t.local > 192.168.1.23: ICMP echo request, id 10305, seq 4, length 64
    ^C
    4 packets captured
    4 packets received by filter
    0 packets dropped by kernel

Без фильтрации, получим все пакеты. Например ARP и NetBIOS.

.. no-code-block:: bash

    $ sudo tcpdump 'src 192.168.1.101 and dst 192.168.1.23'
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlan0, link-type EN10MB (Ethernet), capture size 262144 bytes
    19:39:50.567837 ARP, Request who-has 192.168.1.23 tell x220t.local, length 28
    19:39:50.569144 IP x220t.local.netbios-ns > 192.168.1.23.netbios-ns: NBT UDP PACKET(137): QUERY; POSITIVE; RESPONSE; UNICAST
    19:39:55.517322 IP x220t.local > 192.168.1.23: ICMP echo request, id 10662, seq 1, length 64
    19:40:00.533322 ARP, Reply x220t.local is-at 10:0b:a9:0c:f6:38 (oui Unknown), length 28
    ^C
    4 packets captured
    4 packets received by filter
    0 packets dropped by kernel

Поиск в трафике
~~~~~~~~~~~~~~~

Ответы со статусом 200

.. no-code-block:: bash

    $ sudo tcpdump -n -A | grep -e '200 OK'
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlan0, link-type EN10MB (Ethernet), capture size 262144 bytes
    A).)...sHTTP/1.1 200 OK
    A).9...vHTTP/1.1 200 OK
    ^C508 packets captured
    508 packets received by filter
    0 packets dropped by kernel

Поиск паролей в трафике если он не использует шифрование.
Например если ввести логин и пароль в HTML форме.

.. image:: /_static/login_form.png

.. no-code-block:: bash
    :emphasize-lines: 24

    $ sudo tcpdump -l -A -i lo | egrep -i 'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd=|password=|pass:|user:|username:|password:|login:|pass |user ' --color=auto --line-buffered -B20
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on lo, link-type EN10MB (Ethernet), capture size 262144 bytes
    19:54:00.745538 IP localhost.6543 > localhost.58721: Flags [S.], seq 2085108079, ack 4286254343, win 43690, options [mss 65495,sackOK,TS val 282365190 ecr 282365190,nop,wscale 7], length 0
    E..<..@.@.<............a|H9o.{.......0.........
    ............
    19:54:00.745556 IP localhost.58721 > localhost.6543: Flags [.], ack 1, win 342, options [nop,nop,TS val 282365190 ecr 282365190], length 0
    E..4..@.@............a...{..|H9p...V.(.....
    ........
    19:54:00.745694 IP localhost.58721 > localhost.6543: Flags [P.], seq 1:708, ack 1, win 342, options [nop,nop,TS val 282365190 ecr 282365190], length 707
    E.....@.@............a...{..|H9p...V.......
    ........POST /sign_in HTTP/1.1
    Host: localhost:6543
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Referer: http://localhost:6543/login/
    Cookie: csrftoken=pVVycxJs2YaTCS5vpKTob0TINGsKjAM4; _LOCALE_=ru; _ga=GA1.1.1951453052.1420403120; connect.sid=s%3AnGU-04XqEDWudttY3CHI3LdUmEr__MYG.GF2fEjoSwB0bC99vfK%2FibenygTjwjRPLto948y7FSwU; beaker.session.id=27aa2050fff646b5bfe5cce56dae1472
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 53

    came_from=%2F&login=admin&password=123&submit=Sign+In
    ^C111 packets captured
    222 packets received by filter
    0 packets dropped by kernel

Wireshark
---------

.. seealso::

    * https://ru.wikipedia.org/wiki/Wireshark

Wireshark (ранее — Ethereal) — программа-анализатор трафика для компьютерных сетей Ethernet и некоторых других. Имеет графический пользовательский интерфейс.

Функциональность, которую предоставляет Wireshark, очень схожа с возможностями программы tcpdump, однако Wireshark имеет графический пользовательский интерфейс и гораздо больше возможностей по сортировке и фильтрации информации. Программа позволяет пользователю просматривать весь проходящий по сети трафик в режиме реального времени, переводя сетевую карту в неразборчивый режим.(promiscuous mode)

Просмотр только ICMP трафика в WireShark

.. image:: /_static/wireshark.png
    :align: center

mitmproxy
---------

.. seealso::

    * http://mitmproxy.org/index.html
