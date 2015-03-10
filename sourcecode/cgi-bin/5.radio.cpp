/*
 * 5.radio.cpp
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
    Cgicc formData;

    cout << "Content-type:text/html\r\n\r\n";
    cout << "<html>\n";
    cout << "<head>\n";
    cout << "<title>Radio Button Data to CGI</title>\n";
    cout << "</head>\n";
    cout << "<body>\n";

    form_iterator fi = formData.getElement("subject");  
    if( !fi->isEmpty() && fi != (*formData).end()) {  
        cout << "Radio box selected: " << **fi << endl;  
    }

    cout << "<br/>\n";
    cout << "</body>\n";
    cout << "</html>\n";

    return 0;
}
