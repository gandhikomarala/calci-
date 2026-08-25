# Terraform Module: ROUTE53
# Description: Amazon Route 53 DNS routing and health checks

resource "aws_resource_route53" "main" {
  name        = "finguard-ai-enterprise-route53"
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

output "route53_resource_id" {
  value       = aws_resource_route53.main.id
  description = "Unique resource identifier for route53"
}
