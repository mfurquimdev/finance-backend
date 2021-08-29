from fastapi import FastAPI
from typing import Optional
from .log_manager import log

from app.transaction.view import router as transaction_router

app = FastAPI(title="Finance MFurquim Dev")

def load_modules(app):
    app.include_router(
        transaction_router,
        tags=["Transaction"],
    )

load_modules(app)

