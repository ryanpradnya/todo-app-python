# from fastapi import APIRouter, Depends, status, HTTPException
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

# from ..query.pagination_query import PaginationFilterQuery
# from ...delivery.dto.company import CreateCompanyDTO, ResponseCompanyDTO, UpdateCompanyDTO
# from ...usecase.company_service import CompanyService

# router = APIRouter(
#     prefix='/companies',
#     tags=['companies']
# )


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


# @router.get(
#     path='/{company_code}',
#     response_model=ResponseCompanyDTO,
#     response_model_exclude_unset=True
# )
# async def get_company(company_code: str, service: CompanyService = Depends()):
#     result = await service.find_one_by_company(company_code)
#     return jsonable_encoder(result)


# @router.post(
#     path='',
#     status_code=status.HTTP_201_CREATED,
#     response_model=ResponseCompanyDTO,
#     response_model_exclude_unset=True
# )
# async def add_company(company: CreateCompanyDTO, service: CompanyService = Depends()):
#     result = await service.create(company)
#     if result:
#         return jsonable_encoder(result)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_502_BAD_GATEWAY,
#             detail='Company not created'
#         )


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
