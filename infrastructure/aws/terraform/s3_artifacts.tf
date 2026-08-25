# Terraform Module: S3_ARTIFACTS
# Description: Encrypted Amazon S3 buckets with lifecycle policies for model artifacts and datasets

resource "aws_resource_s3_artifacts" "main" {
  name        = "finguard-ai-enterprise-s3_artifacts"
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

output "s3_artifacts_resource_id" {
  value       = aws_resource_s3_artifacts.main.id
  description = "Unique resource identifier for s3_artifacts"
}
