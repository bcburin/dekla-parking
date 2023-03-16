from fastapi import APIRouter
from starlette.responses import RedirectResponse

from server.api.v1.endpoints import user

router = APIRouter(prefix='/v1')

router.include_router(user.router)


@router.get('/')
async def v1_root():
    return RedirectResponse(url='/docs')
