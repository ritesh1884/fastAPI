import os
from dotenv import load_dotenv

load_dotenv()

class settings:
    SECRET_KEY= os.getenv("SECRET_KEY")
    ORIGINS= os.getenv("ORIGINS")
    DB_URL= os.getenv("DB_URL")

settings = settings()