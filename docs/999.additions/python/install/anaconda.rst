Установка Anaconda в Windows
============================

Установка интерпретатора CPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::

    * https://www.anaconda.com/
    * https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)

Anaconda -- свободный open source дистрибутив для языков программирования Python
и R с открытым кодом для обработки данных большого объема, построения
аналитических прогнозов и научных вычислений. Разработчики дистрибутива имеют
цель упростить управление и использование пакетов. Версии пакетов
контролируются системой управления пакетами conda. По умолчанию, вместе с
Anaconda устанавливается также:

* JupyterLab
* Jupyter Notebook
* Spyder

Пакетный менеджер conda
~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::

    https://conda.io/docs/user-guide/getting-started.html

После установки дистрибутива `Anaconda` в командной строке (`cmd.exe`) должна
появится команда пакетного менеджера `conda`.

Проверим версию выполнив команду в терминале:

.. code-block:: winbatch

    C:\Users\user>conda --version
    conda 4.3.30

Неплохо было бы обновится до последней версии, делается это командой `update`:

.. code-block:: winbath

    C:\Users\user>conda update conda
    Fetching package metadata ...............
    Solving package specifications: .

    Package plan for installation in environment C:\Users\user\Anaconda3:

    The following packages will be UPDATED:

        conda:   4.3.30-py36h404fb56_0 --> 4.5.11-py36_0
        pycosat: 0.6.1-py36_1          --> 0.6.3-py36hfa6e2cd_0

    Proceed ([y]/n)? y

    pycosat-0.6.3- 100% |###############################| Time: 0:00:00   1.40 MB/s
    conda-4.5.11-p 100% |###############################| Time: 0:00:00   5.15 MB/s

`Anaconda` дополнительно устанавливает множество различных python пакетов для
того, что бы узнать, что у нас установлено необходимо выполнить команду `list`:

.. code-block:: winbath

    C:\Users\user\Project\pyramid_test>conda list
    # packages in environment at C:\Users\user\Anaconda3:
    #
    # Name                    Version                   Build  Channel
    _license                  1.1                      py36_1
    alabaster                 0.7.9                    py36_0
    anaconda                  custom                   py36_0
    anaconda-client           1.6.0                    py36_0
    anaconda-navigator        1.5.0                    py36_0
    anaconda-project          0.4.1                    py36_0
    anyqt                     0.0.8                    py36_0
    astroid                   1.4.9                    py36_0
    astropy                   1.3                 np111py36_0
    babel                     2.3.4                    py36_0
    backports                 1.0                      py36_0
    beautifulsoup4            4.5.3                    py36_0
    bitarray                  0.8.1                    py36_1
    blas                      1.0                         mkl
    blaze                     0.10.1                   py36_0
    bokeh                     0.12.4                   py36_0
    boto                      2.45.0                   py36_0
    bottleneck                1.2.0               np111py36_0
    bzip2                     1.0.6                    vc14_3  [vc14]
    cffi                      1.9.1                    py36_0
    chardet                   2.3.0                    py36_0
    chest                     0.2.3                    py36_0
    click                     6.7                      py36_0
    cloudpickle               0.2.2                    py36_0
    clyent                    1.2.2                    py36_0
    colorama                  0.3.7                    py36_0
    comtypes                  1.1.2                    py36_0
    conda                     4.5.11                   py36_0
    conda-env                 2.6.0                         0
    configobj                 5.0.6                    py36_0
    console_shortcut          0.1.1                    py36_1
    contextlib2               0.5.4                    py36_0
    cryptography              1.7.1                    py36_0
    curl                      7.52.1                   vc14_0  [vc14]
    ...

