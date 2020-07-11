from google.cloud import storage
from google.cloud.storage import Blob
import google.oauth2.credentials
import logging
from .abstractions import CreateConnection, Listings, Uploader, Downloader

class Gcp(CreateConnection, Listings, Uploader, Downloader):
    
    def create_client(self, project, bucket_name, object_name, key_file):
        self.project = project
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.key_file = key_file
        
        try:
            self.client = storage.Client.from_service_account_json(self.key_file)
        except Exception as e:
            raise Exception(f"ERROR creating client, " + str(e))
        
        return self.client

    def list_objects(self):
        list_of_objects = []
        response = self.client.list_blobs(
        bucket_or_name=self.bucket_name,
        max_results=10000,
        fields='items(name)'
        )

        for x in response:
            list_of_objects.append(x.name)
            
        return list_of_objects

    def download_objects(self):
        for object_name in self.object_name:
            try:
                bucket = self.client.get_bucket(self.bucket_name)
                blob = Blob(object_name, bucket)
                blob.download_to_filename(object_name)
            except Exception as e:
                logging.error(f"Downloading object(s) from bucket {self.bucket_name}, " + str(e))
        
    def upload_objects(self):
        content_type=None 
        content_encoding=None
        for object_name in self.object_name:
            try:
                bucket = self.client.get_bucket(self.bucket_name)
                blob = Blob(object_name, bucket)

                if content_encoding is not None:
                    blob.content_encoding = content_encoding

                blob.upload_from_filename(object_name, content_type=content_type)
            except Exception as e:
                logging.error(f"Uploading object to bucket {self.bucket_name}, " + str(e))