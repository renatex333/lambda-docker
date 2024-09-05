# lambda-docker

Welcome to this ML project!

## Installing Dependencies

To install the project dependencies, use the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Project Structure

- `data`: Contains the data used by the model.
- `models`: Contains the machine learning models and encoders.
- `notebooks`: Contains the notebooks used for data exploration and visualization.
- `src`: Contains the main source code to collect and process data, train models and make predictions.
- `tests`: Contains unit and integration tests to guarantee code stability.

## Usage

### Configure your AWS CLI

Having [AWS CLI installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), configure your credentials on a profile:
```bash
aws configure --profile mlops
```

To set it as deafult profile:

Linux:
```bash
export AWS_PROFILE=mlops
```

Windows CMD:
```bash
set AWS_PROFILE=mlops
```

Windows PowerShell:
```bash
env:AWS_PROFILE = "mlops"
```

### Create and configure ECR repository

To set up the project, let's build the Docker image from the `Dockerfile` with the `test` tag.

```bash
docker build --platform linux/amd64 -t lambda-ex-image:test .
```

> [!NOTE]  
> To test if it is working:
> ```bash
> docker run -p 9500:8080 lambda-ex-image:test
> curl "http://localhost:9500/2015-03-31/functions/function/invocations" -d "{}"
> ```

Now run the following script to create a repository in AWS ECR:

> [!IMPORTANT]  
> Save the `REPOSITORY_URI`.

```bash
python src/create_repository.py
```

Then login to ECR using the Docker CLI:

> [!IMPORTANT]  
> Substitute `AWS_ACCOUNT_ID` for your AWS Account ID.

```bash
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.us-east-2.amazonaws.com
```

Tag your local Docker image (`Dockerfile`) into the repository as the latest version and push the image:

> [!IMPORTANT]  
> Substitute `REPOSITORY_URI` for the correct repository's URI.

```bash
docker tag lambda-ex-image:test REPOSITORY_URI:latest

docker push REPOSITORY_URI:latest
```

### Create Lambda function

To create a Lambda function from the ECR image, run:

```bash
python src/create_function.py
```

### Test

To test the deployed instance, run the following command:

```bash
python tests/test.py
```

# References

[Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)