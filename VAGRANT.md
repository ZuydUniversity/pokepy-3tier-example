# Running PokePy with Vagrant (Multi-Machine Setup)

This Vagrantfile sets up **3 separate virtual machines** for the PokePy 3-tier application:

| VM | Role | IP | Memory | CPUs | Ports |
|---|---|---|---|---|---|
| **db** | Database (MariaDB) | 192.168.56.10 | 1 GB | 1 | 3306 |
| **backend** | Backend API (FastAPI) | 192.168.56.20 | 1.5 GB | 2 | 8000 |
| **frontend** | Frontend (Next.js) | 192.168.56.30 | 1 GB | 1 | 3000 |

## Prerequisites

Install these tools on your Windows/Mac/Linux machine:

1. **VirtualBox** - https://www.virtualbox.org/wiki/Downloads
2. **Vagrant** - https://www.vagrantup.com/downloads

Verify installation:
```bash
vagrant --version
vboxmanage --version
```

## Quick Start

### 1. Start All VMs
```bash
# From the project root directory
vagrant up
```

This will start all 3 VMs and install Docker on each. **First time takes ~10-15 minutes**

### 2. Start Individual VMs
```bash
# Start only database
vagrant up db

# Start only backend
vagrant up backend

# Start only frontend
vagrant up frontend
```

### 3. SSH into a Specific VM
```bash
# Connect to database VM
vagrant ssh db

# Connect to backend VM
vagrant ssh backend

# Connect to frontend VM
vagrant ssh frontend
```

### 4. Run Services

Inside each VM, run Docker Compose to start the service:

#### Database VM
```bash
vagrant ssh db
cd /vagrant
docker compose up -d pokepy-mariadb
```

#### Backend VM
```bash
vagrant ssh backend
cd /vagrant
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

#### Frontend VM
```bash
vagrant ssh frontend
cd /vagrant
npm run dev
```

### 5. Access Services

| Service | URL | VM | Port |
|---------|-----|----|----|
| **Frontend** | http://localhost:3000 | frontend | 3000 |
| **Backend API** | http://localhost:8000 | backend | 8000 |
| **API Docs** | http://localhost:8000/docs | backend | 8000 |
| **Database** | localhost:3306 | db | 3306 |

## Common Commands

### VM Management
```bash
# Start all VMs
vagrant up

# Start specific VM
vagrant up db
vagrant up backend
vagrant up frontend

# SSH into VM
vagrant ssh db
vagrant ssh backend
vagrant ssh frontend

# Stop all VMs (keeps data)
vagrant halt

# Stop specific VM
vagrant halt db
vagrant halt backend

# Resume all VMs
vagrant resume

# Restart all VMs
vagrant reload

# Destroy all VMs (cleanup)
vagrant destroy

# Check status of all VMs
vagrant status

# Check status of specific VM
vagrant status backend
```

### Inside the VMs
```bash
# View logs for a service
docker compose logs -f pokepy-backend

# Check running containers
docker compose ps

# Rebuild a service
docker compose build pokepy-database
docker compose build pokepy-backend
docker compose build pokepy-frontend

# Stop a service
docker compose down pokepy-frontend
```

## VM Specifications

Each VM independently has:
- **OS**: Ubuntu 22.04 LTS
- **Docker**: Pre-installed
- **Docker Compose**: Pre-installed
- **Git**: Pre-installed
- **Networking**: Private network 192.168.56.0/24

### Database VM
- IP: 192.168.56.10
- Memory: 1 GB
- CPUs: 1
- Hostname: pokepy-db

### Backend VM
- IP: 192.168.56.20
- Memory: 1.5 GB
- CPUs: 2
- Hostname: pokepy-backend
- Includes: Python 3, libmariadb-dev

### Frontend VM
- IP: 192.168.56.30
- Memory: 1 GB
- CPUs: 1
- Hostname: pokepy-frontend
- Includes: Node.js 20.x

## Networking

The VMs can communicate with each other via private network:

- **Database hostname** (from backend): `pokepy-db` or `192.168.56.10`
- **Backend hostname** (from frontend): `pokepy-backend` or `192.168.56.20`
- **Frontend hostname**: `pokepy-frontend` or `192.168.56.30`

Update your Docker Compose or app config to use these hostnames or IPs when connecting between services.

## Customizing VMs

Edit the `Vagrantfile` to change resources:

```ruby
# For more memory on backend:
backend.vm.provider "virtualbox" do |vb|
  vb.memory = "2048"   # Increase to 2GB
  vb.cpus = 4          # Add more cores
