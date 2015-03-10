#!/usr/bin/env ruby
#
# 1.hello.rb
# Copyright (C) 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

sleep 10

puts "Content-type:text/html\r\n\r\n"
puts '<html>'
puts '<head>'
puts '<title>Hello Word - First CGI Program</title>'
puts '</head>'
puts '<body>'
puts '<h2>Hello Word! This is my first CGI program</h2>'
puts '</body>'
puts '</html>'
