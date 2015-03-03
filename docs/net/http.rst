.. _http-protocol:

HTTP протокол
=============

.. seealso::

    * `HTTP: протокол, который каждый разработчик должен знать (часть 1) <http://ruseller.com/lessons.php?rub=28&id=1726>`_
    * `HTTP: протокол, который каждый разработчик должен знать (часть 2) <http://ruseller.com/lessons.php?rub=28&id=1777>`_
    * `Основа www: протокол HTTP <http://www.4stud.info/web-programming/protocol-http.html>`_
    * `Перевод документа RFC 2068 на русский язык <http://www.lib.ru/WEBMASTER/rfc2068/>`_
    * `Гипертекстный протокол HTTP <http://book.itep.ru/4/45/http4561.htm>`_
    * `Доклад от Yandex <https://events.yandex.ru/lib/talks/537/>`_

Протокол `HTTP` это основа Веба, через него передается основная часть веб трафика.
HTTP является протоколом передачи данных 4го (прикладного) уровня стека протоколов `TCP/IP`.

Изначально создавался для передачи гипертекстовых документов в формате HTML,
но сейчас используется для передачи любых данных.
Также может выступать в роли транспорта для других протоколов прикладного уровня,
например `SOAP`, `XML-RPC`, `JSON-RPC`, `WebDAV`.

HTTP обеспечивает общение между множеством хостов и клиентов.
Общение между хостом и клиентом происходит в два этапа: запрос и ответ. Клиент формирует `HTTP` запрос, в ответ на который сервер дает ответ (сообщение).

.. image:: /_static/http1-request-response.png
    :alt: HTTP запрос и ответ

URI
---

.. note:: Список ресурсов:

    * https://ru.wikipedia.org/wiki/URL
    * https://ru.wikipedia.org/wiki/URI
    * `URI,URL,URN <http://handynotes.ru/2009/09/uri-url-urn.html>`_

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

.. seealso::
   * http://www.ietf.org/rfc/rfc3986.txt

::

      foo://example.com:8042/over/there?name=ferret#nose
      \_/   \______________/\_________/ \_________/ \__/
       |           |            |            |        |
     схема   имя(IP) и порт    путь        запрос   элемент
       |   _____________________|__
      / \ /                        \
      urn:example:animal:ferret:nose


