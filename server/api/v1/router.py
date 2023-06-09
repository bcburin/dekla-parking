from os import getenv

from fastapi import APIRouter
from starlette.responses import RedirectResponse

from server.api.v1.endpoints import user
from server.api.v1.endpoints import label
from server.api.v1.endpoints import lot
from server.api.v1.endpoints import sector
from server.api.v1.endpoints import exclusive_policy
from server.api.v1.endpoints import public_policy
from server.api.v1.endpoints import bookings
from server.api.v1.endpoints import labeling
from  server.api.v1.endpoints import ep_permission

router = APIRouter(prefix='/v1')

router.include_router(user.router)
router.include_router(label.router)
router.include_router(lot.router)
router.include_router(sector.router)
router.include_router(exclusive_policy.router)
router.include_router(public_policy.router)
router.include_router(bookings.router)
router.include_router(labeling.router)
router.include_router(ep_permission.router)


if getenv('DEV_MODE'):
    from server.api.v1.endpoints import dev
    router.include_router(dev.router)


@router.get('/')
async def v1_root():
    return RedirectResponse(url='/docs')
