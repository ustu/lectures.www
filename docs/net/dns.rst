DNS (система доменных имен)
===========================

.. seealso::

    * https://ru.wikipedia.org/wiki/DNS
    * http://book.itep.ru/4/44/dns_4412.htm
    * https://developer.mozilla.org/en-US/Learn/Understanding_domain_names

Доменное имя
------------

.. seealso::

    * `<https://ru.wikipedia.org/wiki/Доменное_имя>`_

Доменное имя — символьное имя, служащее для идентификации областей — единиц административной автономии в сети Интернет — в составе вышестоящей по иерархии такой области. Каждая из таких областей называется доменом. Общее пространство имён Интернета функционирует благодаря DNS — системе доменных имён. Доменные имена дают возможность адресации интернет-узлов и расположенных на них сетевых ресурсов (веб-сайтов, серверов электронной почты, других служб) в удобной для человека последовательности.


Примеры доменов
~~~~~~~~~~~~~~~

.. image:: /_static/DNS-names-ru.svg
    :width: 600px
    :align: center

0-й уровень

* \.

1-й уровень

* ru
* com
* org

2-й уровень

* ya.ru
* sql.ru

3-й уровень

* linux.org.ru
* ru.wikipedia.org
* lectureswww.readthedocs.org

Привязка к IP адресу
--------------------

.. seealso::

    * https://ru.wikipedia.org/wiki/BIND
    * https://ru.wikipedia.org/wiki/Hosts
    * https://ru.wikipedia.org/wiki/Dnsmasq
    * https://ru.wikipedia.org/wiki/Localhost

hosts — текстовый файл, содержащий базу данных доменных имен и используемый при их трансляции в сетевые адреса узлов. Запрос к этому файлу имеет приоритет перед обращением к DNS-серверам. В отличие от DNS, содержимое файла контролируется администратором компьютера.

Расположение:

В Unix ``/etc/hosts``

В Windows ``%SystemRoot%\\system32\\drivers\\etc\\hosts``

Пример файла hosts

::

    213.180.204.3   google.com
    127.0.0.1       localhost
    127.0.1.1       x220t
    10.0.0.1        server1
    10.0.0.2        postgres
    10.0.0.3        redis

localhost (так называемый, «локальный хост», по смыслу — этот компьютер) — в компьютерных сетях, стандартное, официально зарезервированное, доменное имя для частных IP-адресов (в диапазоне 127.0.0.1 — 127.255.255.255, RFC 2606). Для сети, состоящей только из одного компьютера, как правило, используется всего один адрес — 127.0.0.1, который устанавливается на специальный сетевой интерфейс «внутренней петли» (англ. loopback) в сетевом протоколе TCP/IP. В Unix-подобных системах данный интерфейс обычно именуется «loN», где N — число, либо просто «lo». При установке соединений в этой вырожденной «сети» присутствует только один компьютер, при этом сетевые протоколы выполняют функции протоколов межпроцессного взаимодействия.

Использование адреса 127.0.0.1 позволяет устанавливать соединение и передавать информацию для программ-серверов, работающих на том же компьютере, что и программа-клиент, независимо от конфигурации аппаратных сетевых средств компьютера (не требуется сетевая карта, модем, и прочее коммуникационное оборудование, интерфейс реализуется при помощи драйвера псевдоустройства в ядре операционной системы). Таким образом, для работы клиент-серверных приложений на одном компьютере не требуется изобретать дополнительные протоколы и дописывать программные модули.


.. image:: /_static/dns_request.png
   :align: center

Способы получения IP адреса по доменному имени
----------------------------------------------

**dig**

.. no-code-block:: bash

    $ dig lectureswww.readthedocs.org +nostats +nocomments +nocmd
    ; <<>> DiG 9.9.5-4.3ubuntu0.1-Ubuntu <<>> lectureswww.readthedocs.org +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;lectureswww.readthedocs.org.   IN      A
    lectureswww.readthedocs.org. 299 IN     A       162.209.114.75

**host**

.. no-code-block:: bash

    $ host lectureswww.readthedocs.org
    lectureswww.readthedocs.org has address 162.209.114.75
    lectureswww.readthedocs.org mail is handled by 20 alt1.aspmx.l.google.com.
    lectureswww.readthedocs.org mail is handled by 30 aspmx3.googlemail.com.
    lectureswww.readthedocs.org mail is handled by 10 aspmx.l.google.com.
    lectureswww.readthedocs.org mail is handled by 20 alt2.aspmx.l.google.com.
    lectureswww.readthedocs.org mail is handled by 30 aspmx2.googlemail.com.

