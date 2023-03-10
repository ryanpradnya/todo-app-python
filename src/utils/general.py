
from typing import TypeVar

from camel_converter import dict_to_camel


T = TypeVar('T')


def get_attribute(cls: T):
    attributes: dict[str, any] = {}

    for attribute in cls.__dict__.keys():
        if attribute[:2] != '__':
            value = getattr(cls, attribute)
            if not callable(value):
                attributes[attribute] = value

    return attributes


def check_enum_value_exists(cls: T, value: any):
    return value in (val.value for val in cls.__members__.values())


def serializeDict(a) -> dict:
    return {"id": str(a["_id"]), **{i: a[i] for i in a if i != "_id"}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


def serializeListToCamel(entity) -> list:
    return [dict_to_camel(serializeDict(a)) for a in entity]
