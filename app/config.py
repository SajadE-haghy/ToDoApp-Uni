import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    raw_db_uri = os.getenv("DATABASE_URL")

    
    if raw_db_uri.startswith("sqlite:///") and not raw_db_uri.startswith("sqlite:////"):
        relative_path = raw_db_uri.replace("sqlite:///", "")
        absolute_path = os.path.join(BASE_DIR, relative_path)
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{absolute_path}"
    else:
        SQLALCHEMY_DATABASE_URI = raw_db_uri

    SQLALCHEMY_TRACK_MODIFICATIONS = False
