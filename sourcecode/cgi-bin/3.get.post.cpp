/*
 * 3.get.cpp
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
    cout << "<title>Using GET and POST Methods</title>\n";
    cout << "</head>\n";
    cout << "<body>\n";

    form_iterator fi = formData.getElement("first_name");
    if(fi != (*formData).end()) {
        cout << "First name: " << **fi << endl;
    }else{
        cout << "No text entered for first name" << endl;
    }
    cout << "<br/>\n";
    fi = formData.getElement("last_name");
    if(fi != (*formData).end()) {
        cout << "Last name: " << **fi << endl;
    }else{
        cout << "No text entered for last name" << endl;
    }
    cout << "<br/>\n";

    cout << "</body>\n";
    cout << "</html>\n";

    return 0;
}
