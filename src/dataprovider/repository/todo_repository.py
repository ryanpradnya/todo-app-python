
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from ...utils.general import serializeDict
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.todo_model import TodoModel, TodoUpdateModel


class TodoRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('todos')

    def find(self):
        return

    def find_one_by_id(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        if not result:
            return None

        return serializeDict(result)

    def create(self, todo: TodoModel):
        return self.collection.insert_one(todo)

    def update(self, id: str, todo: TodoUpdateModel):
        result = self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": jsonable_encoder(todo)}
        )

        if not result:
            return None

        return serializeDict(self.find_one_by_id(id))
