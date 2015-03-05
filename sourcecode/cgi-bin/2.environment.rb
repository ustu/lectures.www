#!/usr/bin/env ruby
#
# 2.environment.rb
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#

print "Content-type: text/html\r\n\r\n"
print "<font size=+10>Environment</font><br>"

for param in ENV
    print "<b>%20s</b>: %s<br>" % param
end
