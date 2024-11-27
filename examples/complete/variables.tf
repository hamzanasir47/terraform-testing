variable "vnet_name" {
  description = "Name of the Virtual Network"
  type        = string
}

variable "location" {
  description = "Azure region where the VNet will be created"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "address_space" {
  description = "Address space for the VNet"
  type        = list(string)
}

variable "subnets" {
  description = "List of subnets to create"
  type = list(object({
    name                       = string
    address_prefixes           = list(string)
    private_endpoint_policies  = bool
  }))
}

variable "tags" {
  description = "Tags to associate with resources"
  type        = map(string)
  default     = {}
}
