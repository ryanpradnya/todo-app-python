from typing import TypeVar, Union
from camel_converter import to_snake
import pymongo

T = TypeVar('T')


def get_sorts(cls: T, sorts: list[str]):
    order: list[any] = []

    for sort in sorts:
        splits = sort.split(',')
        key = "_id" if splits[0] == "id" else to_snake(splits[0])
        val = getattr(cls, key) if hasattr(cls, key) else None
        if splits[1] == 'asc' and val:
            order.append(Union("key", pymongo.ASCENDING))
            pass
        elif splits[1] == 'desc' and val:
            order.append(Union("key", pymongo.DESCENDING))

    return order
