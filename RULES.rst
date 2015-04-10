Правила оформления
==================

Директивы и роли
----------------

| :RFC:`2822` - добавляет ссылку на RFC стандарт.
| :PEP:`3156` - добавляет ссылку на PEP стандарт.
| :src:`6.www.sync/2.codding/blog/0.paster` - добавляет ссылку на код.
| :l:`Nginx` - список глобальных ссылок (см. conf.py)

Изображения
-----------

* Должна использоваться всегда директива ``figure`` вместо ``image``.
* Не должны содержать символов "точка" в путях:

  Не правильно:

     * foo.bar.baz.jpg
     * 0.network.png

  Правильно:

     * foo_bar_baz.jpg
     * 0_network.png

  При генерации PDF система LaTeX на распознает такие имена.

* Ширину картинки нужно ВСЕГДА! задавать в ``pt``, иначе она может не отобразится в PDF.

  .. code-block:: rst

     .. figure:: /_static/wsgi/blog/1_0_step.png
        :align: center
        :width: 100pt

  Это глюк. Подробности см. https://github.com/sphinx-doc/sphinx/issues/1813

* Изображения с одинаковым названием и разными расширениями, считаются одинаковыми. Приоритет отдается `SVG`.

  Пример:

     * foo.svg
     * foo.png

  Это одно и тоже, при выполнении ``make clean-image`` ``foo.png`` удалится, а при выполнении ``make image`` появится.

* Изображения с расширением ``*.svg`` должны включаться в документ следующим образом:

  .. code-block:: rst

    .. figure:: /_static/wsgi/blog/1_0_step_dia.*
       :align: center
       :scale: 80

       Схема работы WSGI-приложения `Blog`

  Заместо расширения ставится знак "*".

* Подпись у изображений с директивой ``figure`` не должны начинаться с `Рис.1` и т.п.
  Sphinx 1.3 - делает это автоматически. Ссылки на такие объекты делаются через ``:numref:``.

  Пример:

  .. code-block:: text

     .. figure:: acrolein.*
        :name: my_figure

        Figure caption

     Ссылка на изображение :numref:`my_figure`

* Статические изображения с расширением ``*.gif`` нужно избегать. В случае gif-анимации необходимо оборачивать в директиву ``.. only:: not latex``.

LaTeX
-----

* Все что не касается `LaTeX`, нужно оборачивать в директиву ``only``

  Пример:

  .. code-block:: rst

    .. only:: not latex

      .. raw:: html

          <form action="http://localhost:8000/cgi-bin/5.radio.cgi" method="POST" target="_blank">
             <input type="radio" name="subject" value="maths"
                                                 checked="checked"/> Maths
             <input type="radio" name="subject" value="physics" /> Physics
             <input type="submit" value="Select Subject" />
          </form>
