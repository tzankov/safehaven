'''
Tests currently cover AWS ONLY. Testing for GCP and Azure needs to be added
'''

import boto3
from moto import mock_s3
from safehaven import Aws

@mock_s3
def aws_test_list_upload():
    #Create the bucket in Moto's 'virtual' AWS account
    conn = boto3.resource('s3', region_name='eu-west-1')
    conn.create_bucket(Bucket='s3-shared-object-store-test')
    #Create an instance of the Aws class and upload a single entry list of a test object
    files = ['test_file']
    s3 = Aws()
    s3.create_client('s3-shared-object-store-test', files, 'region', 'aws_access_key_id', 'aws_secret_access_key')
    s3.upload_objects()

    #List objects in newly created bucket and assert that the single entry list we uploaded earlier matches the what is in the `cloud`
    objects = s3.list_objects()
    assert objects == ['test_file']
    print("AWS List / Upload Test PASSED")

    #Download object and assert
    s3.download_objects()
    print("AWS Download Test PASSED")

aws_test_list_upload()