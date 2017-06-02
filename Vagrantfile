# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set nu :

PROJECT_NAME = "lectureswww"
LECTURES = ENV["LECTURES"]

Vagrant.configure(2) do |config|
  config.vm.synced_folder ".",
      "/home/vagrant/lectures/"

  # Lectures docs
  config.vm.define 'lectures', primary: true do |lectures|

    lectures.ssh.port = 22
    lectures.ssh.username = 'vagrant'
    lectures.ssh.password = '123'

    lectures.vm.provision :shell, privileged: false,
      :path => "vagrant/docker/lectures/build-docs.sh",
      :env => {LECTURES: LECTURES}

    lectures.vm.provider 'docker' do |docker|
      docker.name = PROJECT_NAME
      docker.build_dir = './vagrant/docker/lectures/'
      docker.build_args = ['--tag=ustu/lectureswww']
      docker.remains_running = false

      # -t - Allocate a (pseudo) tty
      # -i - Keep stdin open (so we can interact with it)
      docker.create_args = ['-i', '-t']
      docker.has_ssh = true
    end
  end
end
