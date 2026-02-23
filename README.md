# PokePy - 3-Tier Pokemon Application

A full-stack application for browsing and managing Pokemon data. Built with **Python/FastAPI** backend, **Next.js** frontend, and **MariaDB** database.

## 📋 Architecture

```
┌─────────────────────────────────────┐
│  Frontend (Next.js/React)           │
│  - Port: 3000                       │
│  - Docker image: pokepy-frontend    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Backend (FastAPI/Python)           │
│  - Port: 8000                       │
│  - Docker image: pokepy-backend     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Database (MariaDB)                 │
│  - Port: 3306                       │
└─────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git
- Node.js 20.x (for frontend local dev)
- Python 3.x (for backend local dev)

### Option 1: Docker (Recommended)

```bash
# Start entire stack
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
```

Services will be available at:
- **Frontend**: http://localhost:81
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Option 2: Vagrant VM

Don't have Docker installed? Use Vagrant to run everything in a virtual machine:

```bash
# Start VM and provision Docker
vagrant up

# SSH into the VM
vagrant ssh

# Inside the VM, run:
cd /vagrant
docker compose up -d
```

See [VAGRANT.md](./VAGRANT.md) for detailed instructions.

### Option 3: Local Development (No Docker)

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn src.main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

```
pokemon-3-tier/
├── backend/                    # FastAPI application
│   ├── src/
│   │   ├── main.py            # Entry point
│   │   ├── config_reader.py   # Configuration
│   │   └── pokemon/           # Pokemon domain
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile
│   └── openapi.yaml           # API specification
│
├── frontend/                   # Next.js application
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── lib/
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
│
├── db/                         # Database
│   ├── init.sql               # Schema initialization
│   ├── Dockerfile
│   └── data/
│
├── .github/
│   └── workflows/             # CI/CD pipelines
│       ├── backend-build.yml  # Backend build & push
│       └── frontend-build.yml # Frontend build & push
│
├── docker-compose.yml
└── README.md
```

## 🔄 CI/CD Pipeline

This repo uses **GitHub Actions** for automated builds and deployments.

### Workflows
- **Backend**: Triggers on changes to `/backend` → Builds and pushes Docker image
- **Frontend**: Triggers on changes to `/frontend` → Builds and pushes Docker image
- **Deploy**: Triggers on release → Deploys to Azure VM

Each workflow only runs when its respective folder changes (path-based filtering).

## 📦 Docker Images

Published to Docker Hub:
- `donovicv/pokepy-backend:latest`
- `donovicv/pokepy-frontend:latest`

## 🔐 Environment Variables

### Backend (`backend/config.ini`)
```ini
[database]
host = db
port = 3306
user = root
password = your_password
database = pokemon
```

### Frontend (`.env.development`)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🧪 Testing

### Backend
```bash
cd backend
pytest ./src/tests/
```

### Frontend
```bash
cd frontend
npm test
```

## 📝 API Documentation

Interactive API docs available at: `http://localhost:8000/docs`

API Collection: See `/backend/postman/PokePy.postman_collection.json`

## 📚 Documentation

- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Development setup, code standards, and PR process
- **[VAGRANT.md](./VAGRANT.md)** - Running the app in a virtual machine with Vagrant
- **[Makefile](./Makefile)** - Build and run commands - `make help` to see all options
- **[docker-compose.yml](./docker-compose.yml)** - Service configuration and networking

## 🤝 Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.

## 📄 License

See [LICENSE](./backend/LICENSE)

## 👤 Authors

- **Your Name** - Initial work

---

**Questions?** Open an issue or check the individual service READMEs in `backend/` and `frontend/` folders.
