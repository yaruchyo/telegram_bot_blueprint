import os
from dotenv import load_dotenv

load_dotenv()
class Config(object):
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

class ProductionConfig(Config):
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    # MONGO_DB_USER = os.getenv("MONGO_DB_USER")
    # MONGO_DB_PASS = os.getenv("MONGO_DB_PASS")
    # MONGO_DB_REST_URL = os.getenv("MONGO_DB_REST_URL")
    # MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")





class DevelopmentConfig(Config):
    DEBUG = True

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_TEST")

    # MONGO_DB_USER = os.getenv("MONGO_DB_USER")
    # MONGO_DB_PASS = os.getenv("MONGO_DB_PASS")
    # MONGO_DB_REST_URL = os.getenv("MONGO_DB_REST_URL")
    # MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")



