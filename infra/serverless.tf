# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.56.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

# Create a resource group
resource "azurerm_resource_group" "predict_group" {
  name     = "prediction-resources"
  location = "East US"
}

resource "azurerm_storage_account" "prediction" {
  name                     = "jonnyuniqueresources2"
  resource_group_name      = azurerm_resource_group.predict_group.name
  location                 = azurerm_resource_group.predict_group.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "prediction" {
  name                = "prediction-service-plan-jonny"
  resource_group_name = azurerm_resource_group.predict_group.name
  location            = azurerm_resource_group.predict_group.location
  os_type             = "Linux"
  sku_name            = "B1"

  depends_on = [
    azurerm_storage_account.prediction
  ]
}

resource "azurerm_linux_function_app" "prediction" {
  name                = "prediction-azure-function-jonny"
  location            = azurerm_resource_group.predict_group.location
  resource_group_name = azurerm_resource_group.predict_group.name

  storage_account_name       = azurerm_storage_account.prediction.name
  storage_account_access_key = azurerm_storage_account.prediction.primary_access_key
  service_plan_id            = azurerm_service_plan.prediction.id

  app_settings = {
    FUNCTIONS_WORKER_RUNTIME = "python"
  }

  site_config {
    application_stack {
      python_version = "3.9"
    }
  }

    depends_on = [
    azurerm_storage_account.prediction
  ]
}