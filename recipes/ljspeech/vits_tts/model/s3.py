import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Specify your bucket name and file name
bucket_name = 'coquitry4'
file_name = 'best_model.pth'
config_name = 'config.json'

# Function to upload the model to S3
def upload_to_s3():
    s3.upload_file(file_name, bucket_name, file_name)
    s3.upload_file(config_name, bucket_name, config_name)
    print(f"Successfully uploaded {file_name} to {bucket_name}.")

# Function to download the model from S3
def download_from_s3():
    s3.download_file(bucket_name, file_name, file_name)
    print(f"Successfully downloaded {file_name} from {bucket_name}.")

# Uncomment to run the functions
upload_to_s3()
# download_from_s3()
