from telegram_package.system_layer.database_repository.mongo_db import MongoDB
from telegram_package.system_layer.gemini_llm import GeminiLLM
from fastapi import FastAPI
from flask import Flask, abort
from dotenv import load_dotenv
import os
from telegram_package.config import DevelopmentConfig, ProductionConfig
from telegram.ext import (Application)
import logging
import sys
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Log to stdout
    ],
)
logger = logging.getLogger(__name__)

load_dotenv()

if os.getenv('ENV') == 'production':
    print("I am in the production")
    config = ProductionConfig

else:
    print("I am in the development")
    config = DevelopmentConfig

# mongodb = MongoDB(
#     config.MONGO_DB_NAME,
#     config.MONGO_DB_USER,
#     config.MONGO_DB_PASS,
#     config.MONGO_DB_REST_URL)
#


llm = GeminiLLM(config.GEMINI_API_KEY)

application = Application.builder().token(config.TELEGRAM_TOKEN).updater(None).build()

def create_app():
    #app = Flask(__name__)
    app = FastAPI()
    return app
