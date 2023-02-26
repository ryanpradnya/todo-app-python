
from camel_converter import dict_to_camel
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from ...delivery.dto.todo import TodoQuery
from ...utils.mongo import get_query, get_sorts
from ...delivery.query.pagination_query import PaginationFilterQuery
from ...utils.general import serializeDict, serializeListToCamel
from ...config.mongo import DatabaseMongoService
from ...dataprovider.model.todo_model import TodoModel, TodoUpdateModel


class TodoRepository:
    def __init__(self, dbService: DatabaseMongoService = Depends()) -> None:
        self.collection = dbService.get_collection('todos')

    def _get_total(self, query: PaginationFilterQuery):
        query_filter = get_query(TodoQuery, query.filters)
        result = self.collection.find(query_filter)
        return len(list(result))

    def find(self, query: PaginationFilterQuery):
        offset = query.size * query.page
        sorts = get_sorts(TodoModel, query.sort)
        query_filter = get_query(TodoQuery, query.filters)

        result = self.collection.find(query_filter)

        if len(sorts) > 0:
            result.sort(sorts)
        if offset >= 0:
            result = result.skip(offset)
        if query.size > 0:
            result = result.limit(query.size)

        return {
            "data": serializeListToCamel(result),
            "total": self._get_total(query)
        }

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
