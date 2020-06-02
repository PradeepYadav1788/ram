import os , random

from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

# Obtain the management object for resources, using the credentials from the CLI login.
resource_client = get_client_from_cli_profile(ResourceManagementClient)

# Define variable for resoure group and location

RESOURCE_GROUP_NAME = "PYTHON-STORAGE"
LOCATION = "eastus"

rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, {"location": LOCATION})

# Print resource group details 
print(f"Provisioned {rg_result.name} resource group in {rg_result.location} location ")

# Storage Account object
storage_client = get_client_from_cli_profile(StorageManagementClient)
STORAGE_ACCOUNT_NAME = f"pythonazurestorage{random.randint(1,100000):05}"

# Check storage name availability
availability_result = storage_client.storage_accounts.check_name_availability(STORAGE_ACCOUNT_NAME)

if not availability_result.name_available:
    print(f"Storage name {STORAGE_ACCOUNT_NAME} is not available, Try another name ")
    exit()

#Name is available, Createacount
poller = storage_client.storage_accounts.create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, 
   {
       "location": LOCATION,
       "kind": "StorageV2",
       "sku": {"name": "Standard_LRS"}

   }

)

#After long running operation
account_result = poller.result()
print(f"Provisined Storage account {account_result.name} ")

# Retrive the account primary access key and generate a connection string
keys = storage_client.storage_accounts.list_keys(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME) 
print(f"Primary key for storage account: {keys.keys[0].value} ")
conn_string = f"DefaultEndpointsProtocol=https:EndpointSuffix=core.windows.net;AccountName={STORAGE_ACCOUNT_NAME};AccountKey={keys.keys[0].value} "
print(f"Connection String: {conn_string} ")

#Provision a container 
CONTAINER_NAME = "blob-container-01"
container = storage_client.blob_containers.create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, {} )
print(f"Provisioned blob container {container.name} ")