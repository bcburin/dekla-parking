from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from server.common.exceptions.httpexc_provider import IHTTPExceptionProvider


class UnauthorizedBookingRemovalException(IHTTPExceptionProvider):

    def __init__(self, *, user_id: int, booking_id: int):
        self.user_id = user_id
        self.booking_id = booking_id

    def get_http_exception(self) -> HTTPException:
        return HTTPException(status_code=HTTP_400_BAD_REQUEST,
                             detail=f'Booking {self.booking_id} does not belong belong to user {self.user_id}')
