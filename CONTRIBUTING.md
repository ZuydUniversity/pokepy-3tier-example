# Contributing to PokePy

Thank you for your interest in contributing! This guide explains how to set up your development environment and contribute to the project.

## 📋 Prerequisites

- **Git** - Version control
- **Docker & Docker Compose** - For running the full stack
- **Python 3.x** - Backend requirements
- **Node.js 20.x** - Frontend requirements

## 🛠️ Local Setup

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/your-repo/pokemon-3-tier.git
cd pokemon-3-tier

# Start the entire stack with Docker Compose
docker compose -f docker-compose-local.yml up -d
```

### 2. Backend Development

```bash
cd backend

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Test your changes:
```bash
pytest ./src/tests/ -v
flake8 ./src/
```

### 3. Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will be available at: `http://localhost:3000`

## 📝 Code Standards

### Python (Backend)
- **Linter**: flake8
- **Line Length**: 127 characters max
- **Naming**: snake_case for functions/variables
- **Type Hints**: Encouraged for new code

```bash
# Run linter
flake8 ./src/

# Run tests
pytest ./src/tests/
```

### TypeScript/JavaScript (Frontend)
- **Linter**: ESLint (see `.eslintrc.json`)
- **Formatter**: Prettier (configured in `next.config.mjs`)
- **Naming**: camelCase for variables/functions, PascalCase for components

```bash
# Run ESLint
npm run lint

# Format code
npm run format
```

## 🔄 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Keep commits atomic and descriptive
   - Follow the commit message format below

3. **Write tests**
   - Backend: Add tests to `backend/src/tests/`
   - Frontend: Add tests alongside components

4. **Lint and test locally**
   - `cd backend && pytest && flake8 ./src/`
   - `cd frontend && npm run lint`

5. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Wait for CI/CD**
   - GitHub Actions will automatically run tests
   - Address any failures in CI

## 💬 Commit Message Format

Follow this format for clear history:

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types**:
- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation changes
- `refactor:` Code refactoring without feature change
- `test:` Adding or updating tests
- `chore:` Dependency updates, tooling changes

**Examples**:
```
feat: add Pokemon search filter
fix: resolve database connection timeout
docs: update API endpoint documentation
```

## 🧪 Testing Requirements

- **Backend**: All new functions must have tests (90%+ coverage expected)
- **Frontend**: Components should have unit tests where practical
- Run `pytest` locally before pushing

## 🐛 Bug Reports

Include:
1. Steps to reproduce
2. Expected behavior vs actual behavior
3. Screenshots if applicable
4. Environment details (OS, Python/Node version, etc.)

## 📚 Architecture Notes

- Backend serves REST API on port 8000
- Frontend (Next.js) communicates via `NEXT_PUBLIC_API_URL`
- Database scripts in `db/init.sql`
- All Docker images pushed to Docker Hub on merge to `main`

## 🚀 Deployment

Deployments are **automated** via GitHub Actions:
- Any push to `backend/` → builds and pushes `pokepy-backend:latest`
- Any push to `frontend/` → builds and pushes `pokepy-frontend:latest`
- Any release (tag) → deploys to Azure VM

## 🤔 Questions?

- Check existing issues: https://github.com/your-repo/pokemon-3-tier/issues
- Open a new issue with your question
- Use descriptive titles for better searchability

---

**Thank you for contributing!** 🎉