.. no-code-block:: bash

    $ host 162.209.114.75
    75.114.209.162.in-addr.arpa domain name pointer readthedocs.org.

**ping**

.. no-code-block:: bash

    $ ping lectureswww.readthedocs.org
    PING lectureswww.readthedocs.org (162.209.114.75) 56(84) bytes of data.
    64 bytes from readthedocs.org (162.209.114.75): icmp_seq=1 ttl=46 time=186 ms
    64 bytes from readthedocs.org (162.209.114.75): icmp_seq=2 ttl=46 time=203 ms
    64 bytes from readthedocs.org (162.209.114.75): icmp_seq=3 ttl=46 time=442 ms
    ^C
    --- lectureswww.readthedocs.org ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2002ms
    rtt min/avg/max/mdev = 186.876/277.601/442.618/116.878 ms

**nslookup**

.. no-code-block:: bash

    $ nslookup lectureswww.readthedocs.org
    docs.org
    Server:         127.0.1.1
    Address:        127.0.1.1#53

    Non-authoritative answer:
    Name:   lectureswww.readthedocs.org
    Address: 162.209.114.75

**whois**

.. seealso::

    * https://ru.wikipedia.org/wiki/WHOIS

WHOIS (от англ. who is — «кто такой?») — сетевой протокол прикладного уровня, базирующийся на протоколе TCP (порт 43). Основное применение — получение регистрационных данных о владельцах доменных имён, IP-адресов и автономных систем.

Протокол подразумевает архитектуру «клиент-сервер» и используется для доступа к публичным серверам баз данных (БД) регистраторов IP-адресов и регистраторов доменных имён. Текущая версия этого протокола описана в RFC 3912. Чаще всего WHOIS-клиенты реализованы в виде консольных программ. Однако, поскольку для многих пользователей командная строка недоступна или неудобна, на основе консольных клиентов обычно создаются веб-формы, доступные пользователям на многих сайтах в Интернете. Кроме того, существуют WHOIS-клиенты и с графическим интерфейсом.

.. no-code-block:: bash

   $ whois ustu.ru
   % By submitting a query to RIPN's Whois Service
   % you agree to abide by the following terms of use:
   % http://www.ripn.net/about/servpol.html#3.2 (in Russian)
   % http://www.ripn.net/about/en/servpol.html#3.2 (in English)

   domain:        USTU.RU
   nserver:       ns2.ustu.ru. 93.88.182.2
   nserver:       ns.ustu.ru. 93.88.181.2
   state:         REGISTERED, DELEGATED, VERIFIED
   org:           UrFU
   registrar:     RU-CENTER-RU
   admin-contact: https://www.nic.ru/whois
   created:       1997.09.28
   paid-till:     2015.10.01
   free-date:     2015.11.01
   source:        TCI

   Last updated on 2015.02.25 11:51:31 MSK

TLD (Top-Level Domain). Некоторые Whois сервера
ничего не знают о доменах "ru."

.. no-code-block:: bash

    $ whois --host whois.pir.org ustu.ru
    TLD "ru" is not supported

Что бы посмотреть какой сервер используется,
нужно добавить опцию "--verbose"

.. no-code-block:: bash
   :linenos:
   :emphasize-lines: 2

   $ whois --verbose ustu.ru
   Используется сервер whois.tcinet.ru.
   Строка запроса: "ustu.ru"

   % By submitting a query to RIPN's Whois Service
   % you agree to abide by the following terms of use:
   % http://www.ripn.net/about/servpol.html#3.2 (in Russian)
   % http://www.ripn.net/about/en/servpol.html#3.2 (in English).

   domain:        USTU.RU
   nserver:       ns2.ustu.ru. 93.88.182.2
   nserver:       ns.ustu.ru. 93.88.181.2
   state:         REGISTERED, DELEGATED, VERIFIED
   org:           UrFU
   registrar:     RU-CENTER-RU
   admin-contact: https://www.nic.ru/whois
   created:       1997.09.28
   paid-till:     2015.10.01
   free-date:     2015.11.01
   source:        TCI

   Last updated on 2015.02.25 12:01:33 MSK
