#! /bin/sh
#
# test.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#

err=3

while test "$err" -eq 3 ; do
    python 3.http.middleware.py
    err="$?"
done
