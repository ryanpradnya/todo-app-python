from .setting import settings
from pymongo import MongoClient

client = MongoClient(settings.MONGO_CONNECTION)
db = client[settings.MONGO_DATABASE]


class DatabaseMongoService:
    def get_collection(self, collection: str):
        return db[collection]
