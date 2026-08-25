# Terraform Module: IAM_ROLES
# Description: Least-privilege IAM roles and ECS task execution policies

resource "aws_resource_iam_roles" "main" {
  name        = "finguard-ai-enterprise-iam_roles"
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

output "iam_roles_resource_id" {
  value       = aws_resource_iam_roles.main.id
  description = "Unique resource identifier for iam_roles"
}
