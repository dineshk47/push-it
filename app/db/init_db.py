import os
from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()
_shared_mongo_client = MongoClient(os.getenv("MONGO_URI"))


def get_mongo_db():
    mongo_db = _shared_mongo_client[os.getenv("MONGO_DB_NAME")]
    return mongo_db, _shared_mongo_client
