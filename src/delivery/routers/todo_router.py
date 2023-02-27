from fastapi import APIRouter, Depends, Path, status, HTTPException
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
async def find_one_by_id(id: str = Path(min_length=24), service: TodoService = Depends()):
    return await service.find_one_by_id(id)


@router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def create(dto: CreateTodoDTO, service: TodoService = Depends()):
    return await service.create(dto)


@router.put(
    path='/{id}',
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def update(dto: UpdateTodoDTO, id: str = Path(min_length=24), service: TodoService = Depends()):
    return await service.update(id, dto)
