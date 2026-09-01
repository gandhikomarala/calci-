# Calci Studio — Scientific RPN & Loan Amortization Suite

Calci Studio — Scientific RPN & Loan Amortization Suite is a production-grade enterprise application designed with domain-driven architecture, automated quality validation, and high-performance microservices.

---

## Dependencies

* **Runtime**: Python 3.10+ / Node.js 18+
* **Framework**: FastAPI, Uvicorn, Pydantic v2
* **Quality & Test**: Pytest, Pytest-cov
* **Frontend**: HTML5 Canvas / ES6+, Zero-Dependency Web Client

---

## Installation

### 1. Set Up Python Virtual Environment
```bash
git clone git@github.com:gandhikomarala/calci-.git
cd calci_dash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Build

Build containerized production image locally:
```bash
docker build -t calci_dash:latest .
```

---

## Run

### Microservice Execution
```bash
python -m uvicorn Backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### Containerized Orchestration
```bash
docker-compose up -d --build
```

### Static Web UI
```bash
python -m http.server 8000
```

---

## Usage

1. Access the web dashboard via `http://localhost:8000` or the live GitHub Pages link.
2. Interact with the core domain engine, real-time analytics, and data persistence layers.

---

## Testing

Execute the automated test suite with coverage report:
```bash
pytest tests/ -v
```
