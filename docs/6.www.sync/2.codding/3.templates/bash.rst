Bash
====

sed шаблонизатор
----------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/bash/0.nginx_proxy_conf.tpl
   :language: jinja
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/bash/0.sed.sh
   :language: python
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/bash/proxy.nginx.conf
   :language: nginx
   :linenos:
   :name: render_result
   :caption: ``bash/proxy.nginx.conf`` - результат рендеринга шаблона

eval шаблонизатор
-----------------

.. todo:: добавить описание

.. literalinclude:: /../examples/wsgi/3.templates/bash/1.nginx_proxy_conf.tpl
   :language: bash
   :linenos:

.. literalinclude:: /../examples/wsgi/3.templates/bash/1.eval.sh
   :language: python
   :linenos:

:ref:`render_result`
