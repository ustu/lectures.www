#! /bin/bash
#
# test.sh
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

RST_FILES=`find . -name "*.rst" -printf "%p "`
FLAKE8=$(flake8 ./sourcecode/)
# PEP8=$(pep8 ./sourcecode/)
RST_CHECK=$(rstcheck $RST_FILES --report 2 3>&1 1>&2 2>&3 | tee >(cat - >&2)) # fd=STDERR_FILENO

echo -e "${RED}"
if [ -n "$RST_CHECK" ] ||
    [ -n "$FLAKE8" ] ||
    [ -n "$PEP8" ]
then
    echo -e "RST_CHECK: ${RST_CHECK:-OK}"
    echo -e "PEP8: ${PEP8:-OK}"
    echo -e "FLAKE8: ${FLAKE8:-OK}"
    exit 1
else
    echo -e "${GREEN}OK!"
fi
echo -e "${NC}"

make doctest