.. raw:: html

    <style>
        .red {color: red;}
        .green {color: green;}
        .blue {color: blue;}
        .yellow {color: #BB0;}
        .purple {color: purple;}
        .orange {color: orange;}

        hr.red { background-color: red;}
        hr.blue { background-color: blue;}
        hr.green { background-color: green;}
        hr.yellow { background-color: #BB0;}
        hr.purple { background-color: purple;}
        hr.orange { background-color: orange;}

        .short_line {height:4px;float:left;width:100px;}
    </style>

.. role:: red
.. role:: green
.. role:: blue
.. role:: yellow
.. role:: purple
.. role:: orange

\|-----------------------------------------------------------------URI
-------------------------------------------------------------------\|

\|--------------------------------URL------------------------------------\|
\|--------------------URN------------------\|

:red:`<схема>`://<логин>:<пароль>@<хост>:<порт>/<URN ‐ путь>?<параметры>#<якорь>

.. raw:: html

    <div class='red' style='margin-top:-15px'>
        ws      <br/>
        ftp     <br/>
        http    <br/>
        https   <br/>
        file    <br/>
        mailto  <br/>
        xmpp
    </div>
    <br/>

<схема>://
:green:`<логин>:<пароль>`
@<хост>:<порт>/<URN ‐ путь>?<параметры>#<якорь>

.. raw:: html

    <div class='green' style='padding-left:105px;margin-top:-15px'>
        user:123 <br/>
        user
    </div>
    <br/>

<схема>://<логин>:<пароль>
:blue:`@<хост>:<порт>`/<URN ‐ путь>?<параметры>#<якорь>

.. raw:: html

    <div class='blue' style='padding-left:260px;margin-top:-15px'>
        localhost:8080  <br/>
        yandex.ru       <br/>
        213.180.204.11
    </div>
    <br/>

<схема>://<логин>:<пароль>@<хост>:<порт>
:yellow:`/<URN ‐ путь>`?<параметры>#<якорь>

.. raw:: html

    <div class='yellow' style='padding-left:360px;margin-top:-15px''>
        somedir/somefile.htm
    </div>
    <br/>

<схема>://<логин>:<пароль>@<хост>:<порт>/<URN ‐ путь>
:purple:`?<параметры>`
#<якорь>

.. raw:: html

    <div class='purple' style='padding-left:500px;margin-top:-15px''>
        text=foobar&from=fx3&lr=213
    </div>
    <br/>

<схема>://<логин>:<пароль>@<хост>:<порт>/<URN ‐ путь>?<параметры>
:orange:`#<якорь>`

.. raw:: html

    <div class='orange' style='padding-left:650px;margin-top:-15px''>
        someanchor
    </div>

Пример якоря http://lectureswww.readthedocs.org/ru/latest/net/http.html#id2

Пара <хост>:<порт> называется `INET SOCKET`, например:

    * 127.0.0.1:6543
    * yandex.ru:80
    * 192.168.0.13:22

HTTP по умолчанию использует порт 80, поэтому его часто не указывают.


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

Форматы сообщений запроса/ответа
--------------------------------

На следующем изображении вы можете увидеть схематично оформленный процесс отправки запроса клиентом, обработка и отправка ответа сервером.

.. image:: /_static/http1-req-res-details.png
    :alt: HTTP запрос и ответ

Давайте посмотрим на структуру передаваемого сообщения через HTTP:

::

    message = <Стартовая строка>
              *(<Заголовки>)
              CRLF
              [<Тело сообщения>]

Или

::

    <Метод> <URI> HTTP/1.1
    <Заголовки>
        Referer: http://www.yandex.ru/
    </Заголовки>

    <Тело сообщения>
        param=value&a=1&b=2&c=3
    </Тело сообщения>

Между заголовком и телом сообщения должна обязательно присутствовать пустая строка. Заголовков может быть несколько.

Пример запроса:

::

   GET /ru/latest/net/http.html HTTP/1.1
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
   Accept-Language: en-US,en;q=0.5
   Connection: keep-alive
   Host: lectureswww.readthedocs.org
   User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0

Ответ:

::

   HTTP/1.1 200 OK
   Server: nginx/1.4.6 (Ubuntu)
   Date: Mon, 26 Jan 2015 16:54:33 GMT
   Content-Type: text/html
   Content-Length: 48059
   Last-Modified: Mon, 26 Jan 2015 16:22:21 GMT
   Connection: keep-alive
   Vary: Accept-Encoding
   ETag: "54c669bd-bbbb"
   X-Served: Nginx
   X-Subdomain-TryFiles: True
   X-Deity: hydra-lts
   Accept-Ranges: bytes


   <!DOCTYPE html>
   <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
   <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ...



Стартовая строка запроса
~~~~~~~~~~~~~~~~~~~~~~~~

для HTTP/0.9

::

    GET <URI>

::

    GET /foo/bar

для HTTP/1.0-1.1

::

    <метод> <URI> HTTP/<версия>

::

    GET /foo/bar2 HTTP/1.1

Методы
******

С помощью URL, мы определяем точное название хоста, с которым хотим общаться, однако какое действие нам нужно совершить, можно сообщить только с помощью HTTP метода. Конечно же существует несколько видов действий, которые мы можем совершить. В HTTP реализованы самые нужные, подходящие под нужды большинства приложений.

Существующие методы:

**GET**: получить доступ к существующему ресурсу. В URL перечислена вся необходимая информация, чтобы сервер смог найти и вернуть в качестве ответа искомый ресурс.

**POST**: используется для создания нового ресурса. POST запрос обычно содержит в себе всю нужную информацию для создания нового ресурса.

**PUT**: обновить текущий ресурс. PUT запрос содержит обновляемые данные.

**DELETE**: служит для удаления существующего ресурса.

Данные методы самые популярные и чаще всего используются различными инструментами и фрэймворками. В некоторых случаях, PUT и DELETE запросы отправляются посредством отправки POST, в содержании которого указано действие, которое нужно совершить с ресурсом: создать, обновить или удалить.

Также HTTP поддерживает и другие методы:

**HEAD**: аналогичен GET. Разница в том, что при данном виде запроса не передаётся сообщение. Сервер получает только заголовки. Используется, к примеру, для того чтобы определить, был ли изменён ресурс.

**TRACE**: во время передачи запрос проходит через множество точек доступа и прокси серверов, каждый из которых вносит свою информацию: IP, DNS. С помощью данного метода, можно увидеть всю промежуточную информацию.

**OPTIONS**: используется для определения возможностей сервера, его параметров и конфигурации для конкретного ресурса.

.. note:: POST vs GET

   * http://phpfaq.ru/na_tanke#http

   Определить, какой способ следует применять, очень просто. Если форма служит для запроса некой информации, например - при поиске, то ее следует отправлять методом GET. Чтобы можно было обновлять страницу, можно было поставить закладку и или послать ссылку другу. Если же в результате отправки формы данные записываются или изменяются на сервере, то следует их отправлять методом POST, причем обязательно после обработки формы надо перенаправить браузер методом GET. Так же, POST может понадобиться, если на сервер надо передать большой объём данных (у GET он сильно ограничен), а так же, если не следует "светить" передаваемые данные в адресной строке (при вводе логина и пароля, например).

Метод GET
*********

::

    GET /index.php?param=value&a=1&b=2&c=3 HTTP/1.1
    <Заголовки>

Метод POST
**********

::

    POST /index.php HTTP/1.1
    <Заголовки>

    <Тело сообщения>
        param=value&a=1&b=2&c=3
    </Тело сообщения>

Стартовая строка ответа
~~~~~~~~~~~~~~~~~~~~~~~

::

    HTTP/<версия> <код состояния> <пояснение>

::

    HTTP/1.0 200 OK

Коды состояний
**************

В ответ на запрос от клиента, сервер отправляет ответ,
который содержит, в том числе, и код состояния.
Данный код несёт в себе особый смысл для того,
чтобы клиент мог отчётливей понять, как интерпретировать ответ:

**1xx**: Информационные сообщения

Набор этих кодов был введён в HTTP/1.1.
Сервер может отправить запрос вида: Expect: 100-continue, что означает,
что клиент ещё отправляет оставшуюся часть запроса.
Клиенты, работающие с HTTP/1.0 игнорируют данные заголовки.

**2xx**: Сообщения об успехе

Если клиент получил код из серии `2xx`, то запрос ушёл успешно.
Самый распространённый вариант - это `200 OK`.
При GET запросе, сервер отправляет ответ в теле сообщения.
Также существуют и другие возможные ответы:

    * **202** Accepted: запрос принят, но может не содержать ресурс в ответе. Это полезно для асинхронных запросов на стороне сервера. Сервер определяет, отправить ресурс или нет.
    * **204** No Content: в теле ответа нет сообщения.
    * **205** Reset Content: указание серверу о сбросе представления документа.
    * **206** Partial Content: ответ содержит только часть контента. В дополнительных заголовках определяется общая длина контента и другая инфа.

**3xx**: Перенаправление

Своеобразное сообщение клиенту о необходимости совершить ещё одно действие.
Самый распространённый вариант применения: перенаправить клиент на другой адрес.

    * **301** Moved Permanently: ресурс теперь можно найти по другому URL адресу.
    * **303** See Other: ресурс временно можно найти по другому URL адресу. Заголовок Location содержит временный URL.
    * **304** Not Modified: сервер определяет, что ресурс не был изменён и клиенту нужно задействовать закэшированную версию ответа. Для проверки идентичности информации используется ETag (хэш Сущности - Enttity Tag);

**4xx**: Клиентские ошибки

Данный класс сообщений используется сервером, если он решил, что запрос был отправлен с ошибкой. Наиболее распространённый код: `404 Not Found`. Это означает, что ресурс не найден на сервере. Другие возможные коды:

    * **400** Bad Request: вопрос был сформирован неверно.
    * **401** Unauthorized: для совершения запроса нужна аутентификация. Информация передаётся через заголовок Authorization.
    * **403** Forbidden: сервер не открыл доступ к ресурсу.
    * **405** Method Not Allowed: неверный HTTP метод был задействован для того, чтобы получить доступ к ресурсу.
    * **409** Conflict: сервер не может до конца обработать запрос, т.к. пытается изменить более новую версию ресурса. Это часто происходит при PUT запросах.

**5xx**: Ошибки сервера

Ряд кодов, которые используются для определения ошибки сервера при обработке запроса. Самый распространённый: `500 Internal Server Error`. Другие варианты:

    * **501** Not Implemented: сервер не поддерживает запрашиваемую функциональность.
    * **503** Service Unavailable: это может случиться, если на сервере произошла ошибка или он перегружен. Обычно в этом случае, сервер не отвечает, а время, данное на ответ, истекает.

Заголовки HTTP
~~~~~~~~~~~~~~

.. note::

    `<https://ru.wikipedia.org/wiki/Список_заголовков_HTTP>`_

Между заголовком и телом сообщения должна обязательно присутствовать пустая строка.

Заголовков может быть несколько.

Все необходимые для функционирования HTTP заголовки описаны в основных RFC документах.
Если не хватает существующих, то можно вводить свои.
Традиционно к именам таких дополнительных заголовков добавляют префикс «X-»
для избежания конфликта имён с возможно существующими.
Например, как в заголовках X-Powered-By или X-Cache.
Некоторые разработчики используют свои индивидуальные префиксы.
Примерами таких заголовков могут служить Ms-Echo-Request и Ms-Echo-Reply,
введённые корпорацией Microsoft для расширения WebDAV.

Пример:

.. seealso::

   * https://ru.wikipedia.org/wiki/Chunked_transfer_encoding

.. raw:: html

    <div class='blue'>Основные заголовки</div>
    <div class='green'>Заголовки ответа</div>
    <div class='orange'> Заголовки сущности</div>
    <br/>
    <div style='background:lightgray;width:100%'>
        HTTP/1.1 200 OK
        <div class='blue'>
            Date: Mon, 17 Sep 2012 13:05:11 GMT
            <br/>Transfer-Encoding: chunked
            <br/>Connection: keep-alive
            <br/>Pragma: no-cache
            <br/>Cache-Control: no-cache, no-store, max-age=0, must-revalidate
        </div>
        <div class='green'>
            Server: nginx
            <br/>Vary: X-Real-SSL-Protocol
        </div>
        <div class='orange'>
            Content-Type: text/html; charset=UTF-8
            <br/>Expires: Mon, 17 Sep 2012 13:05:11 GMT
            <br/>Content-Encoding: gzip
        </div>
    </div>

Основные заголовки
******************

.. note::

    http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.5

General Headers («Основные заголовки») — должны включаться в любое сообщение клиента и сервера. Большая часть из них являются обязательными.

::

    Cache-Control
    Connection
    Date
    Pragma
    Trailer
    Transfer-Encoding
    Upgrade
    Via
    Warning

Заголовок **Via** используется в запросе типа TRACE,
и обновляется всеми прокси-серверами.

Заголовок **Pragma** используется для перечисления собственных заголовков. К примеру, Pragma: no-cache - это то же самое, что Cache-Control: no-cache. Подробнее об этом поговорим во второй части.

Заголовок **Date** используется для хранения даты и времени запроса/ответа.

Заголовок **Upgrade** используется для изменения протокола.

**Transfer-Encoding** предназначается для разделения ответа
на несколько фрагментов с помощью Transfer-Encoding: chunked.
Это нововведение версии HTTP/1.1.

Заголовки запроса
*****************

.. note::

    http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5.3

Request Headers («Заголовки запроса») — используются только в запросах клиента.

::

    Accept
    Accept-Charset
    Accept-Encoding
    Accept-Language
    Authorization
    Expect
    From
    Host
    If-Match
    If-Modified-Since
    If-None-Match
    If-Range
    If-Unmodified-Since
    Max-Forwards
    Proxy-Authorization
    Range
    Referer
    TE
    User-Agent

Заголовки ответа
****************

.. note::

    http://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html#sec6.2

Response Headers («Заголовки ответа») — только для ответов от сервера.

::

    Accept-Ranges
    Age
    ETag
    Location
    Proxy-Authenticate
    Retry-After
    Server
    Vary
    WWW-Authenticate

Заголовки сущности
******************

.. note::

    http://www.w3.org/Protocols/rfc2616/rfc2616-sec7.html#sec7.1

::

    Allow
    Content-Encoding
    Content-Language
    Content-Length
    Content-Location
    Content-MD5
    Content-Range
    Content-Type
    Expires
    Last-Modified

Entity Headers («Заголовки сущности») — В заголовках сущностей передаётся мета-информация контента.

Все заголовки с префиксом Content- предоставляют информацию о структуре, кодировке и размере тела сообщения.

Заголовок Expires содержит время и дату истечения сущности. Значение “never expires” означает время + 1 код с текущего момента. Last-Modified содержит время и дату последнего изменения сущности.

Нестандартные заголовки
***********************

X-Frame-Options

::

    X-Frame-Options: DENY;
    //запретит загрузку через <iframe>

::

    X-Frame-Options: SAMEORIGIN;
    //разрешит загрузку через <iframe>  но только если и <iframe>,
    и страница, его загружающая, находятся на одном домене

X-Requested-With

::

    X-Requested-With: XMLHttpRequest
    // используется для идентификации ajax запросов

Пасхалки

::

    // используются чтобы пошутить =)

    X-Awesome: If you found this header please email us about a writing job

    X-Konkurentam: Preved

    X-ServerNickName: Wolverine

Cookie
------

.. note::

    * https://ru.wikipedia.org/wiki/Magic_cookie
    * https://ru.wikipedia.org/wiki/HTTP_cookie

«Волшебное печенье» (magic cookie) — это небольшой набор данных, передаваемых одной программой другой программе. Содержимое куки, как правило, не значимо для получателя и не интерпретируется до тех пор, пока получатель не вернёт куки обратно отправителю или другой программе.

В реальной жизни куки можно сравнить с номерком в гардеробе: номерок не имеет собственной ценности, но он позволяет получить взамен правильное пальто.

Куки могут использоваться для идентификации в компьютерных приложениях. Например, при посещении веб-сайта серверное приложение может оставить на компьютере посетителя HTTP-куки для аутентификации клиента при его возвращении на сайт. Куки являются компонентом наиболее общего метода аутентификации, используемого в X Window System.

Некоторые куки (например, в протоколе HTTP) могут иметь цифровую подпись или могут быть зашифрованы, чтобы злоумышленники не могли подделать и передать их отправителю для получения несанкционированного доступа.

Пример HTTP в браузере
----------------------

Открываем браузер и пишем адрес веб ресурса (URI)

.. image:: /_static/http.example.mozzila.png
    :alt: Стартовое окно браузера
    :align: center
    :width: 800px

Браузер генерирует строку запроса и отправляет его на сервер

::

    GET /ru/latest/net/http.html HTTP/1.1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.5
    Connection: keep-alive
    Host: lectureswww.readthedocs.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0

.. image:: /_static/http_request.svg
    :alt: HTTP запрос
    :align: center
    :width: 800px

Сервер получает текст запроса, обрабатывает его, формирует текст ответа
и отправляет его клиенту.

::

    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Mon, 26 Jan 2015 16:54:33 GMT
    Content-Type: text/html
    Content-Length: 48059
    Last-Modified: Mon, 26 Jan 2015 16:22:21 GMT
    Connection: keep-alive
    Vary: Accept-Encoding
    ETag: "54c669bd-bbbb"
    X-Served: Nginx
    X-Subdomain-TryFiles: True
    X-Deity: hydra-lts
    Accept-Ranges: bytes



    <!DOCTYPE html>
    <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Протокол HTTP &mdash; Документация Основы Веб-программирования 0.0.0</title>

      <link href='https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic|Roboto+Slab:400,700|Inconsolata:400,700' rel='stylesheet' type='text/css'>

        <link rel="stylesheet" href="https://media.readthedocs.org/css/sphinx_rtd_theme.css" type="text/css" />

        <link rel="stylesheet" href="https://media.readthedocs.org/css/readthedocs-doc-embed.css" type="text/css" />

        <link rel="top" title="Документация Основы Веб-программирования 0.0.0" href="../index.html"/>
            <link rel="up" title="Каналы передачи данных" href="index.html"/>
            <link rel="next" title="Сетевое программирование" href="../www.sync/codding.net.html"/>
            <link rel="prev" title="Сети" href="net.html"/>

    <!-- RTD Extra Head -->
    <!--
    Read the Docs is acting as the canonical URL for your project.
    If you want to change it, more info is available in our docs:
      http://docs.readthedocs.org/en/latest/canonical.html
    -->
    <link rel="canonical" href="http://lectureswww.readthedocs.org/ru/latest/net/http.html" />

    <script type="text/javascript">
    ....


      </script>
    </body>
    </html>

.. image:: /_static/http_responce.svg
    :alt: HTTP ответ
    :align: center
    :width: 800px

Пример HTTP в консоле (telnet)
------------------------------

.. note::

    https://ru.wikipedia.org/wiki/Telnet

В этом примере сделаем все то же самое, что и в предыдущем.
Только отправлять HTTP запрос будем через протокол TELNET.

.. code-block:: html

    $ telnet readthedocs.org 80
    Trying 162.209.114.75...
    Connected to readthedocs.org.
    Escape character is '^]'.
    GET /ru/latest/net/http.html HTTP/1.1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Connection: keep-alive
    Host: lectureswww.readthedocs.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0

    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Mon, 26 Jan 2015 16:54:33 GMT
    Content-Type: text/html
    Content-Length: 48059
    Last-Modified: Mon, 26 Jan 2015 16:22:21 GMT
    Connection: keep-alive
    Vary: Accept-Encoding
    ETag: "54c669bd-bbbb"
    X-Served: Nginx
    X-Subdomain-TryFiles: True
    X-Deity: hydra-lts
    Accept-Ranges: bytes



    <!DOCTYPE html>
    <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Протокол HTTP &mdash; Документация Основы Веб-программирования 0.0.0</title>

      <link href='https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic|Roboto+Slab:400,700|Inconsolata:400,700' rel='stylesheet' type='text/css'>

        <link rel="stylesheet" href="https://media.readthedocs.org/css/sphinx_rtd_theme.css" type="text/css" />

        <link rel="stylesheet" href="https://media.readthedocs.org/css/readthedocs-doc-embed.css" type="text/css" />

        <link rel="top" title="Документация Основы Веб-программирования 0.0.0" href="../index.html"/>
            <link rel="up" title="Каналы передачи данных" href="index.html"/>
            <link rel="next" title="Сетевое программирование" href="../www.sync/codding.net.html"/>
            <link rel="prev" title="Сети" href="net.html"/>

    <!-- RTD Extra Head -->
    <!--
    Read the Docs is acting as the canonical URL for your project.
    If you want to change it, more info is available in our docs:
      http://docs.readthedocs.org/en/latest/canonical.html
    -->
    <link rel="canonical" href="http://lectureswww.readthedocs.org/ru/latest/net/http.html" />

    <script type="text/javascript">
    ....


      </script>
    </body>
    </html>Connection closed by foreign host.


Пример HTTP в firebug
---------------------

.. note::

    http://getfirebug.com/

FireBug - это плагин браузера FireFox для веб разработчиков.
Запускается по клавише <F12>.

Заголовки запроса и ответа в FireBug'е из предыдущего примера.

.. image:: /_static/firebug1.png
    :alt: Firebug
    :align: center
    :width: 800px

Тело ответа находится в отдельной вкладке.

.. image:: /_static/firebug2.png
    :alt: Firebug
    :align: center
    :width: 800px
