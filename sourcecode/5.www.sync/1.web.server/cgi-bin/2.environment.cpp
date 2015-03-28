/*
 * 2.environment.cpp
 * Copyright (C) 2015 uralbash <root@uralbash.ru>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv, char** env)
{
    cout << "Content-type:text/html\r\n\r\n";
    cout << "<html>\n";
    cout << "<head>\n";
    cout << "<title>CGI Envrionment Variables</title>\n";
    cout << "</head>\n";
    cout << "<body>\n";

    while (*env)
        cout << *env++ << "<br/>";

    cout << "</body>\n";
    cout << "</html>\n";

    return 0;
}
