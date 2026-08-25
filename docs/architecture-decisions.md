# Architecture Decision Records (ADRs)

## Overview
Key architectural trade-offs: Async FastAPI vs Sync, LightGBM vs Deep Learning, PostgreSQL + Redis vs Graph DBs.

## Key Specifications & Implementation
FinGuard AI provides enterprise-grade capabilities designed for mission-critical financial fraud operations.

### Architectural Highlights
- **Asynchronous Micro-Architecture**: High-throughput FastAPI gateway backed by PostgreSQL 16 connection pooling and Redis 7 message brokers.
- **Explainable Machine Learning**: Sub-millisecond LightGBM GBDT inference coupled with TreeSHAP factor attributions.
- **Configurable Multi-Signal Risk Engine**: Dynamic rules combined with statistical anomaly detection and behavioral velocity indicators.
- **Analyst Investigation Dossier**: Complete audit trail, evidence management, and human-in-the-loop decisioning.

### Configuration Reference
Refer to `.env.example` and `backend/core/config.py` for full environment settings.
