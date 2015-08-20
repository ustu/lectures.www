.. _sqlalchemy:

SQLAlchemy
==========

.. seealso::

   * :l:`SQLAlchemy`
   * https://ru.wikipedia.org/wiki/ORM
   * https://ru.wikipedia.org/wiki/SQLAlchemy

.. todo::

   Добавить http://www.vertabelo.com/blog/technical-articles/orms-under-the-hood

**ORM** (`англ. object-relational mapping, рус. объектно-реляционное
отображение`) — технология программирования, которая связывает базы данных с
концепциями объектно-ориентированных языков программирования, создавая
«виртуальную объектную базу данных». Существуют как проприетарные, так и
свободные реализации этой технологии.

**SQLAlchemy** — это библиотека на языке Python для работы с реляционными СУБД
с применением технологии ORM. Служит для синхронизации объектов Python и
записей реляционной базы данных. SQLAlchemy позволяет описывать структуры баз
данных и способы взаимодействия с ними на языке Python без использования SQL.

.. figure:: /_static/6.www.sync/9.databases/sqlalchemy_layers_ru.png
   :align: center

   Диаграмма уровней SQLAlchemy

Преимущества использования
--------------------------

Использование SQLAlchemy для автоматической генерации SQL-кода имеет несколько
преимуществ по сравнению с ручным написанием SQL:

* **Безопасность**. Параметры запросов экранируются, что делает атаки типа
  внедрение SQL-кода маловероятными.
* **Производительность**. Повышается вероятность повторного использования
  запроса к серверу базы данных, что может позволить ему в некоторых случаях
  применить повторно план выполнения запроса.
* **Переносимость**. SQLAlchemy, при должном подходе, позволяет писать код на
  Python, совместимый с несколькими back-end СУБД. Несмотря на стандартизацию
  языка SQL, между базами данных имеются различия в его реализации,
  абстрагироваться от которых и помогает SQLAlchemy.

Пример
------

Простейший пример с использованием SQLite в оперативной памяти:

.. code-block:: python
   :linenos:

   >>> from sqlalchemy import create_engine
   >>> engine = create_engine('sqlite:///:memory:')
   >>> engine.execute("select 'Hello, World!'").scalar()
   u'Hello, World!'

Базовые понятия
---------------

.. seealso::

   * https://ru.wikibooks.org/wiki/SQLAlchemy
   * https://bitbucket.org/zzzeek/pycon2013_student_package/

.. todo::

   * Описать сессии более подробно https://ru.wikibooks.org/wiki/SQLAlchemy/Sessions

.. toctree::
   :maxdepth: 3

   0.engine.rst
   1.metadata.rst
   2.sql_expressions.rst
   3.orm.rst

Применение и аналоги
--------------------

SQLAlchemy находит применение в веб-фреймворках :l:`TurboGears`,
:l:`Pylons`, :l:`Pyramid`, :l:`Zope`, :l:`Flask`.
Например, известный социальный новостной сайт `Reddit
<http://www.reddit.com/>`_ построен с использованием SQLAlchemy. Список
организаций, использующих SQLAlchemy, можно найти на `сайте проекта
<http://www.sqlalchemy.org/organizations.html>`_.
