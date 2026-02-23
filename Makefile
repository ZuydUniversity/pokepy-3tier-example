.PHONY: help install install-hooks build build-backend build-frontend build-db up down logs lint test clean clean-all

help:
	@echo "PokePy Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install          Install all dependencies + Git hooks"
	@echo "  make install-hooks    Refresh Git hooks (pre-commit, pre-push)"
	@echo ""
	@echo "Building:"
	@echo "  make build            Build all Docker images (backend, frontend, db)"
	@echo "  make build-backend    Build backend image only"
	@echo "  make build-frontend   Build frontend image only"
	@echo "  make build-db         Build database image only"
	@echo ""
	@echo "Running:"
	@echo "  make up               Build and start all services"
	@echo "  make up-nobuild       Start services (skip build)"
	@echo "  make down             Stop all services"
	@echo "  make logs             View logs from all services"
	@echo ""
	@echo "Development:"
	@echo "  make backend-dev      Start backend dev server (requires venv setup)"
	@echo "  make frontend-dev     Start frontend dev server"
	@echo ""
	@echo "Testing & Linting:"
	@echo "  make test             Run all tests"
	@echo "  make test-backend     Run backend tests"
	@echo "  make test-frontend    Run frontend tests"
	@echo "  make lint             Run linters"
	@echo "  make lint-backend     Lint backend code"
	@echo "  make lint-frontend    Lint frontend code"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean            Remove containers and volumes"
	@echo "  make clean-all        Remove everything including images"

# Docker build commands
build:
	@echo "🔨 Building all Docker images..."
	docker compose build
	@echo "✓ All images built successfully"

build-backend:
	@echo "🔨 Building backend image..."
	docker compose build pokepy-backend
	@echo "✓ Backend image built"

build-frontend:
	@echo "🔨 Building frontend image..."
	docker compose build pokepy-frontend
	@echo "✓ Frontend image built"

build-db:
	@echo "🔨 Building database image..."
	docker compose build pokepy-mariadb
	@echo "✓ Database image built"

# Docker Compose commands
up: build
	@echo "🚀 Starting all services..."
	docker compose up -d
	@echo "✓ Services started"
	@echo "  Frontend: http://localhost:81"
	@echo "  Backend:  http://localhost:8000"
	@echo "  API Docs: http://localhost:8000/docs"
	@echo "  Database: localhost:3306"

up-nobuild:
	@echo "🚀 Starting services (without rebuild)..."
	docker compose up -d
	@echo "✓ Services started"
	@echo "  Frontend: http://localhost:81"
	@echo "  Backend:  http://localhost:8000"
	@echo "  API Docs: http://localhost:8000/docs"
	@echo "  Database: localhost:3306"

down:
	docker compose down
	@echo "✓ Services stopped"

logs:
	docker compose logs -f

clean:
	docker compose down -v
	@echo "✓ Containers and volumes removed"

clean-all: clean
	docker compose down -v --remove-orphans --rmi all
	@echo "✓ All containers, volumes, and images removed"

# Backend setup and development
install:
	@echo "Installing backend dependencies..."
	cd backend && python -m venv venv
	cd backend && venv/Scripts/pip install -r requirements.txt
	@echo "✓ Backend dependencies installed"
	@echo ""
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✓ Frontend dependencies installed"
	@echo ""
	@echo "Setting up Git hooks..."
	cd frontend && npm run prepare
	@echo "✓ Git hooks installed (pre-commit, pre-push)"

install-hooks:
	@echo "Installing/refreshing Git hooks..."
	cd frontend && npm run prepare
	@echo "✓ Git hooks updated"

backend-dev:
	cd backend && venv/Scripts/python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

frontend-dev:
	cd frontend && npm run dev

# Testing
test: test-backend test-frontend
	@echo "✓ All tests passed"

test-backend:
	@echo "Running backend tests..."
	cd backend && venv/Scripts/pytest ./src/tests/ -v

test-frontend:
	@echo "Running frontend tests..."
	cd frontend && npm test -- --coverage

# Linting
lint: lint-backend lint-frontend
	@echo "✓ All linting passed"

lint-backend:
	@echo "Linting backend..."
	cd backend && venv/Scripts/flake8 ./src/ --count --statistics

lint-frontend:
	@echo "Linting frontend..."
	cd frontend && npm run lint

# Utility
ps:
	docker compose ps

shell-backend:
	docker compose exec backend /bin/bash

shell-frontend:
	docker compose exec frontend /bin/sh

shell-db:
	docker compose exec db mysql -u root -p pokemon
