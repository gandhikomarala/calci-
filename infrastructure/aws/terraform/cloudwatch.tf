# Terraform Module: CLOUDWATCH
# Description: CloudWatch log groups, alarm thresholds, and inference latency dashboards

resource "aws_resource_cloudwatch" "main" {
  name        = "finguard-ai-enterprise-cloudwatch"
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

output "cloudwatch_resource_id" {
  value       = aws_resource_cloudwatch.main.id
  description = "Unique resource identifier for cloudwatch"
}
