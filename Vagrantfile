# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
    config.vm.box = "alvistack/ubuntu-22.04"

    # via 127.0.0.1 to disable public access
    config.vm.network "forwarded_port", guest: 6379, host: 6379, host_ip: "127.0.0.1"

    # argument is a set of non-required options.
    # config.vm.synced_folder "../data", "/vagrant_data"

    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "8192"
      vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
      vb.customize [ "modifyvm", :id, "--uartmode1", "file", File::NULL ]
      vb.customize [ "modifyvm", :id, "--uart1", "0x3F8", "4" ]
      vb.customize [ "modifyvm", :id, "--cableconnected1", "on" ]
    end

    config.vm.provision "shell", inline: <<-SHELL
      apt-get update
    SHELL
  end
