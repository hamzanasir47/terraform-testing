import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import Resource

# Initialize Azure credentials and clients
subscription_id = "9dfcb940-4a7b-4e3f-b55d-e9fd0dece2eb"
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

def delete_resources(resource_group: str):
    # Get resources in the specified resource group
    resources = resource_client.resources.list_by_resource_group(resource_group)

    for resource in resources:
        # Check if the resource has a 'terraform' tag or any other criteria
        if not resource.tags or resource.tags.get("terraform") != "true":
            print(f"Deleting resource: {resource.name} ({resource.id})")
            resource_client.resources.begin_delete_by_id(resource.id, api_version="2021-04-01")

if __name__ == "__main__":
    resource_group = "myresourcegroup"
    delete_resources(resource_group)
