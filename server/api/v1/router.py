from fastapi import APIRouter
from starlette.responses import RedirectResponse

from server.api.v1.endpoints import user
from server.api.v1.endpoints import label
from server.api.v1.endpoints import lot
from server.api.v1.endpoints import sector
from server.api.v1.endpoints import exclusive_policy
from server.api.v1.endpoints import public_policy
from server.api.v1.endpoints import bookings

router = APIRouter(prefix='/v1')

router.include_router(user.router)
router.include_router(label.router)
router.include_router(lot.router)
router.include_router(sector.router)
router.include_router(exclusive_policy.router)
router.include_router(public_policy.router)
router.include_router(bookings.router)


@router.get('/')
async def v1_root():
    return RedirectResponse(url='/docs')
