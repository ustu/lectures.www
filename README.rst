Инструкция как писать эту документацию
======================================

Документация написана при помощи языка разметки reStructuredText и генератора Sphinx.
Sphinx — это генератор документации, который преобразует файлы в формате reStructuredText
в HTML website и другие форматы (PDF, EPub и man).

| `<https://ru.wikipedia.org/wiki/Sphinx_(генератор_документации)>`_
| `Докумнтация на русском <https://sphinx-ru.readthedocs.org/ru/latest/>`_

Установка
---------

Установка sphinx

.. code-block:: bash

  pip install sphinx
  
Клонирование репозитария

.. code-block:: bash

  git clone git@github.com:ustu/lectures.www.git
  cd lecctures.www

Сборка
------

Для Unix like

.. code-block:: bash

  make html

Для Windows

.. code-block:: bash

  make.bat html

Зависимости
-----------

Для команды ``make livehtml`` необходимо установить `sphinx-autobuild <https://github.com/GaretJax/sphinx-autobuild>`_
