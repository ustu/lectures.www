Mako
====

Mako - это стандартный шаблонизoатор для фреймворка ``Pylons``, написанный Майком Байером (автор ``SQLAlchemy``) и используется на таких сайтах как https://python.org и http://reddit.com

Hello ${ name }!
----------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/mako/0.hello.py
   :language: python
   :linenos:

Hello Вася!

## Комментарии
--------------

.. todo:: добавить описание

.. code-block:: mako

   ## Однострочный коммент

   <%doc> Это кусок кода который стал временно не ненужен, но удалять жалко
       % for user in users:
           ...
       % endfor
   </%doc>

${ Выражения }
--------------

.. code-block:: mako

   Это foo: ${foo}

.. code-block:: mako

   Теорема Пифагора:  ${pow(x,2) + pow(y,2)}
