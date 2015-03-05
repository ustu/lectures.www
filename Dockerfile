# healthdesk
#
# VERSION               0.0.1
# vi: set ft=Dockerfile :
# vi: set nu :

FROM uralbash/docker-ubuntu:latest
MAINTAINER Dmitry Svintsov <root@uralbash.ru>

## Set LOCALE
RUN apt-get -qqy install ruby-full libcgicc5-dev
