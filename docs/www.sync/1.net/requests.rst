HTTP Запросы/Ответы на Python
=============================

httplib
-------

.. note::

    * https://docs.python.org/2/library/httplib.html
    * https://docs.python.org/3/library/http.client.html

httplib представляет собой простую обертку вокруг модуля socket,
которая обеспечивает наибольший контроль при обращении к web-сайту.

Отправка GET запроса.

.. code-block:: python

    import httplib
    conn = httplib.HTTPConnection("lectureswww.readthedocs.org")
    conn.request("GET", "/ru/latest/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()
    conn.request("GET", "/parrot.spam")
    r2 = conn.getresponse()
    print(r2.status, r2.reason)

    data2 = r2.read()
    conn.close()

.. code-block:: bash

    200 OK
    404 OK

В переменных data1, data2 хранится тело ответа.

POST запрос

.. code-block:: python

    import httplib
    import urllib

    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)

    data = response.read()
    print(data)

    conn.close()

.. no-code-block:: bash

    302 Found
    Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>

urllib
------

.. note::

    * `Лекции Р. Сузи <http://www.wiki.intuit.ru/wiki/Курсы/Язык_программирования_Python/Лекция_9:_Сетевые_приложения_на_Python>`_
    * https://docs.python.org/2/library/urllib.html

.. code-block:: python

   import urllib
   doc = urllib.urlopen("http://lectureswww.readthedocs.org").read()
   print(doc[:350])

.. code-block:: html

    <!DOCTYPE html>
    <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Основы Веб-программирования &mdash; Документ

Функция urllib.urlopen() создает файлоподобный объект, который читает методом read(). Другие методы этого объекта: readline(), readlines(), fileno(), close() работают как и у обычного файла, а также есть метод info(), который возвращает соответствующий полученному с сервера Message-объект.

Этот объект можно использовать для получения дополнительной информации:

.. code-block:: python

    import urllib
    doc = urllib.urlopen("http://lectureswww.readthedocs.org")
    print(doc.info())

.. no-code-block:: python

    Server: nginx/1.4.6 (Ubuntu)
    X-Deity: chimera-lts
    Vary: Accept-Encoding
    X-Served: Nginx
    Content-Type: text/html
    Date: Thu, 05 Feb 2015 13:30:41 GMT
    Accept-Ranges: bytes
    ETag: "54c74bc0-62a2"
    Connection: close
    X-Subdomain-TryFiles: True
    Last-Modified: Tue, 27 Jan 2015 08:26:40 GMT
    Content-Length: 25250

С помощью функции urllib.urlopen() можно делать и более сложные вещи, например, передавать web-серверу данные формы.
Как известно, данные заполненной web-формы могут быть переданы на web-сервер с использованием метода GET или метода POST.
Метод GET связан с кодированием всех передаваемых параметров после знака "?" в URL, а при методе POST данные передаются в теле HTTP-запроса.

Оба варианта передачи представлены ниже:

.. code-block:: python

    import urllib

    data = {"s": "Веб программирование"}
    enc_data = urllib.urlencode(data)

    # GET запрос
    f = urllib.urlopen("http://nigma.ru/" + "?" + enc_data)
    print(f.read())

    # POST запрос
    f = urllib.urlopen("http://nigma.ru/", enc_data)
    print(f.read())

В некоторых случаях данные имеют повторяющиеся имена. В этом случае в качестве параметра urllib.urlencode() можно использовать вместо словаря последовательность пар имя-значение:

.. code-block:: python

    import urllib
    data = [("n", "1"), ("n", "3"), ("n", "4"), ("button", "Привет"),]
    enc_data = urllib.urlencode(data)
    print(enc_data)

::

    n=1&n=3&n=4&button=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82

Модуль urllib позволяет загружать web-объекты через прокси-сервер. Если ничего не указывать, будет использоваться прокси-сервер, который был задан принятым в конкретной ОС способом. В Unix прокси-серверы задаются в переменных окружения http_proxy, ftp_proxy и т.п., в Windows прокси-серверы записаны в реестре, а в Mac OS они берутся из конфигурации Internet. Задать прокси-сервер можно и как именованный параметр proxies к urllib.urlopen():

.. code-block:: python

   # Использовать указанный прокси
   proxies = {'http': 'http://www.proxy.com:3128'}
   f = urllib.urlopen(some_url, proxies=proxies)

   # Не использовать прокси
   f = urllib.urlopen(some_url, proxies={})

   # Использовать прокси по умолчанию
   f = urllib.urlopen(some_url, proxies=None)
   f = urllib.urlopen(some_url)

urllib2
-------

.. note::

    * https://docs.python.org/3.5/howto/urllib2.html
    * https://docs.python.org/2/howto/urllib2.html
    * http://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/

Функциональности модулей urllib и urlparse хватает для большинства задач, которые решают сценарии на Python как web-клиенты. Тем не менее, иногда требуется больше. На этот случай можно использовать модуль для работы с протоколом HTTP - httplib - и создать собственный класс для HTTP-запросов (в лекциях модуль httplib не рассматривается). Однако вполне вероятно, что нужная функциональность уже имеется в модуле urllib2.

Пример запроса

.. code-block:: python

    import urllib2
    response = urllib2.urlopen('http://lectureswww.readthedocs.org/')
    print(response.info())
    print
    print(response.info()['server'])
    print
    print(response.read()[:350])

