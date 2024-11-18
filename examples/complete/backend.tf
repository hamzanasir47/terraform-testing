terraform {
  backend "azurerm" {
    resource_group_name  = "myresourcegroup"
    storage_account_name = "mytfstate1"
    container_name       = "terraform-state"
    region               =  "East US"
    key                  = "prod.terraform.tfstate"
  }
}
