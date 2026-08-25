# Terraform Module: SECRETS_MANAGER
# Description: AWS Secrets Manager integration for database and API credentials

resource "aws_resource_secrets_manager" "main" {
  name        = "finguard-ai-enterprise-secrets_manager"
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

output "secrets_manager_resource_id" {
  value       = aws_resource_secrets_manager.main.id
  description = "Unique resource identifier for secrets_manager"
}
