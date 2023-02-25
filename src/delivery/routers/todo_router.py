from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...delivery.dto.todo import CreateTodoDTO, ResponseTodoDTO
from ...usecase.todo_service import TodoService
from ..query.pagination_query import PaginationFilterQuery

router = APIRouter(
    prefix='/todo',
    tags=['todo']
)


# @router.get(
#     path='',
#     response_model=list[ResponseCompanyDTO],
#     response_model_exclude_unset=True
# )
# async def get_companies(
#     query: PaginationFilterQuery = Depends(),
#     service: CompanyService = Depends()
# ):
#     result = await service.find(query)
#     return JSONResponse(content=jsonable_encoder(result), headers={'x-total-count': str(len(result))})


@router.get(
    path='/{id}',
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def get_company(id: str, service: TodoService = Depends()):
    result = await service.find_one_by_id(id)
    return JSONResponse(content=jsonable_encoder(result))


@router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseTodoDTO,
    response_model_exclude_unset=True
)
async def add_company(dto: CreateTodoDTO, service: TodoService = Depends()):
    result = await service.create(dto)
    return JSONResponse(content=jsonable_encoder(result))


# @router.put(
#     path='/{company_code}',
#     response_model=ResponseCompanyDTO,
#     response_model_exclude_unset=True
# )
# async def update_company(
#     company_code: str,
#     company: UpdateCompanyDTO,
#     service: CompanyService = Depends()
# ):
#     result = await service.update(company_code, company)
#     if result:
#         return jsonable_encoder(result)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_502_BAD_GATEWAY,
#             detail='Company not created'
#         )
