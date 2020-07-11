![https://www.gnu.org/licenses/gpl-3.0](https://img.shields.io/badge/License-GPL%20v3-blue.svg "GPL-3.0")
# safehaven

## Description
This library allows users to list, upload and download objects to and from the following cloud providers:

* Amazon Web Services (AWS S3)
* Microsoft Azure (Blob Store) 
* Google Cloud Platform (GCP Storage)

## Usage
### Installation
```
pip install safehaven
```

### AWS
```
from safehaven import Aws
s3 = Aws()
s3.create_client('s3-shared-object-store-test', 'file_names', 'region', 'aws_access_key_id', 'aws_secret_access_key')
s3.list_objects()
s3.upload_objects()
s3.download_objects()
```

### Azure
```
from safehaven import Azure
blob = Azure()
blob.create_client('container_name', 'file_names', 'connection_string')
blob.list_objects()
blob.upload_objects()
blob.download_objects()
```

### GCP
```
from safehaven import Gcp
gcp = Gcp()
gcp.create_client('project_name' 'storage_bucket_name', 'location_and_name_of_files', 'key_file')
gcp.list_objects()
gcp.upload_objects()
gcp.download_objects()
```

### Testing this library
```
pip install moto
python3 tests/test_safehaven.py
```


## Links
* Code: https://github.com/tzankov/safehaven
* Releases on Pypi: https://pypi.org/project/safehaven