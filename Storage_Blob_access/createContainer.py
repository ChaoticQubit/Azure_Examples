import sys
from azure.storage.blob import BlobServiceClient

def createContainer():
    try:
        with open('conn_string.txt', 'r') as f:
            connection_string = f.read()
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.create_container(sys.argv[1])
        print(f"""Container {sys.argv[1]} successfully created.""")

    except Exception as ex:
        print('Exception:')
        print(ex)
    
createContainer()