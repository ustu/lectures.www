Декораторы для асинхронных функций пишутся как и для обычных только возвращать
нужно корутину, а не функцию.

Для примера обычная функция:

.. code-block:: python

   def plusplus(func):
       def wrapped():
           return func() + 1
       return wrapped


   @plusplus
   def one():
       return 1

   print(one())  # return 2


   @plusplus
   @plusplus
   @plusplus
   @plusplus
   def one():
       return 1

   print(one())  # now return 5

В декораторе наша обертка над функцией (``wrapped``) стала корутиной:

.. no-code-block:: python
   :linenos:
   :emphasize-lines: 7-9, 14-15, 30-31

   import timeit

   import asyncio


   def plusplus(func):
       async def wrapped():
           await asyncio.sleep(1)
           return await func() + 1
       return wrapped


   @plusplus
   async def one():
       await asyncio.sleep(2)
       return 1

   loop = asyncio.get_event_loop()

   start = timeit.default_timer()
   print(loop.run_until_complete(one()))  # return 2
   stop = timeit.default_timer()
   print(stop - start)  # minimum 3 seconds


   @plusplus
   @plusplus
   @plusplus
   @plusplus
   async def one():
       await asyncio.sleep(2)
       return 1

   start = timeit.default_timer()
   print(loop.run_until_complete(one()))  # return 5
   stop = timeit.default_timer()
   print(stop - start)  # minimum 6 seconds

Более практичный пример это функция ``json_response`` для вьюх в
:l:`aiohttp`. Идея взята из презентации
(http://igordavydenko.com/talks/lvivpy-4/#slide-31).


.. no-code-block:: python

   import ujson
   import asyncio
   from aiohttp import web


   def json_response(data, **kwargs):
       kwargs.setdefault('content_type', 'application/json')
       return web.Response(text=ujson.dumps(data), **kwargs)


   async def index(request):
      return json_response({"Hello": "World"})


Все хорошо но ретурнов во вьюхе может быть много и тогда оборачивать каждый в
``json_response`` довольно неудобно. Что бы решить эту проблему создадим
декоратор ``json_view``.

.. no-code-block:: python

   def json_view(func):
       async def wrapped(request):
           return json_response(await func(request))
       return wrapped

Теперь можно писать так:

.. no-code-block:: python

   @json_view
   async def index(request):
      if somethink:
         return {"Somethink": "happens"}
      else:
         return {"else": "happens"}
      return {"Hello": "World"}

Класс :class:`aiohttp.web.Response` позволяет задавать различные параметры типа
заголовков и статуса ответа. Перепишем наш декоратор таким образом что бы он
умел принимать эти параметры:


.. no-code-block:: python

   def json_view_arg(**kwargs):
       def wrap(func):
           async def wrapped(request):
               return json_response(await func(request), **kwargs)
           return wrapped
       return wrap

Теперь можно задать, например, кастомный заголовок ответа ``Server``:

.. no-code-block:: python

   @json_view_arg(headers={"Server": "Nginx"})
   async def index(request):
      return {"Hello": "World"}

.. image:: /_static/999.additions/python/header-server-nginx.png
   :align: center

И в заключение то же в виде класса-декоратора:

.. no-code-block:: python

   class JsonView(object):

       def __init__(self, **kwargs):
           self.kwargs = kwargs

       def __call__(self, func):
           async def wrapped(request):
               return json_response(await func(request), **self.kwargs)
           return wrapped

.. no-code-block:: python

   @JsonView(headers={"Server": "Nginx"})
   async def index(request):
      return {"Hello": "World"}
