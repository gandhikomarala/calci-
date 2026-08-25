# Terraform Module: VPC
# Description: AWS Virtual Private Cloud with public/private subnets across 3 AZs

resource "aws_resource_vpc" "main" {
  name        = "finguard-ai-enterprise-vpc"
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

output "vpc_resource_id" {
  value       = aws_resource_vpc.main.id
  description = "Unique resource identifier for vpc"
}
