#! /bin/bash
#
# test.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${RED}"
if rstcheck `find . -name "*.rst" -printf "%p "` ||
    flake8 ./sourcecode/ ||
    pep8 ./sourcecode/
then
    exit 1
fi
echo -e "${NC}"

make doctest
