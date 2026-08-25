# FinGuard AI — Intelligent Financial Transaction Risk Detection, Fraud Investigation & MLOps Platform

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-teal.svg)](https://fastapi.tiangolo.com/)
[![LightGBM](https://img.shields.io/badge/LightGBM-4.3.0-orange.svg)](https://lightgbm.readthedocs.io/)
[![React: 18](https://img.shields.io/badge/React-18-blue.svg)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38bdf8.svg)](https://tailwindcss.com/)

**FinGuard AI** is an enterprise-grade financial fraud detection, multi-signal risk decisioning, analyst investigation, and MLOps platform built for banks, fintechs, and payment processors.

---

## Installation

Ensure you have Python 3.10+, Node.js, and Docker installed.

```bash
# Setup Python virtual environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Setup Frontend dependencies
cd frontend
npm install
cd ..
```

## Build

To build the full application container and frontend bundles:

```bash
# Build Docker images
docker compose build

# Build Frontend production bundle
cd frontend
npm run build
cd ..
```

## Run

To start the complete platform:

```bash
# Start all services with Docker Compose
docker compose up -d

# Generate synthetic transaction dataset
python scripts/generate_data.py --transactions 50000

# Run automated tests
pytest tests/ -v
```

## Dependencies

The system requires:
- **Backend**: Python 3.10+, FastAPI, Pydantic v2, SQLAlchemy 2.0, PostgreSQL, Redis, Celery, LightGBM, Scikit-learn
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, TanStack Query, Recharts
- **Infrastructure**: Docker, Docker Compose, Terraform

All requirements are declared in `requirements.txt`, `pyproject.toml`, and `package.json`.

## Usage

1. Open the API Documentation: `http://localhost:8000/docs`
2. Access the Risk Intelligence Dashboard: `http://localhost:5173`
3. Execute codebase verification: `python scripts/count_loc.py`
