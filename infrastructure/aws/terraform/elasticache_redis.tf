# Terraform Module: ELASTICACHE_REDIS
# Description: Amazon ElastiCache Redis 7 Cluster for Celery message broker and caching

resource "aws_resource_elasticache_redis" "main" {
  name        = "finguard-ai-enterprise-elasticache_redis"
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

output "elasticache_redis_resource_id" {
  value       = aws_resource_elasticache_redis.main.id
  description = "Unique resource identifier for elasticache_redis"
}
