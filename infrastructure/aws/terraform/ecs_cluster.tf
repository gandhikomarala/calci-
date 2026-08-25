# Terraform Module: ECS_CLUSTER
# Description: Amazon ECS Fargate cluster with Auto-Scaling for API, Worker, and Scheduler tasks

resource "aws_resource_ecs_cluster" "main" {
  name        = "finguard-ai-enterprise-ecs_cluster"
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

output "ecs_cluster_resource_id" {
  value       = aws_resource_ecs_cluster.main.id
  description = "Unique resource identifier for ecs_cluster"
}
