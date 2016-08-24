# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set nu :

PROJECT_NAME = "lectureswww"
LECTURES = ENV["LECTURES"]

Vagrant.configure(2) do |config|
  config.vm.synced_folder ".",
      "/home/vagrant/lectureswww/"

  # Lectures docs
  config.vm.define 'lectureswww', primary: true do |lectureswww|

    lectureswww.ssh.port = 22
    lectureswww.ssh.username = 'vagrant'
    lectureswww.ssh.password = '123'

    lectureswww.vm.provision :shell, privileged: false,
      :path => "vagrant/docker/lectureswww/build-docs.sh",
      :env => {LECTURES: LECTURES}

    lectureswww.vm.provider 'docker' do |docker|
      docker.name = PROJECT_NAME
      docker.build_dir = './vagrant/docker/lectureswww/'
      docker.build_args = ['--tag=ustu/lectureswww']
      docker.remains_running = false

      # -t - Allocate a (pseudo) tty
      # -i - Keep stdin open (so we can interact with it)
      docker.create_args = ['-i', '-t']
      docker.has_ssh = true
    end
  end
end
