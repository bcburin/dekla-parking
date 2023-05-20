from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from server.api import v1
from server.common.exceptions.httpexc_provider import IHTTPExceptionProvider

api = FastAPI(
    title='Dekla Parking API',
    version='1.0.0'
)

api.include_router(v1.router)


@api.exception_handler(IHTTPExceptionProvider)
async def handle_db_exceptions(_: Request, exc: IHTTPExceptionProvider):
    http_exc = exc.get_http_exception()
    return JSONResponse(status_code=http_exc.status_code, content={'detail': http_exc.detail})
