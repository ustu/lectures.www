.. _additions_python_decorator:

Декораторы
==========

.. seealso::

   * :PEP:`318`
   * http://lgiordani.com/blog/2015/04/23/python-decorators-metaprogramming-with-style/

Декоратор подменяет функцию, например мы можем подменить функцию ``foo`` на
ноль.

.. code-block:: python

   def zero(func):
      return 0

   @zero
   def foo():
      return "Hi"

   print(foo)  # 0
   print(foo())  # Вызовет ошибку как-будто мы хотим вызвать ноль 0()

Подменим функцию на другую:

.. code-block:: python

   def zero(func):
      return lambda: 0

   @zero
   def foo():
      return "Hi"

   print(foo())  # 0

Теперь ``foo`` это ``lambda: 0``, а ``foo()`` соответственно ``0``.

И более практичный пример, дополним нашу функцию:

.. code-block:: python

   def world(func):
      return lambda: func() + " World!"

   @world
   def foo():
      return "Hi"

   print(foo())  # Hi World!

   @world
   def hello():
      return "Hello"

   print(hello())  # Hello World!
