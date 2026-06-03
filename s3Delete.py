
import boto3
s3 = boto3.client('s3')

bucket_name = 'ln-python-bucket'

response = s3.delete_bucket(
    Bucket=bucket_name
)

print("bucket deleted successfully")
print(response)