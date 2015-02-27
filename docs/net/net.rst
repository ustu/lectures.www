Сети
====

.. seealso::

    * `Каналы передачи данных <http://book.itep.ru/1/intro1.htm>`_
    * `<https://developer.mozilla.org/en-US/Learn/How_the_Internet_works>`_

**World Wide Web (WWW, W3)** — гипертекстовая (гипермедиа) система,
предназначенная для интеграции различных сетевых ресурсов в единое информационное
пространство. Всемирную паутину образуют миллионы веб-серверов сети Интернет,
расположенных по всему миру. Веб-сервер является программой, запускаемой на
подключённом к сети компьютере и использующей обычно
протокол **HTTP** для передачи данных.
В качестве клиента чаще всего выступает программа-браузер
(**Microsoft Internet Explorer**, **Mozilla FireFox** и другие).
Клиент обращается по сети к серверу, который обрабатывает
запрос и возвращает ответ в виде `HTML` кода. Связь с сервером чаще всего
происходит посредством протокола **HTTP** через **TCP/IP** сети.

.. рисунок клиент-серверной архитектуры

Распределение протоколов по уровням модели **TCP/IP**

.. raw:: html

    <table>
    <tr>
        <td style="padding: 0 15px 0 0">4</td>
        <td style="border:1px solid red;padding: 20px 10px 20px;">
            Прикладной
        </td>
        <td style="padding: 0 0 0 10px">
            HTTP, FTP, DNS, Telnet, SSH
        </td>
    </tr>
    <tr>
        <td>3</td>
        <td style="border:1px solid red;padding: 20px 10px 20px;">
            Транспортный
        </td>
        <td style="padding: 0 0 0 10px">
            TCP, UDP
        </td>
    </tr>
    <tr>
        <td>2</td>
        <td style="border:1px solid red;padding: 20px 10px 20px;">
            Сетевой
        </td>
        <td style="padding: 0 0 0 10px">
            IP, ICMP
        </td>
    </tr>
    <tr>
        <td>1</td>
        <td style="border:1px solid red;padding: 20px 10px 20px;">
            Доступа к среде
        </td>
        <td style="padding: 0 0 0 10px">
            Ethernet, Token Ring, E1
        </td>
    </tr>
    </table>

Передача данных по TCP/IP

.. image:: /_static/TCP_IP.svg
   :align: center
   :width: 800px

В курсе Веб-программирования нас будут интересовать в основном протоколы 4-го
уровня стека протоколов TCP/IP. Остальные протоколы вы изучите на курсе "Каналы передачи
данных".
