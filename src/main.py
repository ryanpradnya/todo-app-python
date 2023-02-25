from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.setting import settings
from .config.mongo import client
from .delivery.routers import user_router

# Init Application
app = FastAPI(
    title='To Do App',
    version=settings.ENGINE_VERSION
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
