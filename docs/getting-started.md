# FinGuard AI — Getting Started Guide

## Prerequisites
- Python >= 3.10
- Node.js >= 20.0
- Docker & Docker Compose
- PostgreSQL 16
- Redis 7

## Local Setup
```bash
# 1. Clone repository & configure environment
cp .env.example .env

# 2. Start PostgreSQL & Redis via Docker
docker compose up -d postgres redis

# 3. Generate synthetic transactions
python scripts/generate_data.py --transactions 10000

# 4. Run automated test suite
pytest tests/ -v

# 5. Measure codebase metrics
python scripts/count_loc.py
```
