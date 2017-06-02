# Sphinx-docs
#
# VERSION               0.0.1
# vi: set ft=dockerfile :

FROM uralbash/sphinx-doc:latest
MAINTAINER Dmitry Svintsov <root@uralbash.ru>

RUN apt-get install -y git
RUN pip install sphinx ipython sphinx_links
RUN pip install git+https://bitbucket.org/zzzeek/zzzeeksphinx
