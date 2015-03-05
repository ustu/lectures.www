# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set nu :

PROJECT_NAME = "lectureswww"

Vagrant.configure(2) do |config|
  sourcecode_dir = './sourcecode/'
  config.vm.synced_folder sourcecode_dir, "/home/vagrant/sourcecode/"

  # Lecture examples
  config.vm.define 'lectureswww', primary: true do |lectureswww|
    lectureswww.ssh.port = 22
    lectureswww.ssh.username = 'vagrant'
    lectureswww.ssh.password = '123'
    lectureswww.vm.provider 'docker' do |docker|
      docker.build_dir = '.'
      docker.name = 'lectureswww'
      docker.build_args = ['--tag=ustu/lectureswww']
      docker.remains_running = false

      # telnet redis 6379
      docker.link('%s_db_redis:redis' % PROJECT_NAME)
      # telnet postgres 5432
      docker.link('%s_db_postgres:postgres' % PROJECT_NAME)

      # -t - Allocate a (pseudo) tty
      # -i - Keep stdin open (so we can interact with it)
      docker.create_args = ['-i', '-t']
      docker.has_ssh = true

      # HOST:CONTAINER
      # Pyramid
      docker.ports = ['6543:6543', '6544:6544']
      # CGI & WSGI
      docker.ports = ['8000:8000', '8080:8080']
    end
  end

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
      docker.image = "dockerfile/redis"
      docker.name = '%s_db_redis' % PROJECT_NAME
      docker.ports = ["6379:6379"]
    end
  end
end
