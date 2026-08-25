# Terraform Module: ALB
# Description: Application Load Balancer with SSL/TLS termination and path-based routing

resource "aws_resource_alb" "main" {
  name        = "finguard-ai-enterprise-alb"
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

output "alb_resource_id" {
  value       = aws_resource_alb.main.id
  description = "Unique resource identifier for alb"
}
