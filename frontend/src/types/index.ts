export interface Customer {
  id: string;
  customer_code: string;
  first_name: string;
  last_name: string;
  email: string;
  phone?: string;
  gender?: string;
  age?: number;
  region?: string;
  city?: string;
  occupation?: string;
  income?: number;
  signup_date: string;
  is_churned: boolean;
  churn_date?: string;
  created_at: string;
}

export interface Customer360 extends Customer {
  tenure_months: number;
  total_spend: number;
  current_churn_risk: number;
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH';
  engagement_score: number;
  satisfaction_score: number;
}

export interface PredictionFactor {
  feature: string;
  contribution: number;
  abs_impact: number;
}

export interface PredictionResult {
  customer_id: string;
  prediction: number;
  churn_probability: number;
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH';
  confidence: number;
  model_version: string;
  prediction_timestamp: string;
  top_positive_factors: PredictionFactor[];
  top_negative_factors: PredictionFactor[];
}

export interface Dataset {
  id: string;
  name: string;
  description?: string;
  data_format: string;
  latest_version: number;
  is_approved: boolean;
  created_at: string;
}

export interface ModelVersion {
  id: string;
  model_id: string;
  version_tag: string;
  stage: 'DEVELOPMENT' | 'VALIDATION' | 'STAGING' | 'PRODUCTION' | 'ARCHIVED';
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
  roc_auc: number;
  pr_auc: number;
  is_production: boolean;
  created_at: string;
}

export interface DriftReport {
  id: string;
  model_version_tag: string;
  drift_status: 'NORMAL' | 'WARNING' | 'CRITICAL';
  overall_psi: number;
  features_drifted_count: number;
  total_features_count: number;
  created_at: string;
}
