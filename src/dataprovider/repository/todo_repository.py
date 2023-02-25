
from fastapi import Depends
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.todo_model import TodoModel, TodoUpdateModel


class TodoRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('todos')

    def find(self):
        return

    def find_one(self, id: str):
        return self.collection.find_one({"_id": id})

    def create(self, todo: TodoModel):
        return self.collection.insert_one(todo)

    def update(self, todo: TodoUpdateModel):
        return self.collection.update_one({"_id": id}, todo)
