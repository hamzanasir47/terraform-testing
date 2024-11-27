output "vnet_id" {
  description = "The ID of the Virtual Network"
  value       = azurerm_virtual_network.main.id
}

output "subnets" {
  description = "Details of created subnets"
  value = azurerm_subnet.main[*].id
}

output "nsg_ids" {
  description = "Network Security Group IDs for subnets"
  value       = azurerm_network_security_group.main[*].id
}
