
from typing import TypeVar


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
