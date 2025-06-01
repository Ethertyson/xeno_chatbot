# # Created by Pritanshu on 2025-05-28

# import redis
from flask import current_app
import requests

# def redisConnection():
#     return redis.Redis(
#         host=current_app.config['REDIS_HOST'],
#         port=current_app.config['REDIS_PORT'],
#         db=current_app.config['REDIS_DB'],
#         decode_responses=True  # to get strings, not bytes
#     )

def get_google_news_client():
    try:
        params ={
                    'token': current_app.config['GOOGLE_NEWS_API_KEY'],
                    'lang': 'en',
                    'max': 1  # number of articles you want
                }
                
        return requests.get(current_app.config['GOOGLE_NEWS_API_HOST'],params=params)
    except Exception as e:
        return {"Status":2,"Message":f"Connection Interrupted because of error: {e}"}