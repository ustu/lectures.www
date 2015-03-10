# healthdesk
#
# VERSION               0.0.1
# vi: set ft=Dockerfile :
# vi: set nu :

FROM uralbash/docker-ubuntu:latest
MAINTAINER Dmitry Svintsov <root@uralbash.ru>

## Ruby
RUN apt-get -qqy install ruby-full
## CGI & FastCGI for C++
RUN apt-get -qqy install libfcgi-dev libcgicc5-dev spawn-fcgi
## For gvm - Golang version manager
RUN apt-get install -qqy bison

USER vagrant

## Golang
RUN wget https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer -O /tmp/gvm-installer.sh
RUN chmod +x /tmp/gvm-installer.sh
RUN /tmp/gvm-installer.sh

ADD install_go.sh /tmp/install_go.sh
RUN /tmp/install_go.sh

USER root
