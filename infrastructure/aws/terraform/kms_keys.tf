# Terraform Module: KMS_KEYS
# Description: Customer Managed KMS keys for envelope encryption of banking data

resource "aws_resource_kms_keys" "main" {
  name        = "finguard-ai-enterprise-kms_keys"
  environment = var.environment

  tags = {
    Project     = "FinGuard AI — Enterprise Fraud Detection"
    ManagedBy   = "Terraform"
    Environment = var.environment
    Compliance  = "SOC2-Type2 / PCI-DSS"
  }
}

variable "environment" {
  type        = string
  default     = "production"
  description = "Deployment environment tier (development, staging, production)"
}

output "kms_keys_resource_id" {
  value       = aws_resource_kms_keys.main.id
  description = "Unique resource identifier for kms_keys"
}