Виртуальное окружение Conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Conda` позволяет создавать виртуальные окружения для изолированной разработки
программ. Делается это при помощи команды `create`:

.. code-block:: winbath

    C:\Users\user>conda create --name myenv sqlite
    Solving environment: done

    ## Package Plan ##

      environment location: C:\Users\user\Anaconda3\envs\myenv

      added / updated specs:
        - sqlite


    The following packages will be downloaded:

        package                    |            build
        ---------------------------|-----------------
        vc-14.1                    |       h0510ff6_4           6 KB
        sqlite-3.25.2              |       hfa6e2cd_0         897 KB
        vs2015_runtime-14.15.26706 |       h3a45250_0         2.1 MB
        ------------------------------------------------------------
                                               Total:         2.9 MB

    The following NEW packages will be INSTALLED:

        sqlite:         3.25.2-hfa6e2cd_0
        vc:             14.1-h0510ff6_4
        vs2015_runtime: 14.15.26706-h3a45250_0

    Proceed ([y]/n)? y


    Downloading and Extracting Packages
    vc-14.1              | 6 KB      | ############################################################################ | 100%
    sqlite-3.25.2        | 897 KB    | ############################################################################ | 100%
    vs2015_runtime-14.15 | 2.1 MB    | ############################################################################ | 100%
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use:
    # > activate myenv
    #
    # To deactivate an active environment, use:
    # > deactivate
    #
    # * for power-users using bash, you must source
    #


    C:\Users\user>

Активация виртуального окружения осуществляется при помощи команды `activate`:

.. code-block:: winbath

    C:\Users\user>activate myenv

    (myenv) C:\Users\user>conda list
    # packages in environment at C:\Users\user\Anaconda3\envs\myenv:
    #
    # Name                    Version                   Build  Channel
    sqlite                    3.25.2               hfa6e2cd_0
    vc                        14.1                 h0510ff6_4
    vs2015_runtime            14.15.26706          h3a45250_0

После активации, мы как бы находимся внутри изолированного окружения,
подтверждением этого является пригласительная надпись в круглых скобках в начале
строки с именем нашего окружения  `(myenv)`. Теперь если запустить команду
`list` (список установленных пакетов) мы получим намного меньший список только
того, что установлено в наше новое виртуальное окружение.

Пакетный менеджер pip
~~~~~~~~~~~~~~~~~~~~~

Пакетный менеджер `pip` это универсальный инструмент установки пакетов в мире
`python`, он устанавливает официальные пакеты из общего хранилища пакетов
`PyPi`. Поэтому `pip` незаменимый инструмент для разработки на `Python`.
Установим его при помощи команды `install`.

.. code-block:: winbath

    (myenv) C:\Users\user>conda install pip
    Solving environment: done


    ==> WARNING: A newer version of conda exists. <==
      current version: 4.4.6
      latest version: 4.5.11

    Please update conda by running

        $ conda update -n base conda



    ## Package Plan ##

      environment location: C:\Users\user\Anaconda3\envs\myenv

      added / updated specs:
        - pip


    The following packages will be downloaded:

        package                    |            build
        ---------------------------|-----------------
        setuptools-40.4.3          |           py37_0         575 KB
        wincertstore-0.2           |           py37_0          13 KB
        pip-10.0.1                 |           py37_0         1.7 MB
        python-3.7.1               |       h33f27b4_3        18.6 MB
        wheel-0.32.2               |           py37_0          51 KB
        sqlite-3.20.1              |   vc14hf772eac_1         796 KB
        certifi-2018.10.15         |           py37_0         138 KB
        ------------------------------------------------------------
                                               Total:        21.9 MB

    The following NEW packages will be INSTALLED:

        certifi:      2018.10.15-py37_0
        pip:          10.0.1-py37_0
        python:       3.7.1-h33f27b4_3
        setuptools:   40.4.3-py37_0
        wheel:        0.32.2-py37_0
        wincertstore: 0.2-py37_0

    The following packages will be DOWNGRADED:

        sqlite:       3.25.2-hfa6e2cd_0 --> 3.20.1-vc14hf772eac_1

    Proceed ([y]/n)? y


    Downloading and Extracting Packages
    setuptools 40.4.3: ############################################################################################ | 100%
    wincertstore 0.2: ############################################################################################# | 100%
    pip 10.0.1: ################################################################################################### | 100%
    python 3.7.1: ################################################################################################# | 100%
    wheel 0.32.2: ################################################################################################# | 100%
    sqlite 3.20.1: ################################################################################################ | 100%
    certifi 2018.10.15: ########################################################################################### | 100%
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done

Теперь нам доступны все пакеты с `PyPi`, установим фреймворк `Pyramid`:

.. code-block:: winbath

    (myenv) C:\Users\user>pip install pyramid
    Collecting pyramid
      Downloading https://files.pythonhosted.org/packages/85/c7/0a14873ef7bbb6d30e38678334d5b5faee1ccae2f5a59f093d104a3cc5ee/pyramid-1.9.2-py2.py3-none-any.whl (582kB)
        100% |████████████████████████████████| 583kB 4.0MB/s
    Collecting zope.deprecation>=3.5.0 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/ee/33/625098914ec59b3006adf2cdf44a721e9671f4836af9eeb8cbe14e485954/zope.deprecation-4.3.0-py2.py3-none-any.whl
    Collecting zope.interface>=3.8.0 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/55/99/f728599ef08137889cacc58c08e3b1affe974fcd029528a822ec7b7efffa/zope.interface-4.6.0-cp37-cp37m-win32.whl (132kB)
        100% |████████████████████████████████| 133kB 2.0MB/s
    Collecting plaster-pastedeploy (from pyramid)
      Downloading https://files.pythonhosted.org/packages/d9/e2/de7cd499923dbf6aacc9b243f262817bfea3ffbbd4dcc5847e1aaec817a7/plaster_pastedeploy-0.6-py2.py3-none-any.whl
    Collecting translationstring>=0.4 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/26/e7/9dcf5bcd32b3ad16db542845ad129c06927821ded434ae88f458e6190626/translationstring-1.3-py2.py3-none-any.whl
    Requirement already satisfied: setuptools in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid) (40.4.3)
    Collecting PasteDeploy>=1.5.0 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/31/28/51201a54aeecbd02eff767d17050b302f6fd98fdfecb4e3f4c9301ba6ef8/PasteDeploy-1.5.2-py2.py3-none-any.whl
    Collecting plaster (from pyramid)
      Downloading https://files.pythonhosted.org/packages/61/29/3ac8a5d03b2d9e6b876385066676472ba4acf93677acfc7360b035503d49/plaster-1.0-py2.py3-none-any.whl
    Collecting WebOb>=1.7.0 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/b5/74/a9aaec7ca6c94a58e379a9c95255a2b2017514948054c72c0d1a25953348/WebOb-1.8.3-py2.py3-none-any.whl (113kB)
        100% |████████████████████████████████| 122kB 3.8MB/s
    Collecting repoze.lru>=0.4 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/b0/30/6cc0c95f0b59ad4b3b9163bff7cdcf793cc96fac64cf398ff26271f5cf5e/repoze.lru-0.7-py3-none-any.whl
    Collecting hupper (from pyramid)
      Downloading https://files.pythonhosted.org/packages/70/b7/4013ae11e977d4a38141ecba1c754f8b0a826b182de0c5c6fb780ede9834/hupper-1.3.1-py2.py3-none-any.whl
    Collecting venusian>=1.0a3 (from pyramid)
      Downloading https://files.pythonhosted.org/packages/2f/c2/3d122e19287ed7d73f03821cef87e53673f27d41cae54ee3a46e92b147e2/venusian-1.1.0-py2.py3-none-any.whl
    Installing collected packages: zope.deprecation, zope.interface, PasteDeploy, plaster, plaster-pastedeploy, translationstring, WebOb, repoze.lru, hupper, venusian, pyramid
    Successfully installed PasteDeploy-1.5.2 WebOb-1.8.3 hupper-1.3.1 plaster-1.0 plaster-pastedeploy-0.6 pyramid-1.9.2 repoze.lru-0.7 translationstring-1.3 venusian-1.1.0 zope.deprecation-4.3.0 zope.interface-4.6.0
    You are using pip version 10.0.1, however version 18.1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.

Проверим что пакет установился командой `list`:

.. code-block:: winbath
    :emphasize-lines: 10

    (myenv) C:\Users\user>conda list
    # packages in environment at C:\Users\user\Anaconda3\envs\myenv:
    #
    certifi                   2018.10.15               py37_0
    hupper                    1.3.1                     <pip>
    PasteDeploy               1.5.2                     <pip>
    pip                       10.0.1                   py37_0
    plaster                   1.0                       <pip>
    plaster-pastedeploy       0.6                       <pip>
    pyramid                   1.9.2                     <pip>
    python                    3.7.1                h33f27b4_3
    repoze.lru                0.7                       <pip>
    setuptools                40.4.3                   py37_0
    sqlite                    3.20.1           vc14hf772eac_1  []
    translationstring         1.3                       <pip>
    vc                        14.1                 h0510ff6_4  []
    venusian                  1.1.0                     <pip>
    vs2015_runtime            14.15.26706          h3a45250_0  []
    WebOb                     1.8.3                     <pip>
    wheel                     0.32.2                   py37_0
    wincertstore              0.2                      py37_0
    zope.deprecation          4.3.0                     <pip>
    zope.interface            4.6.0                     <pip>

Пример
~~~~~~

.. seealso::

    https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html

Для примера создадим стартовую Веб-страницу при помощи фреймворка `Pyramid`.
Для её создания будем использовать готовый шаблон проекта, который можно
установить при помощи программы `cookiecutter`. Скачаем `cookiecutter`:

.. code-block:: winbath

    (myenv) C:\Users\user\Project\pyramid_test>pip install cookiecutter
    Collecting cookiecutter
      Downloading https://files.pythonhosted.org/packages/16/99/1ca3a75978270288354f419e9166666801cf7e7d8df984de44a7d5d8b8d0/cookiecutter-1.6.0-py2.py3-none-any.whl (50kB)
        100% |████████████████████████████████| 51kB 584kB/s
    Collecting requests>=2.18.0 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/f1/ca/10332a30cb25b627192b4ea272c351bce3ca1091e541245cccbace6051d8/requests-2.20.0-py2.py3-none-any.whl (60kB)
        100% |████████████████████████████████| 61kB 1.5MB/s
    Collecting poyo>=0.1.0 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/e0/16/e00e3001007a5e416ca6a51def6f9e4be6a774bf1c8486d20466f834d113/poyo-0.4.2-py2.py3-none-any.whl
    Collecting click>=5.0 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
        100% |████████████████████████████████| 81kB 6.8MB/s
    Collecting jinja2>=2.7 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
        100% |████████████████████████████████| 133kB 8.9MB/s
    Collecting future>=0.15.2 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/85/aa/ba2e24dcb889d7e98733f87515d80b3512418b80ba79d82d2ddcd43fadf3/future-0.17.0.tar.gz (827kB)
        100% |████████████████████████████████| 829kB 3.1MB/s
    Collecting whichcraft>=0.4.0 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/ab/c6/eb4d1dfbb68168bb01c4394420e5e71d5851e64b910838aa0f14ebd5c7a0/whichcraft-0.5.2-py2.py3-none-any.whl
    Collecting jinja2-time>=0.1.0 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/6a/a1/d44fa38306ffa34a7e1af09632b158e13ec89670ce491f8a15af3ebcb4e4/jinja2_time-0.2.0-py2.py3-none-any.whl
    Collecting binaryornot>=0.2.0 (from cookiecutter)
      Downloading https://files.pythonhosted.org/packages/24/7e/f7b6f453e6481d1e233540262ccbfcf89adcd43606f44a028d7f5fae5eb2/binaryornot-0.4.4-py2.py3-none-any.whl
    Collecting urllib3<1.25,>=1.21.1 (from requests>=2.18.0->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/8c/4b/5cbc4cb46095f369117dcb751821e1bef9dd86a07c968d8757e9204c324c/urllib3-1.24-py2.py3-none-any.whl (117kB)
        100% |████████████████████████████████| 122kB 4.1MB/s
    Collecting idna<2.8,>=2.5 (from requests>=2.18.0->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl (58kB)
        100% |████████████████████████████████| 61kB 4.7MB/s
    Collecting chardet<3.1.0,>=3.0.2 (from requests>=2.18.0->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
        100% |████████████████████████████████| 143kB 7.6MB/s
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from requests>=2.18.0->cookiecutter) (2018.10.15)
    Collecting MarkupSafe>=0.23 (from jinja2>=2.7->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
    Collecting arrow (from jinja2-time>=0.1.0->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/e0/86/4eb5228a43042e9a80fe8c84093a8a36f5db34a3767ebd5e1e7729864e7b/arrow-0.12.1.tar.gz (65kB)
        100% |████████████████████████████████| 71kB 2.0MB/s
    Collecting python-dateutil (from arrow->jinja2-time>=0.1.0->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/2f/e9/b02e8a1a8c53a55a4f37df1e8e111539d0a3e76828bcd252947a5200b797/python_dateutil-2.7.4-py2.py3-none-any.whl (211kB)
        100% |████████████████████████████████| 215kB 2.9MB/s
    Collecting six>=1.5 (from python-dateutil->arrow->jinja2-time>=0.1.0->cookiecutter)
      Downloading https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
    Building wheels for collected packages: future, MarkupSafe, arrow
      Running setup.py bdist_wheel for future ... done
      Stored in directory: C:\Users\user\AppData\Local\pip\Cache\wheels\fc\5b\ec\2983c4a6e3692d1315f44d6480c6abdd8585d96471b431d6b4
      Running setup.py bdist_wheel for MarkupSafe ... done
      Stored in directory: C:\Users\user\AppData\Local\pip\Cache\wheels\33\56\20\ebe49a5c612fffe1c5a632146b16596f9e64676768661e4e46
      Running setup.py bdist_wheel for arrow ... done
      Stored in directory: C:\Users\user\AppData\Local\pip\Cache\wheels\a3\dd\b2\d3b8d22e8136164c2e2c36ed42392531957cdf9c717065b28b
    Successfully built future MarkupSafe arrow
    Installing collected packages: urllib3, idna, chardet, requests, poyo, click, MarkupSafe, jinja2, future, whichcraft, six, python-dateutil, arrow, jinja2-time, binaryornot, cookiecutter
    Successfully installed MarkupSafe-1.0 arrow-0.12.1 binaryornot-0.4.4 chardet-3.0.4 click-7.0 cookiecutter-1.6.0 future-0.17.0 idna-2.7 jinja2-2.10 jinja2-time-0.2.0 poyo-0.4.2 python-dateutil-2.7.4 requests-2.20.0 six-1.11.0 urllib3-1.24 whichcraft-0.5.2
    You are using pip version 10.0.1, however version 18.1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.

При помощи `cookiecutter` развернем самый простой шаблон Веб-сайта который имеется в фреймворке `Pyramid`:

.. code-block:: winbath

    (myenv) C:\Users\user\Project\pyramid_test>cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 1.9-branch
    project_name [Pyramid Scaffold]: myfirstapp
    repo_name [myfirstapp]:
    Select template_language:
    1 - jinja2
    2 - chameleon
    3 - mako
    Choose from 1, 2, 3 (1, 2, 3) [1]: 1

    ===============================================================================
    Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
    Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
    Twitter:       https://twitter.com/PylonsProject
    Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    ===============================================================================

    Change directory into your newly created project.
        cd myfirstapp

    Create a Python virtual environment.
        py -3 -m venv env

    Upgrade packaging tools.
        env\Scripts\pip install --upgrade pip setuptools

    Install the project in editable mode with its testing requirements.
        env\Scripts\pip install -e ".[testing]"

    Run your project's tests.
        env\Scripts\pytest

    Run your project.
        env\Scripts\pserve development.ini

Проект создается в отдельной директории ``myfirstapp``.

.. code-block:: winbath

    (myenv) C:\Users\user\Project\pyramid_test>dir
     Том в устройстве C не имеет метки.
     Серийный номер тома: 480D-DE95

     Содержимое папки C:\Users\user\Project\pyramid_test

    26.10.2018  16:30    <DIR>          .
    26.10.2018  16:30    <DIR>          ..
    26.10.2018  16:30    <DIR>          myfirstapp
                   0 файлов              0 байт
                   3 папок  31 729 090 560 байт свободно

Что бы запустить проект необходимо прежде установить его в окружение, перейдем
в директорию проекта и запустим стандартную команду установки пакетов из
исходников.

.. code-block:: winbath

    (myenv) C:\Users\user\Project\pyramid_test>cd myfirstapp
    (myenv) C:\Users\user\Project\pyramid_test\myfirstapp>pip install -e .
    Obtaining file:///C:/Users/user/Project/pyramid_test/myfirstapp
    Requirement already satisfied: plaster_pastedeploy in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from myfirstapp==0.0) (0.6)
    Requirement already satisfied: pyramid in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from myfirstapp==0.0) (1.9.2)
    Collecting pyramid_jinja2 (from myfirstapp==0.0)
      Downloading https://files.pythonhosted.org/packages/21/30/fdd0b9a365a60c9e56ae4730c8839eae603f7a87696df14dbd4f980acf35/pyramid_jinja2-2.7-py2.py3-none-any.whl (70kB)
        100% |████████████████████████████████| 71kB 421kB/s
    Collecting pyramid_debugtoolbar (from myfirstapp==0.0)
      Downloading https://files.pythonhosted.org/packages/6f/9a/933267076461c1fd6f4f8b0715ecf037dbe622180d0b77e7ea605a32b51b/pyramid_debugtoolbar-4.5-py2.py3-none-any.whl (345kB)
        100% |████████████████████████████████| 348kB 2.3MB/s
    Collecting waitress (from myfirstapp==0.0)
      Downloading https://files.pythonhosted.org/packages/ee/af/ac32a716d64e56561ee9c23ce45ee2865d7ac4e0678b737d2f5ee49b5fd6/waitress-1.1.0-py2.py3-none-any.whl (114kB)
        100% |████████████████████████████████| 122kB 3.7MB/s
    Requirement already satisfied: PasteDeploy>=1.5.0 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from plaster_pastedeploy->myfirstapp==0.0) (1.5.2)
    Requirement already satisfied: plaster>=0.5 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from plaster_pastedeploy->myfirstapp==0.0) (1.0)
    Requirement already satisfied: zope.interface>=3.8.0 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (4.6.0)
    Requirement already satisfied: translationstring>=0.4 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (1.3)
    Requirement already satisfied: zope.deprecation>=3.5.0 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (4.3.0)
    Requirement already satisfied: setuptools in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (40.4.3)
    Requirement already satisfied: WebOb>=1.7.0 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (1.8.3)
    Requirement already satisfied: hupper in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (1.3.1)
    Requirement already satisfied: repoze.lru>=0.4 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (0.7)
    Requirement already satisfied: venusian>=1.0a3 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid->myfirstapp==0.0) (1.1.0)
    Requirement already satisfied: MarkupSafe in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid_jinja2->myfirstapp==0.0) (1.0)
    Requirement already satisfied: Jinja2>=2.5.0 in c:\users\user\anaconda3\envs\myenv\lib\site-packages (from pyramid_jinja2->myfirstapp==0.0) (2.10)
    Collecting Pygments (from pyramid_debugtoolbar->myfirstapp==0.0)
      Downloading https://files.pythonhosted.org/packages/02/ee/b6e02dc6529e82b75bb06823ff7d005b141037cb1416b10c6f00fc419dca/Pygments-2.2.0-py2.py3-none-any.whl (841kB)
        100% |████████████████████████████████| 849kB 1.9MB/s
    Collecting pyramid-mako>=0.3.1 (from pyramid_debugtoolbar->myfirstapp==0.0)
      Downloading https://files.pythonhosted.org/packages/f1/92/7e69bcf09676d286a71cb3bbb887b16595b96f9ba7adbdc239ffdd4b1eb9/pyramid_mako-1.0.2.tar.gz
    Collecting Mako>=0.8 (from pyramid-mako>=0.3.1->pyramid_debugtoolbar->myfirstapp==0.0)
      Downloading https://files.pythonhosted.org/packages/eb/f3/67579bb486517c0d49547f9697e36582cd19dafb5df9e687ed8e22de57fa/Mako-1.0.7.tar.gz (564kB)
        100% |████████████████████████████████| 573kB 1.5MB/s
    Building wheels for collected packages: pyramid-mako, Mako
      Running setup.py bdist_wheel for pyramid-mako ... done
      Stored in directory: C:\Users\user\AppData\Local\pip\Cache\wheels\08\5f\98\3dfc5a39bcb3fd094897db7f394eb13768cdf472bdf2a89a2f
      Running setup.py bdist_wheel for Mako ... done
      Stored in directory: C:\Users\user\AppData\Local\pip\Cache\wheels\15\35\25\dbcb848832ccb1a4b4ad23f529badfd3bce9bf88017f7ca510
    Successfully built pyramid-mako Mako
    Installing collected packages: pyramid-jinja2, Pygments, Mako, pyramid-mako, pyramid-debugtoolbar, waitress, myfirstapp
      Running setup.py develop for myfirstapp
    Successfully installed Mako-1.0.7 Pygments-2.2.0 myfirstapp pyramid-debugtoolbar-4.5 pyramid-jinja2-2.7 pyramid-mako-1.0.2 waitress-1.1.0
    You are using pip version 10.0.1, however version 18.1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.

Проверяем что все поставилось:

.. code-block:: winbath
    :emphasize-lines: 17

    (myenv) C:\Users\user\Project\pyramid_test\myfirstapp>conda list
    # packages in environment at C:\Users\user\Anaconda3\envs\myenv:
    #
    arrow                     0.12.1                    <pip>
    binaryornot               0.4.4                     <pip>
    certifi                   2018.10.15               py37_0
    chardet                   3.0.4                     <pip>
    Click                     7.0                       <pip>
    cookiecutter              1.6.0                     <pip>
    future                    0.17.0                    <pip>
    hupper                    1.3.1                     <pip>
    idna                      2.7                       <pip>
    Jinja2                    2.10                      <pip>
    jinja2-time               0.2.0                     <pip>
    Mako                      1.0.7                     <pip>
    MarkupSafe                1.0                       <pip>
    myfirstapp                0.0                       <pip>
    numpy                     1.15.3                    <pip>
    PasteDeploy               1.5.2                     <pip>
    pip                       10.0.1                   py37_0
    plaster                   1.0                       <pip>
    plaster-pastedeploy       0.6                       <pip>
    poyo                      0.4.2                     <pip>
    Pygments                  2.2.0                     <pip>
    pyramid                   1.9.2                     <pip>
    pyramid-debugtoolbar      4.5                       <pip>
    pyramid-jinja2            2.7                       <pip>
    pyramid-mako              1.0.2                     <pip>
    python                    3.7.1                h33f27b4_3
    python-dateutil           2.7.4                     <pip>
    repoze.lru                0.7                       <pip>
    requests                  2.20.0                    <pip>
    setuptools                40.4.3                   py37_0
    six                       1.11.0                    <pip>
    sqlite                    3.20.1           vc14hf772eac_1  []
    translationstring         1.3                       <pip>
    urllib3                   1.24                      <pip>
    vc                        14.1                 h0510ff6_4  []
    venusian                  1.1.0                     <pip>
    vs2015_runtime            14.15.26706          h3a45250_0  []
    waitress                  1.1.0                     <pip>
    WebOb                     1.8.3                     <pip>
    wheel                     0.32.2                   py37_0
    whichcraft                0.5.2                     <pip>
    wincertstore              0.2                      py37_0
    zope.deprecation          4.3.0                     <pip>
    zope.interface            4.6.0                     <pip>

Последний шаг это запуск самого Веб-приложения, после его установки в окружение
должна появиться команда ``pserve`` она позволяет запускать ``WSGI`` приложения
которым и является наш проект. Давайте попробуем это сделать:

.. code-block:: winbath

    (myenv) C:\Users\user\Project\pyramid_test\myfirstapp>pserve development.ini --reload
    Starting monitor for PID 1144.
    Starting server in PID 1144.
    Serving on http://DESKTOP-9JPISDO:6543
    Serving on http://DESKTOP-9JPISDO:6543


Заходим на http://localhost:6543/admin/

.. figure:: /_static/999.additions/python/install/windows/pyramid_simple_app.png
   :align: center
   :width: 800px
