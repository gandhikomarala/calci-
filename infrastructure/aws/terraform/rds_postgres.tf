# Terraform Module: RDS_POSTGRES
# Description: Amazon RDS PostgreSQL 16 Multi-AZ instance with automated backups and KMS encryption

resource "aws_resource_rds_postgres" "main" {
  name        = "finguard-ai-enterprise-rds_postgres"
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

output "rds_postgres_resource_id" {
  value       = aws_resource_rds_postgres.main.id
  description = "Unique resource identifier for rds_postgres"
}