end
```

Then reload:
```bash
vagrant reload backend
```

## Running All Services Across VMs

### Method 1: Manual Docker Starts
```bash
# Terminal 1: Start database
vagrant ssh db
cd /vagrant && docker compose up -d pokepy-mariadb

# Terminal 2: Start backend
vagrant ssh backend
cd /vagrant && docker compose up -d pokepy-backend

# Terminal 3: Start frontend
vagrant ssh frontend
cd /vagrant && docker compose up -d pokepy-frontend
```

### Method 2: Using Make Commands
Each VM has `make` installed, so you can use:

```bash
# In backend VM
vagrant ssh backend
cd /vagrant
make build-backend
docker compose up -d pokepy-backend

# In frontend VM
vagrant ssh frontend
cd /vagrant
make build-frontend
docker compose up -d pokepy-frontend
```

## Troubleshooting

### VM won't start
```bash
# Try destroying and recreating
vagrant destroy db
vagrant up db
```

### Port conflicts
If ports 3000, 8000, or 3306 are in use, edit Vagrantfile:
```ruby
db.vm.network "forwarded_port", guest: 3306, host: 3307  # Change 3306 to 3307
backend.vm.network "forwarded_port", guest: 8000, host: 8001
frontend.vm.network "forwarded_port", guest: 3000, host: 3001
```

Then:
```bash
vagrant reload
```

### Can't access services from host
Ensure the VM is running:
```bash
vagrant status
```

Check if Docker container is running inside the VM:
```bash
vagrant ssh backend
docker compose ps
```

### Services can't communicate
Verify VMs are on the same network:
```bash
vagrant ssh backend
ping pokepy-db  # Should work
```

If not, check Docker network:
```bash
docker network ls
docker network inspect pokepy_network
```

### Out of disk space
Vagrant VMs can accumulate large images. Clean up:
```bash
vagrant destroy
rm -rf .vagrant
vagrant up
```

## Performance Tips

### Slow Sync on Windows/Mac?
The virtualbox synced folder can be slow. Use rsync:

In Vagrantfile, for each VM:
```ruby
config.vm.synced_folder ".", "/vagrant", type: "rsync"
```

Then sync manually:
```bash
vagrant rsync
vagrant rsync-auto  # Auto-sync on changes
```

### Reduce Memory Usage
Decrease VM memory in Vagrantfile:
```ruby
db.vm.provider "virtualbox" do |vb|
  vb.memory = "512"   # Reduce to 512MB
end
```

## Destroying Everything

When done:
```bash
# Stop all VMs
vagrant halt

# Completely remove all VMs and data
vagrant destroy

# Optional: Remove the vagrant box image
vagrant box remove ubuntu/jammy64
```

## Next Steps

After VMs are set up and services are running:

1. **Test the API**: http://localhost:8000/docs
2. **Access Frontend**: http://localhost:3000
3. **Read Contributing Guide**: See [CONTRIBUTING.md](../CONTRIBUTING.md)
4. **Run Tests**: `cd /vagrant && make test`
5. **Check Logs**: `docker compose logs -f`

---

**Questions?** Check the main [README.md](../README.md) or [CONTRIBUTING.md](../CONTRIBUTING.md).
