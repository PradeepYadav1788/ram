# These libraries are already istalled by requrements.txt file.
from azure.common.client_factory import get_client_from_cli_profile
from azure .mgmt.resource import ResourceManagementClient

# Create a objet for resource to get credential from CLI login.
resource_client = get_client_from_cli_profile(ResourceManagementClient)

#Create Resource Group
rg_result = resource_client.resource_groups.create_or_update(
    "python-rg-test",
     {
         "location": "centralus"
         
     }
)

# Print Resource group details

print(f" Provisioned {rg_result.name} resource group in {rg_result.location} location")



