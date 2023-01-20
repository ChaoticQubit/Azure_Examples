import sys
from azure.storage.blob import BlobServiceClient

def deleteContainer():
    try:
        with open('conn_string.txt', 'r') as f:
            connection_string = f.read()
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container=sys.argv[1])
        container_client.delete_container()
        print(f"""Container {sys.argv[1]} successfully deleted.""")

    except Exception as ex:
        print('Exception:')
        print(ex)
    
deleteContainer()