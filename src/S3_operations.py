import boto3

BUCKET_NAME = 'abhishek-s3-2021-bucket'


# Step 1: An s3 client to use as a global operation to perform operations on s3
def s3_client():
    s3 = boto3.client('s3')
    # To get the auto complete benefits of boto3
    """ :type : pyboto3.s3 """
    return s3


# Step 2: A function to create a bucket given bucket name as argument, for a given aws region{eu-west-1}
def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1'
        }
    )


# Step 3: Main method to test the function Create Bucket
if __name__ == '__main__':
    print(create_bucket(BUCKET_NAME))
