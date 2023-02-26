from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...delivery.dto.todo import CreateTodoDTO, ResponseTodoDTO, UpdateTodoDTO
from ...usecase.todo_service import TodoService
from ..query.pagination_query import PaginationFilterQuery

router = APIRouter(
    prefix='/todo',
    tags=['todo']
)


@router.get(
    path='',
    response_model=list[ResponseTodoDTO],
    response_model_exclude_unset=True
)
async def find(
    query: PaginationFilterQuery = Depends(),
    service: TodoService = Depends()
):
    result = await service.find_by_user_id(query)
    return JSONResponse(
        content=jsonable_encoder(result["data"]),
        headers={'x-total-count': str(result["total"])}
    )


@router.get(
    path='/{id}',
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def find_one_by_id(id: str, service: TodoService = Depends()):
    result = await service.find_one_by_id(id)
    return JSONResponse(content=jsonable_encoder(result))


@router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def create(dto: CreateTodoDTO, service: TodoService = Depends()):
    result = await service.create(dto)
    return JSONResponse(content=jsonable_encoder(result))


@router.put(
    path='/{id}',
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def update(id: str, dto: UpdateTodoDTO, service: TodoService = Depends()):
    result = await service.update(id, dto)
    return JSONResponse(content=jsonable_encoder(result))
