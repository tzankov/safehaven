'''
Tests currently cover AWS ONLY. Testing for GCP and Azure needs to be added
'''

import boto3
from moto import mock_s3
from safehaven import Aws

@mock_s3
def test_upload():
    #Create the bucket in Moto's 'virtual' AWS account
    conn = boto3.resource('s3', region_name='eu-west-1')
    conn.create_bucket(Bucket='s3-shared-object-store-test')
    #Create an instance of the Aws class and upload a test object
    s3 = Aws()
    s3.create_client('s3-shared-object-store-test', 'test_file', 'region', 'aws_access_key_id', 'aws_secret_access_key')
    s3.list_objects()
    s3.upload_objects()

    body = conn.Object('s3-shared-object-store-test', 'test_file').get()['Body'].read().decode("utf-8")

    assert body == 'exists'