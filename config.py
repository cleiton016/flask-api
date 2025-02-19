import os
from dotenv import load_dotenv
# Carregar variáveis de ambiente
load_dotenv()

class Config:
    FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
