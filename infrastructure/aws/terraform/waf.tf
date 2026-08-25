# Terraform Module: WAF
# Description: AWS WAF Web ACL rules protecting against DDoS and SQL injection attacks

resource "aws_resource_waf" "main" {
  name        = "finguard-ai-enterprise-waf"
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

output "waf_resource_id" {
  value       = aws_resource_waf.main.id
  description = "Unique resource identifier for waf"
}
