from fastapi import Request

from ...utils.general import check_enum_value_exists
from ...delivery.enum.query_enum import QueryFilter
from ...delivery.dto.query import QueryFilterDTO


def query_filters(request: Request) -> list[QueryFilterDTO]:
    filters: list[QueryFilterDTO] = []
    params = request.query_params
    for key in params:
        if key not in ('sort', 'size', 'page'):
            keys: list[str] = key.split('.')
            is_exists = check_enum_value_exists(QueryFilter, keys[1])
            if len(keys) == 2 and is_exists:
                filters.append(QueryFilterDTO(
                    key=keys[0], criteria=keys[1], val=params[key]))

    return filters
