import sys
from datetime import datetime, timedelta
from azure.storage.blob import (
    BlobServiceClient,
    BlobSasPermissions, 
    generate_blob_sas
)

def getBlobls(**kwargs):
    try:
        AZURE_ACC_NAME = kwargs['AZURE_ACC_NAME']
        AZURE_PRIMARY_KEY = kwargs['AZURE_PRIMARY_KEY']
        AZURE_CONTAINER = kwargs['AZURE_CONTAINER']
        AZURE_BLOB= kwargs['AZURE_BLOB']
        AZURE_SAS_EXPIRY = kwargs['AZURE_SAS_EXPIRY']

        sas = generate_blob_sas(
            account_name=AZURE_ACC_NAME,
            container_name=AZURE_CONTAINER,
            blob_name=AZURE_BLOB,
            account_key=AZURE_PRIMARY_KEY,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=AZURE_SAS_EXPIRY)
        )
        return 'https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+AZURE_BLOB+'?'+sas

    except Exception as ex:
        print('Exception:')
        print(ex)

env_variables = {
    'AZURE_ACC_NAME': '',
    'AZURE_PRIMARY_KEY': '',
    'AZURE_CONTAINER': '',
    'AZURE_BLOB': '',
    'AZURE_SAS_EXPIRY': 1
}


env_variables['AZURE_CONTAINER'] = sys.argv[1]
env_variables['AZURE_BLOB'] = sys.argv[2]
env_variables['AZURE_SAS_EXPIRY'] = sys.argv[3] if len(sys.argv) > 3 else 1
print(getBlobls(**env_variables))
