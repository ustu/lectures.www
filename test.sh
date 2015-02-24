#! /bin/bash
#
# test.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#

rstcheck `find . -name "*.rst" -printf "%p "`
flake8 ./sourcecode/
pep8 ./sourcecode/
make doctest
