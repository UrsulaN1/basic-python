import boto3
s3 = boto3.client('s3')

bucket_name = 'ln-python-bucket'
region = s3.meta.region_name                   # So that code can work in any region other than aws config region

config = {}
if region != "us-east-1":
    config["CreateBucketConfiguration"] = {"LocationConstraint": region}

response = s3.create_bucket(       # This will work if only your aws config was set to us-east-1
    Bucket=bucket_name,
    # CreateBucketConfiguration={                               # In us-east-1, you must NOT specify LocationConstraint. In every other region, you MUST.
    #     'LocationConstraint': 'us-east-1'
    # }
    **config                       # because you added lines 5 to 9
)

print(response)