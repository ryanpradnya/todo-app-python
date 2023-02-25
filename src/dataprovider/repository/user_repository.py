
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from ...utils.general import serializeDict
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.user_model import UserModel, UserUpdateModel


class UserRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('users')

    def find(self):
        return

    def find_one_by_id(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        if not result:
            return None

        return serializeDict(result)

    def find_one_by_username(self, username: str):
        result = self.collection.find_one({"username": username})
        if not result:
            return None

        return serializeDict(result)

    def create(self, user: UserModel):
        return self.collection.insert_one(user)

    def update(self, id: str, user: UserUpdateModel):
        return self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": jsonable_encoder(user)}
        )
