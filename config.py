#Created by Pritanshu on 2025-05-28

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("FLASK_ENV") == "development"
    # REDIS_HOST = os.getenv("REDIS_HOST")
    # REDIS_PORT = int(os.getenv("REDIS_PORT",6379))
    # REDIS_DB = int(os.getenv("REDIS_DB",0))
    GOOGLE_NEWS_API_KEY = os.getenv("GOOGLE_NEWS_API_KEY")
    GOOGLE_NEWS_API_HOST = os.getenv("GOOGLE_NEWS_API_HOST")