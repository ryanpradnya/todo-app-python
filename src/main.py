from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .config.setting import settings
from .config.mongo import client
from .delivery.routers import user_router, todo_router

# Init Application
app = FastAPI(
    title='To Do App',
    version=settings.ENGINE_VERSION
)

# Handler


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()
    error_detail: dict[str, str] = {}
    for error in details:
        print(error)
        key = error["loc"][-1]
        error_detail = {
            **error_detail,
            key: error["msg"]
        }
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": error_detail}),
    )

# Set CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Events


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()


# Routers
app.include_router(user_router.router)
app.include_router(todo_router.router)
