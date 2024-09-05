"""
Module to create a new AWS Lambda function from ECR image
"""

import os
import boto3
from dotenv import load_dotenv

def main():
    load_dotenv()

    function_name = "ex_docker_renatex"

    # Provide Image URI
    version = "latest"
    image_uri = f"{os.getenv('REPOSITORY_URI')}:{version}"

    lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

    lambda_client = boto3.client(
        "lambda",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    response = lambda_client.create_function(
        FunctionName=function_name,
        PackageType="Image",
        Code={"ImageUri": image_uri},
        Role=lambda_role_arn,
        Timeout=30,  # Optional: function timeout in seconds
        MemorySize=128,  # Optional: function memory size in megabytes
    )

    print("Lambda function created successfully:")
    print(f"Function Name: {response['FunctionName']}")
    print(f"Function ARN: {response['FunctionArn']}")

if __name__ == "__main__":
    main()
