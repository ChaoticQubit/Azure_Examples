import sys
from azure.storage.blob import BlobServiceClient

def listBlobs():
    try:
        with open('conn_string.txt', 'r') as f:
            connection_string = f.read()
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container=sys.argv[1])

        print("\nListing blobs...")
        blob_list = container_client.list_blobs()
        counter = 1
        for blob in blob_list:
            print(str(counter) + ": " + blob.name + " -- " + str(blob.size) + " Bytes")
            counter += 1

    except Exception as ex:
        print('Exception:')
        print(ex)
    
listBlobs()