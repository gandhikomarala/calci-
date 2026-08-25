# Terraform Module: EVENTBRIDGE
# Description: Amazon EventBridge rules for scheduled retraining triggers

resource "aws_resource_eventbridge" "main" {
  name        = "finguard-ai-enterprise-eventbridge"
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

output "eventbridge_resource_id" {
  value       = aws_resource_eventbridge.main.id
  description = "Unique resource identifier for eventbridge"
}
