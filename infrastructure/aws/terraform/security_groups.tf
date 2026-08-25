# Terraform Module: SECURITY_GROUPS
# Description: Stateful security groups and network access control lists (NACLs)

resource "aws_resource_security_groups" "main" {
  name        = "finguard-ai-enterprise-security_groups"
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

output "security_groups_resource_id" {
  value       = aws_resource_security_groups.main.id
  description = "Unique resource identifier for security_groups"
}
