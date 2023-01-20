## Setup
1. Go onto Azure Portal
2. Navigate to your storage account.
3. Click on the "Access Keys" function.
4. Show and Copy the connection string.
5. Create a file named "conn_string.txt" in the same directory as the python file.
5. Paste your newly copied connection string in this file.

## Creating a Container
In the terminal, run command,

```python 
    python createContainer.py <NEW_CONTAINER_NAME>
```

## Upload Blob to a Container
In the terminal, run command,

```python 
    python uploadBlobs.py <CONTAINER_NAME> <FILE_URI>
```

## List All Blobs in a Container
In the terminal, run command,

```python 
    python listBlobsInContainer.py <CONTAINER_NAME>
```

## Get Access Link For a Particular Blob
In the terminal, run command,

```python 
    python uploadBlobs.py <CONTAINER_NAME> <FILE_NAME> <EXPIRY_TIME_IN_HOURS:Optional-Default(1)>
```

## Delete a Container
In the terminal, run command,

```python 
    python deleteContainer.py <CONTAINER_NAME>
```
