import requests
import redis
import logging

logging.basicConfig(level=logging.INFO)
db = redis.Redis(decode_responses=True, host='redis')

r = requests.get("http://python_app:8080/ping")

logging.info(db.get("lastPing"))