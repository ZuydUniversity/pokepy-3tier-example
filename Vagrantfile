# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Use Ubuntu 22.04 LTS for all VMs
  config.vm.box = "ubuntu/jammy64"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  
  # Database VM
  config.vm.define "db" do |db|
    db.vm.hostname = "pokepy-db"
    db.vm.network "private_network", ip: "192.168.56.10"
    db.vm.network "forwarded_port", guest: 3306, host: 3306, auto_correct: true
    
    db.vm.provider "virtualbox" do |vb|
      vb.name = "pokepy-db-vm"
      vb.memory = "1024"  # 1GB for database
      vb.cpus = 1
    end
    
    db.vm.provision "shell", inline: <<-SHELL
      # Update system
      apt-get update
      apt-get upgrade -y
      
      # Install Docker
      apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
      echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
      apt-get update
      apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
      
      # Install Docker Compose
      DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d'"' -f4)
      curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      chmod +x /usr/local/bin/docker-compose
      
      # Add vagrant user to docker group
      usermod -aG docker vagrant
      
      # Create docker network
      docker network create pokepy_network 2>/dev/null || true
      
      echo "✓ Database VM provisioned"
    SHELL
    
    db.vm.provision "shell", privileged: false, inline: <<-SHELL
      echo "=========================================="
      echo "Database VM (pokepy-db) Ready!"
      echo "=========================================="
      echo "IP Address: 192.168.56.10"
      echo "Port: 3306 (mapped to host port 3306)"
      echo ""
      echo "To start database:"
      echo "  cd /vagrant"
      echo "  docker compose up -d pokepy-mariadb"
    SHELL
  end
  
  # Backend VM
  config.vm.define "backend" do |backend|
    backend.vm.hostname = "pokepy-backend"
    backend.vm.network "private_network", ip: "192.168.56.20"
    backend.vm.network "forwarded_port", guest: 8000, host: 8000, auto_correct: true
    
    backend.vm.provider "virtualbox" do |vb|
      vb.name = "pokepy-backend-vm"
      vb.memory = "1536"  # 1.5GB for backend
      vb.cpus = 2
    end
    
    backend.vm.provision "shell", inline: <<-SHELL
      # Update system
      apt-get update
      apt-get upgrade -y
      
      # Install dependencies
      apt-get install -y libmariadb3 libmariadb-dev gcc
      
      # Install Docker
      apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
      echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
      apt-get update
      apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
      
      # Install Docker Compose
      DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d'"' -f4)
      curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      chmod +x /usr/local/bin/docker-compose
      
      # Install Python
      apt-get install -y python3 python3-venv python3-pip
      
      # Install Git and Make
      apt-get install -y git make
      
      # Add vagrant user to docker group
      usermod -aG docker vagrant
      
      # Create docker network
      docker network create pokepy_network 2>/dev/null || true
      
      echo "✓ Backend VM provisioned"
    SHELL
    
    backend.vm.provision "shell", privileged: false, inline: <<-SHELL
      echo "=========================================="
      echo "Backend VM (pokepy-backend) Ready!"
      echo "=========================================="
      echo "IP Address: 192.168.56.20"
      echo "Port: 8000 (mapped to host port 8000)"
      echo ""
      echo "To start backend:"
      echo "  cd /vagrant"
      echo "  docker compose up -d pokepy-backend"
      echo ""
      echo "Access API docs at:"
      echo "  http://localhost:8000/docs"
    SHELL
  end
  
  # Frontend VM
  config.vm.define "frontend" do |frontend|
    frontend.vm.hostname = "pokepy-frontend"
    frontend.vm.network "private_network", ip: "192.168.56.30"
    frontend.vm.network "forwarded_port", guest: 3000, host: 3000, auto_correct: true
    
    frontend.vm.provider "virtualbox" do |vb|
      vb.name = "pokepy-frontend-vm"
      vb.memory = "1024"  # 1GB for frontend
      vb.cpus = 1
    end
    
    frontend.vm.provision "shell", inline: <<-SHELL
      # Update system
      apt-get update
      apt-get upgrade -y
      
      # Install Node.js
      curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
      apt-get install -y nodejs
      
      # Install Docker
      apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
      echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
      apt-get update
      apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
      
      # Install Docker Compose
      DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d'"' -f4)
      curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      chmod +x /usr/local/bin/docker-compose
      
      # Install Git and Make
      apt-get install -y git make
      
      # Add vagrant user to docker group
      usermod -aG docker vagrant
      
      # Create docker network
      docker network create pokepy_network 2>/dev/null || true
      
      echo "✓ Frontend VM provisioned"
    SHELL
    
    frontend.vm.provision "shell", privileged: false, inline: <<-SHELL
      echo "=========================================="
      echo "Frontend VM (pokepy-frontend) Ready!"
      echo "=========================================="
      echo "IP Address: 192.168.56.30"
      echo "Port: 3000 (mapped to host port 3000)"
      echo ""
      echo "To start frontend:"
      echo "  cd /vagrant"
      echo "  docker compose up -d pokepy-frontend"
      echo ""
      echo "Access frontend at:"
      echo "  http://localhost:3000"
    SHELL
  end
end

