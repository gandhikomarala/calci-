# Terraform Module: SNS_NOTIFICATIONS
# Description: Amazon SNS topics for critical fraud and drift alert broadcasts

resource "aws_resource_sns_notifications" "main" {
  name        = "finguard-ai-enterprise-sns_notifications"
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

output "sns_notifications_resource_id" {
  value       = aws_resource_sns_notifications.main.id
  description = "Unique resource identifier for sns_notifications"
}
