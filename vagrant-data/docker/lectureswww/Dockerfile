# lectureswww
#
# VERSION               0.0.1
# vi: set ft=Dockerfile :
# vi: set nu :

FROM uralbash/docker-ubuntu-ru:latest
MAINTAINER Dmitry Svintsov <root@uralbash.ru>

## apt-get install
# Ruby
RUN apt-get -qqy install ruby-full
# CGI & FastCGI for C++
RUN apt-get -qqy install libfcgi-dev libcgicc5-dev spawn-fcgi
# For gvm - Golang version manager
RUN apt-get install -qqy bison
# SQLite
RUN apt-get install -qqy sqlite
# Memcached
RUN apt-get install -qqy libmemcached-dev zlib1g-dev libssl-dev

USER vagrant

## Python
ADD install_py.sh /tmp/install_py.sh
RUN /tmp/install_py.sh

## Golang
RUN wget https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer -O /tmp/gvm-installer.sh
RUN chmod +x /tmp/gvm-installer.sh
RUN /tmp/gvm-installer.sh
ADD install_go.sh /tmp/install_go.sh
RUN /tmp/install_go.sh

## nodejs + iojs
RUN wget https://raw.githubusercontent.com/creationix/nvm/v0.24.0/install.sh -O /tmp/nvm-installer.sh
RUN chmod +x /tmp/nvm-installer.sh
RUN /tmp/nvm-installer.sh
ADD install_js.sh /tmp/install_js.sh
RUN /tmp/install_js.sh

USER root
