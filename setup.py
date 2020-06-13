from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
	readme = f.read()

setup(
	name='safehaven',
	version='0.1.0',
	author="Tzankov",
    author_email="tzankotz@gmail.com",
	description='Library to list, upload and download objects from AWS S3, Azure Blob Storage, and GCP Storage.',
	keywords="aws gcp azure s3 azureblob gcpblob blob cloud storage cloudstorage",
	long_description=readme,
	url="https://github.com/tzankov/safehaven",
	install_requires=[
		'boto3==1.12.31',
		'azure-storage-blob==12.3.0',
		'google-cloud-storage==1.25.0'
		],
	packages=find_packages('safehaven'),
    package_dir={"": "safehaven"},
	python_requires=">=3.6"
	)