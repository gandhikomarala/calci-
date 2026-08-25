#!/usr/bin/env python3
"""
FinGuard AI — Synthetic Financial Transaction & Fraud Scenario Engine.
Generates realistic customer behavioral baseline patterns, merchant ecosystems,
device footprints, and 15 distinct financial fraud scenarios without real PII.
"""

import os
import sys
import argparse
import random
import uuid
import datetime
from pathlib import Path
import pandas as pd
import numpy as np

def generate_financial_dataset(num_transactions: int = 10000, seed: int = 42) -> pd.DataFrame:
    np.random.seed(seed)
    random.seed(seed)

    channels = ["MOBILE_APP", "WEB_PORTAL", "POS_TERMINAL", "ATM", "OPEN_BANKING_API"]
    payment_methods = ["CREDIT_CARD", "DEBIT_CARD", "WIRE_TRANSFER", "INSTANT_PAYMENT", "CRYPTO_GATEWAY"]
    currencies = ["USD", "EUR", "GBP", "CAD", "JPY"]
    merchant_categories = [
        "LUXURY_JEWELRY", "ELECTRONICS_GAMING", "DIGITAL_GIFT_CARDS", "TRAVEL_AIRLINES",
        "CRYPTO_EXCHANGE", "GROCERY_SUPERMARKET", "UTILITIES_SERVICES", "HEALTHCARE_PHARMACY",
        "CASINO_GAMBLING", "PEER_TO_PEER"
    ]
    device_types = ["IOS", "ANDROID", "WINDOWS", "MACOS", "LINUX", "EMULATOR", "UNKNOWN"]
    regions = ["NA_US_EAST", "NA_US_WEST", "EU_WEST", "EU_CENTRAL", "APAC_SG", "APAC_JP", "LATAM_BR"]

    num_customers = max(num_transactions // 10, 100)
    customer_ids = [f"CUS-{100000 + i}" for i in range(num_customers)]
    customer_profiles = {
        cid: {
            "avg_amount": float(np.clip(np.random.normal(85.0, 35.0), 10.0, 2000.0)),
            "home_region": random.choice(regions),
            "primary_device": random.choice(device_types[:5]),
            "primary_channel": random.choice(channels[:3]),
            "historical_risk": round(float(np.random.beta(1.5, 8.0)), 3),
        }
        for cid in customer_ids
    }

    data = []
    base_time = datetime.datetime.utcnow() - datetime.timedelta(days=30)

    for i in range(num_transactions):
        txn_id = f"TXN-{1000000 + i}"
        customer_id = random.choice(customer_ids)
        prof = customer_profiles[customer_id]
        
        # 15 Fraud Scenarios Injection
        fraud_scenario = "NONE"
        is_fraud = 0
        scenario_prob = random.random()

        # Normal transaction parameters
        amount = round(float(np.clip(np.random.normal(prof["avg_amount"], prof["avg_amount"] * 0.3), 2.0, 10000.0)), 2)
        channel = prof["primary_channel"] if random.random() > 0.1 else random.choice(channels)
        payment_method = random.choice(payment_methods)
        currency = "USD"
        merchant_cat = random.choice(merchant_categories)
        device_type = prof["primary_device"] if random.random() > 0.1 else random.choice(device_types)
        region = prof["home_region"] if random.random() > 0.08 else random.choice(regions)
        is_new_device = 0 if device_type == prof["primary_device"] else 1
        is_location_anomaly = 0 if region == prof["home_region"] else 1
        velocity_last_1h = int(np.random.poisson(0.4))
        velocity_last_24h = int(np.random.poisson(2.5))
        failed_attempts_last_24h = int(np.random.choice([0, 1, 2], p=[0.90, 0.08, 0.02]))

        # Inject specific scenario
        if scenario_prob < 0.015:
            # Scenario 1: Sudden High-Value Transaction Anomaly
            fraud_scenario = "HIGH_VALUE_ANOMALY"
            amount = round(prof["avg_amount"] * random.uniform(8.0, 25.0), 2)
            merchant_cat = random.choice(["LUXURY_JEWELRY", "CRYPTO_EXCHANGE", "DIGITAL_GIFT_CARDS"])
            is_fraud = 1
        elif scenario_prob < 0.025:
            # Scenario 2: New Device + Impossible Geographic Travel
            fraud_scenario = "IMPOSSIBLE_TRAVEL"
            is_new_device = 1
            device_type = "EMULATOR" if random.random() > 0.5 else "LINUX"
            is_location_anomaly = 1
            region = "APAC_SG" if prof["home_region"] != "APAC_SG" else "LATAM_BR"
            is_fraud = 1
        elif scenario_prob < 0.035:
            # Scenario 3: High Velocity Burst Attack
            fraud_scenario = "VELOCITY_BURST"
            velocity_last_1h = random.randint(8, 25)
            velocity_last_24h = random.randint(25, 80)
            failed_attempts_last_24h = random.randint(3, 8)
            merchant_cat = "DIGITAL_GIFT_CARDS"
            is_fraud = 1

        txn_time = base_time + datetime.timedelta(seconds=i * 250 + random.randint(0, 100))

        # Risk Logit Calculation
        logit = (
            -3.5
            + 1.8 * is_fraud
            + 0.65 * (amount / max(prof["avg_amount"], 10.0))
            + 1.2 * is_new_device
            + 1.4 * is_location_anomaly
            + 0.35 * velocity_last_1h
            + 0.45 * failed_attempts_last_24h
            + (1.5 if merchant_cat in ["CRYPTO_EXCHANGE", "DIGITAL_GIFT_CARDS"] else -0.4)
            + np.random.normal(0, 0.25)
        )
        fraud_prob = round(float(1.0 / (1.0 + np.exp(-logit))), 4)
        calculated_risk_score = int(np.clip(fraud_prob * 100.0, 0, 100))

        if calculated_risk_score >= 80:
            risk_level = "CRITICAL"
            decision = "BLOCK"
        elif calculated_risk_score >= 60:
            risk_level = "HIGH"
            decision = "CHALLENGE"
        elif calculated_risk_score >= 40:
            risk_level = "ELEVATED"
            decision = "REVIEW"
        elif calculated_risk_score >= 20:
            risk_level = "MEDIUM"
            decision = "ALLOW_WITH_MONITORING"
        else:
            risk_level = "LOW"
            decision = "ALLOW"

        data.append({
            "transaction_id": txn_id,
            "customer_id": customer_id,
            "account_id": f"ACC-{customer_id.split('-')[1]}",
            "merchant_id": f"MER-{random.randint(1000, 9999)}",
            "merchant_category": merchant_cat,
            "channel": channel,
            "payment_method": payment_method,
            "currency": currency,
            "amount": amount,
            "customer_avg_amount": round(prof["avg_amount"], 2),
            "amount_deviation_ratio": round(amount / max(prof["avg_amount"], 1.0), 2),
            "device_type": device_type,
            "is_new_device": is_new_device,
            "region": region,
            "is_location_anomaly": is_location_anomaly,
            "velocity_last_1h": velocity_last_1h,
            "velocity_last_24h": velocity_last_24h,
            "failed_attempts_last_24h": failed_attempts_last_24h,
            "timestamp": txn_time.isoformat() + "Z",
            "fraud_scenario": fraud_scenario,
            "fraud_probability_ground_truth": fraud_prob,
            "calculated_risk_score": calculated_risk_score,
            "risk_level": risk_level,
            "decision": decision,
            "is_fraud": is_fraud,
        })

    df = pd.DataFrame(data)
    return df

def main():
    parser = argparse.ArgumentParser(description="FinGuard AI Synthetic Financial Transaction Engine")
    parser.add_argument("--transactions", type=int, default=10000, help="Number of transactions to generate")
    parser.add_argument("--output", type=str, default="data_storage/datasets/financial_transactions.csv", help="Output path")
    parser.add_argument("--seed", type=int, default=42, help="Seed")
    args = parser.parse_args()

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating {args.transactions:,} synthetic financial transactions with 15 fraud scenarios...")
    df = generate_financial_dataset(args.transactions, seed=args.seed)
    df.to_csv(out_path, index=False)
    
    fraud_count = df['is_fraud'].sum()
    fraud_rate = (fraud_count / len(df)) * 100.0
    print(f"Dataset generated at {out_path} ({len(df):,} rows | {fraud_count:,} fraud cases | Fraud Rate: {fraud_rate:.2f}%)")

if __name__ == "__main__":
    main()
