hello:
	g++ -o hello.fcgi hello.cpp -lfcgi++ -lfcgi

hello_go:
	go build -o hello.go.fcgi hello.go

run:
	spawn-fcgi -p 5000 -n hello.fcgi
