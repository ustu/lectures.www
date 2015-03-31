/*
 * 10.fileupload.cpp
 * Copyright (C) 2015 uralbash <root@uralbash.ru>
 *
 * Distributed under terms of the MIT license.
 */
#include <iostream>
#include <cgicc/Cgicc.h>
#include <cgicc/HTTPHTMLHeader.h>

using namespace std;
using namespace cgicc;

int main()
{
    Cgicc cgi;

    // get list of files to be uploaded
    const_file_iterator file = cgi.getFile("filename");
    if(file != cgi.getFiles().end()) {
        // send data type at cout.
        cout << HTTPContentHeader(file->getDataType());
        // write content at cout.
        file->writeToStream(cout);
        cout << "<br><br>";
        cout << "File uploaded successfully!\n";
    } else
        cout << "No file :(";

    return 0;
}
