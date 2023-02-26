from typing import TypeVar, Union
from camel_converter import to_snake
import pymongo

from ..delivery.enum.query_enum import QueryFilter
from ..delivery.dto.query import QueryFilterDTO

T = TypeVar('T')


def get_sorts(cls: T, sorts: list[str]):
    order: list[any] = []

    for sort in sorts:
        splits = sort.split(',')
        key = "_id" if splits[0] == "id" else to_snake(splits[0])
        if splits[1] == 'asc' and hasattr(cls, key):
            order.append(("key", pymongo.ASCENDING))
        elif splits[1] == 'desc' and hasattr(cls, key):
            order.append(("key", pymongo.DESCENDING))

    return order


def get_query(cls: T, filters: list[QueryFilterDTO]):
    query: dict[str, any] = {}

    for fil in filters:
        key: str = "_id" if fil.key == "id" else to_snake(fil.key)
        if hasattr(cls, key):
            if QueryFilter[fil.criteria] is QueryFilter.equal:
                query = {**query, key: {"$eq": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.not_equal:
                query = {**query, key: {"$ne": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.greather_than_or_equal:
                query = {**query, key: {"$gte": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.less_than_or_equal:
                query = {**query, key: {"$lte": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.greather_than:
                query = {**query, key: {"$gt": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.less_than:
                query = {**query, key: {"$lt": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.in_vals:
                query = {**query, key: {"$in": fil.val}}
            if QueryFilter[fil.criteria] is QueryFilter.includes:
                query = {**query, key: {"$regex": f"(?i){fil.val}"}}

    return query
