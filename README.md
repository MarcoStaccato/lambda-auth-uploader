# AWS


## Requirements

* AWS CLI already configured with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)

## Setup process

```
sam build
```

### Local development

**Invoking function locally using a local sample payload**

```bash
sam local invoke UploadRequestFunction --event event.json
```

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```

If the previous command ran successfully you should now be able to hit the following local endpoint to invoke the function `http://localhost:3000/upload`

## Testing


Next, we install test dependencies and we run `pytest` against our `tests` folder to run our initial unit tests:

```bash
pip install pytest pytest-mock --user
python -m pytest tests/ -v
```

## Upload to s3

For an easier deployment we let SAM package and upload the function to s3
```
sam build
sam package --s3-bucket [your-bucket-name]
```

## Cleanup

In order to delete our Serverless Application recently deployed you can use the following AWS CLI Command:

```bash
aws cloudformation delete-stack --stack-name aws
```
