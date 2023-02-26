
from camel_converter import dict_to_camel
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from ...utils.mongo import get_sorts
from ...delivery.query.pagination_query import PaginationFilterQuery
from ...utils.general import serializeDict, serializeListToCamel
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.todo_model import TodoModel, TodoUpdateModel


class TodoRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('todos')

    def find(self, query: PaginationFilterQuery):
        offset = query.size * query.page
        sorts = get_sorts(TodoModel, query.sort)
        result = self.collection.find().sort(
            sorts).skip(offset).limit(query.size)
        return serializeListToCamel(result)

    def find_one_by_id(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        if not result:
            return None

        return dict_to_camel(serializeDict(result))

    def create(self, todo: TodoModel):
        return self.collection.insert_one(todo)

    def update(self, id: str, todo: TodoUpdateModel):
        result = self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": jsonable_encoder(todo)}
        )

        if not result:
            return None

        return self.find_one_by_id(id)
