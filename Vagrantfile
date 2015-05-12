# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set nu :

PROJECT_NAME = "lectureswww"

Vagrant.configure(2) do |config|
  sourcecode_dir = './sourcecode/'
  config.vm.synced_folder sourcecode_dir, "/home/vagrant/sourcecode/"
  config.vm.provision :shell,
    run: "always",
    privileged: false,
    :path => "vagrant-data/nginx.sh"

  # Postgres
  config.vm.define 'postgres' do |postgres|
    postgres.vm.provider 'docker' do |docker|
      docker.image = "postgres:9.4"
      docker.name = '%s_db_postgres' % PROJECT_NAME
      docker.ports = ["5433:5432"]
      docker.env = {
        USER: "postgres",
        PASS: "postgres",
      }
    end
  end

  # Redis
  config.vm.define "redis" do |redis|
    redis.vm.provider "docker" do |docker|
      docker.image = "redis"
      docker.name = '%s_db_redis' % PROJECT_NAME
      docker.ports = ["6379:6379"]
    end
  end

  # Memcached
  config.vm.define "memcached" do |memcached|
    memcached.vm.provider "docker" do |docker|
      docker.image = "memcached"
      docker.name = '%s_db_memcached' % PROJECT_NAME
      docker.ports = ["11211:11211"]
    end
  end

  # Nginx with inotify (auto reload)
  config.vm.define "nginx" do |nginx|
    nginx.vm.provider "docker" do |docker|
      docker.build_dir = 'vagrant-data/docker/nginx'
      docker.build_args = ['--tag=uralbash/nginx']
      docker.name = '%s_nginx' % PROJECT_NAME
      docker.ports = ["8080:80"]

      nginx_dir = '%s/sourcecode/nginx' % Dir.pwd
      nginx_html = "%s/html:/usr/share/nginx/html" % nginx_dir
      nginx_sites_enables = "%s/sites-enabled:/etc/nginx/sites-enabled" % nginx_dir
      nginx_includes = "%s/includes:/etc/nginx/includes" % nginx_dir
      docker.volumes = [nginx_sites_enables, nginx_html, nginx_includes]
    end
  end

  # Lecture examples
  config.vm.define 'lectureswww', primary: true do |lectureswww|
    lectureswww.ssh.port = 22
    lectureswww.ssh.username = 'vagrant'
    lectureswww.ssh.password = '123'
    lectureswww.ssh.forward_x11 = true
    lectureswww.vm.provider 'docker' do |docker|
      docker.build_dir = 'vagrant-data/docker/lectureswww'
      docker.name = 'lectureswww'
      docker.build_args = ['--tag=ustu/lectureswww']
      docker.remains_running = false

      docker.link('%s_nginx:nginx' % PROJECT_NAME)
      docker.link('%s_db_redis:redis' % PROJECT_NAME)
      docker.link('%s_db_postgres:postgres' % PROJECT_NAME)
      docker.link('%s_db_memcached:memcached' % PROJECT_NAME)

      # -t - Allocate a (pseudo) tty
      # -i - Keep stdin open (so we can interact with it)
      docker.create_args = ['-i', '-t']
      docker.has_ssh = true

      # HOST:CONTAINER
      docker.ports = ['6543:6543',  # Pyramid
                      '6544:6544',  # Websocket
                      '8000:8000']  # CGI & WSGI
    end
  end
end
