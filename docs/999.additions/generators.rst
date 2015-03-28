Генераторы
==========

.. seealso::

   * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*
   * `<https://ru.wikipedia.org/wiki/Продолжение_(информатика)>`_

Python
------

.. todo::

   расписать детали

.. literalinclude:: /../sourcecode/999.additions/generators/gen.py
   :language: python
   :linenos:

Запуск:

.. code-block:: bash

   $ python gen.py
   0
   1
   2

.. literalinclude:: /../sourcecode/999.additions/generators/csv_gen.py
   :language: python
   :linenos:

.. literalinclude:: /../sourcecode/999.additions/generators/sample.csv
   :linenos:

.. code-block:: bash

   $ python csv_gen.py
   ['1997', 'Ford', 'E350', '"ac', ' abs', ' moon"', '3000.00\n']
   ['1999', 'Chevy', '"Venture ""Extended Edition"""', '""', '4900.00\n']
   ['1996', 'Jeep', 'Grand Cherokee', '"MUST SELL! air', ' moon roof', ' loaded"', '4799.00\n']

JavaScript
----------

.. literalinclude:: /../sourcecode/999.additions/generators/gen.js
   :language: javascript
   :linenos:

Запуск:

.. code-block:: bash

   $ iojs gen.js
   0
   1
   2
