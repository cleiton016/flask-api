import os
from dotenv import load_dotenv
import json
import boto3
from botocore.exceptions import ClientError
# Carregar variáveis de ambiente
load_dotenv()

class Config:
    FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
    
    @staticmethod
    def get_secret():

        secret_name = "firebase-flask"
        region_name = "sa-east-1"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e

        secret = get_secret_value_response['SecretString']

        return json.loads(secret)
    # Your code goes here.

