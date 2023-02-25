from fastapi import Depends, Query

from ...application.dependencies.request import query_filters
from ...delivery.dto.query import QueryFilterDTO


class BasePaginationQuery:
    def __init__(
        self,
        size: int = Query(
            default=10,
            description='The amount of data taken'
        ),
        page: int = Query(
            default=0,
            description='The part of the data that want to retrieve'
        ),
        sort: list[str] = Query(
            default=[],
            regex='^[A-Za-z0-9_-]+,(desc|asc)$',
            description='Field used to sort in ascending or descending order',
            example='query_item,asc'
        ),
    ):
        self.size = size
        self.page = page
        self.sort = sort


class PaginationFilterQuery(BasePaginationQuery):
    def __init__(
        self,
        size: int = Query(default=10, description='The amount of data taken'),
        page: int = Query(
            default=0,
            description='The part of the data that want to retrieve'
        ),
        sort: list[str] = Query(
            default=[],
            regex='^[A-Za-z0-9_-]+,(desc|asc)$',
            description='Field used to sort in ascending or descending order',
            example='query_item,asc'
        ),
        filters: list[QueryFilterDTO] = Depends(query_filters)
    ):
        super().__init__(size, page, sort)
        self.filters = filters
