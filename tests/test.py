import os
import io
import json
import boto3
from dotenv import load_dotenv

def main():
    load_dotenv()

    # Lambda function name
    function_name = "ex_docker_renatex"

    # Lambda basic execution role
    test_lambda(function_name)

def test_lambda(function_name: str):
    # Create a Boto3 client for AWS Lambda
    lambda_client = boto3.client(
        "lambda",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    try:
        # Invoke the function
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
        )

        payload = response["Payload"]

        response_dict = json.loads(io.BytesIO(payload.read()).read().decode("utf-8"))
        print(f"Response:\n{response_dict}")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
