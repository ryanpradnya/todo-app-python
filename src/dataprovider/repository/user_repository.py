
from camel_converter import dict_to_camel
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from ...utils.general import serializeDict
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.user_model import UserModel, UserUpdateModel


class UserRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('users')

    def find_one_by_id(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        if not result:
            return None

        return dict_to_camel(serializeDict(result))

    def find_one_by_username(self, username: str):
        result = self.collection.find_one({"username": username})
        if not result:
            return None

        return dict_to_camel(serializeDict(result))

    def create(self, user: UserModel):
        return self.collection.insert_one(user)

    def update(self, id: str, user: UserUpdateModel):
        result = self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": jsonable_encoder(user)}
        )

        if not result:
            return None

        return self.find_one_by_id(id)
