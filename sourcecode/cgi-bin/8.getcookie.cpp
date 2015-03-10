/*
 * 8.getcookie.cpp
 * Copyright (C) 2015 uralbash <root@uralbash.ru>
 *
 * Distributed under terms of the MIT license.
 */
#include <iostream>
#include <cgicc/Cgicc.h>

using namespace std;
using namespace cgicc;

int main()
{
    Cgicc cgi;
    const_cookie_iterator cci;

    cout << "Content-type:text/html\r\n\r\n";
    cout << "<html>\n";
    cout << "<head>\n";
    cout << "<title>Cookies in CGI</title>\n";
    cout << "</head>\n";
    cout << "<body>\n";
    cout << "<table border = \"0\" cellspacing = \"2\">";

    // get environment variables
    const CgiEnvironment& env = cgi.getEnvironment();

    for( cci = env.getCookieList().begin();
            cci != env.getCookieList().end();
            ++cci )
    {
        cout << "<tr><td>" << cci->getName() << "</td><td>";
        cout << cci->getValue();
        cout << "</td></tr>\n";
    }
    cout << "</table>\n";

    cout << "<br/>\n";
    cout << "</body>\n";
    cout << "</html>\n";

    return 0;
}
