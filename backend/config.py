import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "edu-genie-dev-secret")
