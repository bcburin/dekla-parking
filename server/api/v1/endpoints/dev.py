from os import getenv

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.common.exceptions.auth import AuthException
from server.common.schemas.generator import GenerationRequest, GenerationResponse
from server.database.config import get_db
from server.services.auth import AuthReq
from server.services.booking import BookingService
from server.services.label import LabelService
from server.services.labeling import LabelingService
from server.services.lot import LotService
from server.services.sector import SectorService
from server.services.user import UserService

router = APIRouter(prefix='/data-generator', tags=['development'])


@router.post('/', response_model=GenerationResponse, dependencies=[Depends(AuthReq.current_user_has_permission)])
def generate_mock_data(req: GenerationRequest, db: Session = Depends(get_db)):
    if not getenv('DEV_MODE'):
        raise AuthException('Data generation only available in dev mode.')
    users = UserService(db).generate_mock_data(req.n_users)
    labels = LabelService(db).generate_mock_data(req.n_labels)
    labelings = LabelingService(db).generate_mock_data(req.n_labelings)
    sectors = SectorService(db).generate_mock_data(req.n_sectors)
    lots = LotService(db).generate_mock_data(req.n_lots)
    bookings = BookingService(db).generate_mock_data(req.n_bookings)
    return GenerationResponse(
        n_users=len(users),
        n_labels=len(labels),
        n_labelings=len(labelings),
        n_sectors=len(sectors),
        n_lots=len(lots),
        n_bookings=len(bookings)
    )