.. no-code-block:: bash

    Server: nginx/1.4.6 (Ubuntu)
    X-Deity: asgard-lts
    Vary: Accept-Encoding
    X-Served: Nginx
    Content-Type: text/html
    Date: Fri, 06 Feb 2015 10:09:07 GMT
    Accept-Ranges: bytes
    ETag: "54c74bc0-62a2"
    Connection: close
    X-Subdomain-TryFiles: True
    Last-Modified: Tue, 27 Jan 2015 08:26:40 GMT
    Content-Length: 25250


    nginx/1.4.6 (Ubuntu)



    <!DOCTYPE html>
    <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Основы Веб-программирования &mdash; Документ

.. code-block:: python

    import urllib2
    response = urllib2.urlopen('http://lectureswww.readthedocs.org/')
    print("Response:", response)

    # Get the URL. This gets the real URL.
    print("The URL is: ", response.geturl())

    # Getting the code
    print("This gets the code: ", response.code)

    # Get the Headers.
    # This returns a dictionary-like object that describes the page fetched,
    # particularly the headers sent by the server
    print("The Headers are: ", response.info())

    # Get the date part of the header
    print("The Date is: ", response.info()['date'])

    # Get the server part of the header
    print("The Server is: ", response.info()['server'])

    # Get all data
    html = response.read()
    print("Get all data: ", html[:350])

    # Get only the length
    print("Get the length :", len(html))

    # Showing that the file object is iterable
    for line in response:
        print(line.rstrip())


.. no-code-block:: bash

    Response: <addinfourl at 140390167715208 whose fp = <socket._fileobject object at 0x7faf2451b8d0>>
    The URL is:  http://lectureswww.readthedocs.org/ru/latest/
    This gets the code:  200
    The Headers are:  Server: nginx/1.4.6 (Ubuntu)
    X-Deity: chimera-lts
    Vary: Accept-Encoding
    X-Served: Nginx
    Content-Type: text/html
    Date: Fri, 06 Feb 2015 10:15:11 GMT
    Accept-Ranges: bytes
    ETag: "54c74bc0-62a2"
    Connection: close
    X-Subdomain-TryFiles: True
    Last-Modified: Tue, 27 Jan 2015 08:26:40 GMT
    Content-Length: 25250

    The Date is:  Fri, 06 Feb 2015 10:15:11 GMT
    The Server is:  nginx/1.4.6 (Ubuntu)
    Get all data:

    <!DOCTYPE html>
    <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Основы Веб-программирования &mdash; Документ
    Get the length : 25250


Запись в файл

.. code-block:: python

    import urllib2

    # file to be written to
    file = "downloaded_file.html"

    url = "http://www.pythonforbeginners.com/"
    response = urllib2.urlopen(url)

    #open the file for writing
    fh = open(file, "w")

    # read from request while writing to file
    fh.write(response.read())
    fh.close()

    # You can also use the with statement:
    with open(file, 'w') as f: f.write(response.read())

Скачиваем файл по прямой ссылке

.. code-block:: python

    import urllib2

    mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
    output = open('test.mp3','wb')
    output.write(mp3file.read())
    output.close()

POST запрос

.. code-block:: python

    import urllib2
    import urllib

    # Specify the url
    url = 'http://nigma.ru'

    # Prepare the data
    query_args = {'s': "Веб программирование"}

    # This urlencodes your data (that's why we need to import urllib at the top)
    data = urllib.urlencode(query_args)

    # Send HTTP POST request
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    html = response.read()

    # Print the result
    print(html[:330])

.. code-block:: html

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

    <html>

        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">


            <title>Нигма-интернет : Веб программирование

Заголовки

.. code-block:: python

    import urllib2

    req = urllib2.Request('http://lectureswww.readthedocs.org/')
    req.add_header('User-agent', 'Mozilla 5.10')
    print(req.headers)

    res = urllib2.urlopen(req)
    html = res.read()
    print(html[:350])

.. code-block:: html

    {'User-agent': 'Mozilla 5.10'}


    <!DOCTYPE html>
    <!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Основы Веб-программирования &mdash; Документ

requests
--------

.. note::

    http://docs.python-requests.org/en/latest/

`requests` - самая популярная библиотека на языке программирования Python.
Она предоставляет более абстрактный уровень чем urllib, urllib2 и использует их в своем коде.

Пример Basic авторизации через urllib

.. code-block:: python

    import urllib2

    gh_url = 'https://api.github.com'

    req = urllib2.Request(gh_url)

    password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, gh_url, 'user', 'pass')

    auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
    opener = urllib2.build_opener(auth_manager)

    urllib2.install_opener(opener)

    handler = urllib2.urlopen(req)

    print(handler.getcode())
    print(handler.headers.getheader('content-type'))

    # ------
    # 200
    # 'application/json'

Тоже но на requests

.. code-block:: python

    import requests

    r = requests.get('https://api.github.com', auth=('user', 'pass'))

    print(r.status_code)
    print(r.headers['content-type'])

    # ------
    # 200
    # 'application/json'

Сессии

.. code-block:: python

   import requests

   s = requests.Session()

   s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
   r = s.get("http://httpbin.org/cookies")

   print(r.text)
   # '{"cookies": {"sessioncookie": "123456789"}}'
