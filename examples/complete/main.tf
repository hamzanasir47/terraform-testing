provider "azurerm" {
  features {}
}

resource "azurerm_virtual_network" "main" {
  name                = var.vnet_name
  location            = var.location
  resource_group_name = var.resource_group_name
  address_space       = var.address_space
  tags                = var.tags
}

resource "azurerm_subnet" "main" {
  count                   = length(var.subnets)
  name                    = var.subnets[count.index].name
  resource_group_name     = var.resource_group_name
  virtual_network_name    = azurerm_virtual_network.main.name
  address_prefixes        = var.subnets[count.index].address_prefixes
  enforce_private_link_endpoint_network_policies = var.subnets[count.index].private_endpoint_policies
}

resource "azurerm_network_security_group" "main" {
  count                = length(var.subnets)
  name                 = "${var.subnets[count.index].name}-nsg"
  location             = var.location
  resource_group_name  = var.resource_group_name
  tags                 = var.tags
}

resource "azurerm_subnet_network_security_group_association" "main" {
  count                = length(var.subnets)
  subnet_id            = azurerm_subnet.main[count.index].id
  network_security_group_id = azurerm_network_security_group.main[count.index].id
}
