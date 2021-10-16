from asyncpg import UniqueViolationError, ForeignKeyViolationError
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from typing import Optional

from .log_manager import log

from app.transaction.view import router as transaction_router

app = FastAPI(title="Finance MFurquim Dev")

@app.exception_handler(UniqueViolationError)
async def unique_violation_error_exception_handler(request: Request,
                                                   exc: RequestValidationError):
    """`UniqueViolationError` exception handling"""

    content = {
        "Duplicate Entry": {
            "body": str(exc),
            "trace": traceback.format_exc()
        }
    }
    return JSONResponse(content=content, status_code=status.HTTP_403_FORBIDDEN)


@app.exception_handler(ForeignKeyViolationError)
async def foreignKey_violation_error_exception_handler(
        request: Request, exc: RequestValidationError):
    """`ForeignKeyViolationError` Handling"""

    content = {
        "ForeignKeyViolationError": {
            "body": str(exc),
            "trace": traceback.format_exc()
        }
    }
    return JSONResponse(content=content, status_code=status.HTTP_403_FORBIDDEN)

def get_app():
    log.info('Executing get_app function')
#     db.init_app(app)
    load_modules(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return app

def load_modules(app):
    log.info(f'load_modules({app.__dict__})')

    app.include_router(
        transaction_router,
        tags=["Transaction"],
    )

    log.info(f'modules loaded')
