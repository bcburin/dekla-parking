from fastapi import APIRouter
from starlette.responses import RedirectResponse

from server.api.v1.endpoints import user
from server.api.v1.endpoints import label
from server.api.v1.endpoints import lot

router = APIRouter(prefix='/v1')

router.include_router(user.router)
router.include_router(label.router)
router.include_router(lot.router)


@router.get('/')
async def v1_root():
    return RedirectResponse(url='/docs')
