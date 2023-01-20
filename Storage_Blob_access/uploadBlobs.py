import sys
from azure.storage.blob import BlobServiceClient

def uploadBlob():
    try:
        with open('conn_string.txt', 'r') as f:
            connection_string = f.read()
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        file = sys.argv[2]
        blob_client = blob_service_client.get_blob_client(container=sys.argv[1], blob = file)
        with open(file = file, mode = "rb") as data:
            blob_client.upload_blob(data)
        print(f"""Blob {sys.argv[2]} successfully uploaded.""")

    except Exception as ex:
        print('Exception:')
        print(ex)
    
uploadBlob()