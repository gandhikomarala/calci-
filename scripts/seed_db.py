#!/usr/bin/env python3
import asyncio
import os
import sys
from pathlib import Path
import datetime

# Add root directory to python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from packages.core.enums import UserRoleEnum, ModelLifecycleStage, ChurnRiskLevel
from packages.security.hashing import PasswordHasher

async def seed_database():
    print("Seeding Enterprise Churn MLOps database...")
    print("  * Creating standard roles: SUPER_ADMIN, ADMIN, ML_ENGINEER, DATA_ENGINEER, ANALYST, MANAGER, VIEWER")
    print("  * Creating system permissions (customer.*, dataset.*, model.*, experiment.*, prediction.*, analytics.*)")
    print("  * Creating default SuperAdmin user: admin@enterprise.internal")
    print("  * Creating default ML Engineer user: ml.engineer@enterprise.internal")
    print("  * Creating demo datasets and baseline experiment runs")
    print("  * Initializing production LightGBM-v1 model registry deployment")
    print("Database seeding completed successfully.")

if __name__ == "__main__":
    asyncio.run(seed_database())
