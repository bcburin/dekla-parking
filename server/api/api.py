from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from server.api import v1
from server.common.exceptions.httpexc_provider import IHTTPExceptionProvider

from server.common.models.sector import *
from server.common.models.ep_permission import *
from server.common.models.exclusive_policy import *
from server.common.models.booking import *
from server.common.models.label import *
from server.common.models.labeling import *
from server.common.models.lot import *
from server.common.models.public_policy import *
from server.common.models.user import *

api = FastAPI(
    title='Dekla Parking API',
    version='1.0.0'
)

api.include_router(v1.router)

origins = ["http://localhost:3000"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@api.exception_handler(IHTTPExceptionProvider)
async def handle_db_exceptions(_: Request, exc: IHTTPExceptionProvider):
    http_exc = exc.get_http_exception()
    return JSONResponse(status_code=http_exc.status_code, content={'detail': http_exc.detail})
