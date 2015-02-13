Парсим HTML
===========

.. note::

    http://devacademy.ru/posts/parsing-resursov-pri-pomoschi-python/

Разбор HTTP ответа
------------------

Довольно легко распарсить html код полученный при помощи lxml. Как только мы преобразовали данные в дерево, можно использовать xPath для извлечения данных.

.. code-block:: python

   import requests
   from lxml import html

   response = requests.get('http://ya.ru')

   # Преобразование тела документа в дерево элементов (DOM)
   parsed_body = html.fromstring(response.text)

   # Выполнение xpath в дереве элементов
   print parsed_body.xpath('//title/text()')[0]    # Получить title страницы
   print parsed_body.xpath('//a/@href')            # Получить аттрибут href для всех ссылок

.. code-block:: bash

    Яндекс
    ['https://mail.yandex.ru', '//www.yandex.ru']

Скачиваем все изображения со страницы
-------------------------------------

Следующий скрипт скачает все изображения и сохранит их в downloaded_images/. Только сначала не забудьте создать соответствующий каталог.

.. code-block:: python

    import requests
    from lxml import html
    import sys
    import urlparse

    response = requests.get('http://imgur.com/')
    parsed_body = html.fromstring(response.text)

    # Парсим ссылки с картинками
    images = parsed_body.xpath('//img/@src')
    if not images:
        sys.exit("Found No Images")

    # Конвертирование всех относительных ссылок в абсолютные
    images = [urlparse.urljoin(response.url, url) for url in images]
    print 'Found %s images' % len(images)

    # Скачиваем только первые 10
    for url in images[0:10]:
        r = requests.get(url)
        f = open('downloaded_images/%s' % url.split('/')[-1], 'w')
        f.write(r.content)
        f.close()

.. image:: /_static/imgur.png
