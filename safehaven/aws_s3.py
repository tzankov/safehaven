import boto3
from .abstractions import CreateConnection, Listings, Uploader, Downloader

class Aws(CreateConnection, Listings, Uploader, Downloader):
    
    def create_client(self, bucket_name, object_name, region, aws_access_key_id, aws_secret_access_key):
        self.bucket_name = bucket_name
        self.object_name = object_name

        try:
            self.client = boto3.client('s3',
                    region_name=region,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key
                    )
        except Exception as e:
            raise Exception(f"ERROR creating client, " + str(e))
        

        return self.client

    def list_objects(self):
        list_of_objects = []
        response = self.client.list_objects_v2(
        Bucket=self.bucket_name,
        MaxKeys=10000
        )
        for k,v in response.items():
            if k == "Contents":
                #print(k,v)
                for value in v:
                    list_of_objects.append(value['Key'])

        return list_of_objects

    def download_objects(self):
        for object_name in self.object_name:
            try:
                self.client.download_file(self.bucket_name, object_name, object_name)
            except Exception as e:
                raise Exception(f"ERROR downloading object(s) from bucket {self.bucket_name}, " + str(e))
        
    def upload_objects(self):
        for object_name in self.object_name:
            try:
                self.client.upload_file(object_name, self.bucket_name, object_name)
            except Exception as e:
                raise Exception(f"ERROR uploading object to bucket {self.bucket_name}, " + str(e))