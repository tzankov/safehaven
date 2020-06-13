import os
import logging
from azure.storage.blob import BlobServiceClient
from .abstractions import CreateConnection, Listings, Uploader, Downloader


class Azure(CreateConnection, Listings, Uploader, Downloader):
    
    def create_client(self, container_name, object_name, connection_string):
        self.blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
        self.container_name = container_name
        self.object_name = object_name
        self.status = ""

    def list_objects(self):
        try:
            logging.warning("\t Listing blobs")
            generator = self.blob_service_client.get_container_client(self.container_name)
            for blob in generator.list_blobs():
                logging.warning("\t Blob name: " + blob.name)
            self.status = "Existing Blobs listed successfully."
        except Exception as e:
            logging.error(f"ERROR uploading object, " + str(e))
            self.status = "Listing of Blobs Failed."

        return self.status

    def upload_objects(self):
        for object_name in self.object_name:
            try:
                blob_client = self.blob_service_client.get_blob_client(
                                                    container=self.container_name, 
                                                    blob=object_name
                                                    )

                with open(object_name, "rb") as data:
                    blob_client.upload_blob(data)
                
                self.status = f"Uploading of object {object_name} to {self.container_name} successful."
            except Exception as e:
                logging.error(f"Failed to upload object, " + str(e))
                self.status = "Upload of Object Failed"

        return self.status

    def download_objects(self):
        for object_name in self.object_name:
            try:
                blob_client = self.blob_service_client.get_blob_client(
                                                    container=self.container_name, 
                                                    blob=object_name
                                                    )
                with open(object_name, "wb") as download_file:
                    download_file.write(blob_client.download_blob().readall())

                self.status = f"Downloading of object {object_name} from {self.container_name} successful."
            except Exception as e:
                logging.error(f"Failed to download object, " + str(e))
                self.status = "Download of Object Failed"

        return self.status