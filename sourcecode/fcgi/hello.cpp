/*
 * hello.cpp
 * Copyright (C) 2015 uralbash <root@uralbash.ru>
 *
 * Distributed under terms of the MIT license.
 */
#include "fcgi_stdio.h"
#include <stdlib.h>

int main(void)
{
    while(FCGI_Accept() >= 0)
    {
        printf("Content-type: text/html\r\nStatus: 200 OK\r\n\r\nHello World!");

    }

    return 0;
}
