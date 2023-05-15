variable "db_password" {
  type = string
}

resource "azurerm_cosmosdb_postgresql_cluster" "data_store" {
  name                            = "jonnys-prediction-data-store"
  resource_group_name             = azurerm_resource_group.predict_group.name
  location                        = azurerm_resource_group.predict_group.location
  administrator_login_password    = var.db_password
  coordinator_storage_quota_in_mb = 131072
  coordinator_vcore_count         = 2
  node_count                      = 0
}