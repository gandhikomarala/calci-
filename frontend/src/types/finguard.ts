export type UserRole = 
  | 'SUPER_ADMIN'
  | 'ADMIN'
  | 'FRAUD_ANALYST'
  | 'SENIOR_ANALYST'
  | 'ML_ENGINEER'
  | 'DATA_ENGINEER'
  | 'MANAGER'
  | 'AUDITOR'
  | 'VIEWER';

export type RiskLevel = 'LOW' | 'MEDIUM' | 'ELEVATED' | 'HIGH' | 'CRITICAL';
export type RiskDecision = 'ALLOW' | 'ALLOW_WITH_MONITORING' | 'REVIEW' | 'CHALLENGE' | 'BLOCK';
export type AlertStatus = 'NEW' | 'ASSIGNED' | 'UNDER_REVIEW' | 'ESCALATED' | 'RESOLVED' | 'DISMISSED';
export type InvestigationDecision = 'CONFIRMED_FRAUD' | 'LIKELY_FRAUD' | 'FALSE_POSITIVE' | 'LEGITIMATE' | 'INCONCLUSIVE' | 'ESCALATED';

export interface Transaction {
  transaction_id: string;
  customer_id: string;
  account_id: string;
  merchant_id: string;
  merchant_category: string;
  channel: string;
  payment_method: string;
  currency: string;
  amount: number;
  customer_avg_amount: number;
  amount_deviation_ratio: number;
  device_type: string;
  is_new_device: number;
  region: string;
  is_location_anomaly: number;
  velocity_last_1h: number;
  velocity_last_24h: number;
  failed_attempts_last_24h: number;
  timestamp: string;
  calculated_risk_score: number;
  risk_level: RiskLevel;
  decision: RiskDecision;
  is_fraud: number;
}

export interface FraudAlert {
  id: string;
  transaction_id: string;
  customer_id: string;
  risk_score: number;
  risk_level: RiskLevel;
  status: AlertStatus;
  assigned_to?: string;
  created_at: string;
  sla_deadline: string;
}

export interface Investigation {
  id: string;
  alert_id: string;
  analyst_id: string;
  status: string;
  decision?: InvestigationDecision;
  decision_notes?: string;
  evidence_count: number;
  created_at: string;
  updated_at: string;
}
