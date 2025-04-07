# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  subscription_id = "<SUBSCRIPTION ID HERE>"
}


resource "azurerm_resource_group" "language_translator_rg" {
  name     = "beanspeak-rg"
  location = "westus3"
}


resource "azurerm_cognitive_account" "text_translation" {
  name                = "beanspeak-translation"
  location            = azurerm_resource_group.language_translator_rg.location
  resource_group_name = azurerm_resource_group.language_translator_rg.name
  kind                = "TextTranslation"
  sku_name            = "F0"
}
output "text_translation_key" {
  value = azurerm_cognitive_account.text_translation.primary_access_key
  sensitive = true
}
output "text_translation_endpoint" {
  value = azurerm_cognitive_account.text_translation.endpoint
  sensitive = true
}
