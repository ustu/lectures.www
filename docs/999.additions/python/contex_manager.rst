.. _context_manager:

Контекстный менеджер
====================

.. seealso::

   * :PEP:`343`


.. code-block:: python
   :linenos:

   with file("/tmp/foo", "w") as foo:
       print >> foo, "Hello!"

Эквивалентно

.. code-block:: python
   :linenos:

   foo = file("/tmp/foo", "w")
   try:
       print >> foo, "Hello!"
   finally:
       foo.close()
