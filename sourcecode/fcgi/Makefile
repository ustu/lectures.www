hello:
	g++ -o hello.fcgi hello.cpp -lfcgi++ -lfcgi

run:
	spawn-fcgi -p 5000 -n hello.fcgi
