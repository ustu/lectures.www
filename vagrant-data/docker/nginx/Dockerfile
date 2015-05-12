# nginx
#
# VERSION               0.0.3
# vi: set ft=Dockerfile :
# vi: set nu :

FROM ubuntu
MAINTAINER Dmitry Svintsov <root@uralbash.ru>

# Add packages
RUN apt-get install -y software-properties-common
# Install Nginx.
RUN \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx inotify-tools && \
  rm -rf /var/lib/apt/lists/* && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
WORKDIR /etc/nginx

# Add inotify.sh to execute during container startup
RUN mkdir -p /etc/service/inotify
ADD inotify.sh /etc/service/inotify/run
RUN chmod +x /etc/service/inotify/run
ENTRYPOINT ["/etc/service/inotify/run"]

# Nginx as deamon
RUN sed -i "s/daemon off/daemon on/" nginx.conf

# Expose ports.
EXPOSE 80
EXPOSE 443
