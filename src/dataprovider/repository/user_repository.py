
from fastapi import Depends

from ...utils.general import serializeDict
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.user_model import UserModel, UserUpdateModel


class UserRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('users')

    def find(self):
        return

    def find_one_by_id(self, id: str):
        return serializeDict(self.collection.find_one({"_id": id}))

    def find_one_by_username(self, username: str):
        result = self.collection.find_one({"username": username})
        if not result:
            return None

        return serializeDict(result)

    def create(self, user: UserModel):
        return self.collection.insert_one(user)

    def update(self, user: UserUpdateModel):
        return self.collection.update_one({"_id": id}, user)
