/*
 * 4.checkbox.cpp
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
    bool maths_flag, physics_flag;

    cout << "Content-type:text/html\r\n\r\n";
    cout << "<html>\n";
    cout << "<head>\n";
    cout << "<title>Checkbox Data to CGI</title>\n";
    cout << "</head>\n";
    cout << "<body>\n";

    maths_flag = formData.queryCheckbox("maths");
    if( maths_flag ) {
        cout << "Maths Flag: ON " << endl;
    }else{
        cout << "Maths Flag: OFF " << endl;
    }
    cout << "<br/>\n";

    physics_flag = formData.queryCheckbox("physics");
    if( physics_flag ) {
        cout << "Physics Flag: ON " << endl;
    }else{
        cout << "Physics Flag: OFF " << endl;
    }
    cout << "<br/>\n";
    cout << "</body>\n";
    cout << "</html>\n";

    return 0;
}
