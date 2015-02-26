#! /bin/bash
#
# test.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#

if rstcheck `find . -name "*.rst" -printf "%p "`
then
    exit 1
fi

if flake8 ./sourcecode/
then
    exit 1
fi

if pep8 ./sourcecode/
then
    exit 1
fi

make doctest
