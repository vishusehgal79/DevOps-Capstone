terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.38.0"
    }
  }
}

provider "kubernetes" {
  config_path = "C:/Users/VANSHIKA/.kube/config"
}

resource "kubernetes_namespace_v1" "employee_platform" {
  metadata {
    name = "employee-platform"
  }
}

resource "kubernetes_config_map_v1" "employee_config" {
  metadata {
    name      = "employee-api-config"
    namespace = kubernetes_namespace_v1.employee_platform.metadata[0].name
  }

  data = {
    APP_NAME  = "Employee Management API"
    APP_ENV   = "production"
    LOG_LEVEL = "INFO"
  }
}

output "namespace" {
  value = kubernetes_namespace_v1.employee_platform.metadata[0].name
}

output "config_map" {
  value = kubernetes_config_map_v1.employee_config.metadata[0].name
}
