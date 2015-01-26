Протокол HTTP
=============

.. note:: Список ресурсов:

    * `HTTP: протокол, который каждый разработчик должен знать (часть 1) <http://ruseller.com/lessons.php?rub=28&id=1726>`_
    * `HTTP: протокол, который каждый разработчик должен знать (часть 2) <http://ruseller.com/lessons.php?rub=28&id=1777>`_
    * `Основа www: протокол HTTP <http://www.4stud.info/web-programming/protocol-http.html>`_
    * `Перевод документа RFC 2068 на русский язык <http://www.lib.ru/WEBMASTER/rfc2068/>`_
    * `Гипертекстный протокол HTTP <http://book.itep.ru/4/45/http4561.htm>`_
    * `Доклад от Yandex <https://events.yandex.ru/lib/talks/537/>`_

Протокол HTTP это основа Веба, через него передается основная часть веб трафика.
HTTP является протоколом передачи данных 4го (прикладного) уровня стека протоколов TCP/IP.

Изначально создавался для передачи гипертекстовых документов в формате HTML,
но сейчас используется для передачи любых данных.
Также может выступать в роли транспорта для других протоколов прикладного уровня,
например SOAP, XML-RPC, JSON-RPC, WebDAV.

HTTP обеспечивает общение между множеством хостов и клиентов.
Общение между хостом и клиентом происходит в два этапа: запрос и ответ. Клиент формирует HTTP запрос, в ответ на который сервер дает ответ (сообщение).

.. image:: /_static/http1-request-response.png
    :alt: HTTP запрос и ответ

URI
---

.. note:: Список ресурсов:

    * https://ru.wikipedia.org/wiki/URL
    * https://ru.wikipedia.org/wiki/URI

Основным объектом манипуляции в `HTTP` является ресурс, на который указывает `URI` (`Uniform Resource Identifier` – уникальный идентификатор ресурса) в запросе клиента. Основными ресурсами являются хранящиеся на сервере файлы, но ими могут быть и другие логические (напр. каталог на сервере) или абстрактные объекты (напр. ISBN). Протокол `HTTP` позволяет указать способ представления (кодирования) одного и того же ресурса по различным параметрам: mime-типу, языку и т. д. Благодаря этой возможности клиент и веб-сервер могут обмениваться двоичными данными, хотя данный протокол является текстовым.

Примеры URI:

::

    ftp://ftp.is.co.za/rfc/rfc1808.txt

    http://www.ietf.org/rfc/rfc2396.txt

    ldap://[2001:db8::7]/c=GB?objectClass?one

    mailto:John.Doe@example.com

    news:comp.infosystems.www.servers.unix

    tel:+1-816-555-1212

    telnet://192.0.2.16:80/

    urn:oasis:names:specification:docbook:dtd:xml:4.1.2

Структура URI
~~~~~~~~~~~~~

.. raw:: html

    <style>
        .red {color: red;}
        .green {color: green;}
        .blue {color: blue;}
        .yellow {color: #BB0;}
        .purple {color: purple;}
        .orange {color: orange;}
    </style>

.. role:: red
.. role:: green
.. role:: blue
.. role:: yellow
.. role:: purple
.. role:: orange

\|-----------------------------------------------------------------URI
------------------------------------------------------------------\|

\|--------------------------------URL------------------------------------\|
\|------------------------URN------------------------------\|

:red:`<схема>`://<логин>:<пароль>@<хост>:<порт>/<URL ‐ путь>?<параметры>#<якорь>

.. raw:: html

    <div class='red'>
        ws      <br/>
        ftp     <br/>
        http    <br/>
        https   <br/>
        file    <br/>
        mailto  <br/>
        xmpp
    </div>

<схема>://
:green:`<логин>:<пароль>`
@<хост>:<порт>/<URL ‐ путь>?<параметры>#<якорь>

.. raw:: html

    <div class='green' style='padding-left:105px'>
        user:123 <br/>
        user
    </div>

<схема>://<логин>:<пароль>
:blue:`@<хост>:<порт>`/<URL ‐ путь>?<параметры>#<якорь>

.. raw:: html

    <div class='blue' style='padding-left:220px'>
        localhost:8080  <br/>
        yandex.ru       <br/>
        213.180.204.11
    </div>

<схема>://<логин>:<пароль>@<хост>:<порт>
:yellow:`/<URL ‐ путь>`?<параметры>#<якорь>

.. raw:: html

    <div class='yellow' style='padding-left:320px'>
        somedir/somefile.htm
    </div>

<схема>://<логин>:<пароль>@<хост>:<порт>/<URL ‐ путь>
:purple:`?<параметры>`
#<якорь>

.. raw:: html

    <div class='purple' style='padding-left:430px'>
        text=foobar&from=fx3&lr=213
    </div>

<схема>://<логин>:<пароль>@<хост>:<порт>/<URL ‐ путь>?<параметры>
:orange:`#<якорь>`

.. raw:: html

    <div class='orange' style='padding-left:540px'>
        someanchor
    </div>

Пример якоря http://lectureswww.readthedocs.org/ru/latest/net/http.html#id2

Допустимые символы
~~~~~~~~~~~~~~~~~~

* Латинские буквы
* Цифры
* Специальные символы $-_.+!*'(),
* Зарезервированные символы ; /? :@=&

Символ ; можно использовать вместо &

::

    URI "http://host/?x=1&y=2"

    <a href="http://host/?x=1&#38;y=2">

    <a href="http://host/?x=1&amp;y=2">

Запрос
------

Ответ
-----

