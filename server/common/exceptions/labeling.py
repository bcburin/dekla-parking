from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from server.common.exceptions.httpexc_provider import IHTTPExceptionProvider


class UnauthorizedLabelingRemovalException(IHTTPExceptionProvider):

    def __init__(self, *, user_id: int, labeling_id: int):
        self.user_id = user_id
        self.labeling_id = labeling_id

    def get_http_exception(self) -> HTTPException:
        return HTTPException(status_code=HTTP_400_BAD_REQUEST,
                             detail=f'Labeling {self.labeling_id} does not belong belong to user {self.user_id}')
