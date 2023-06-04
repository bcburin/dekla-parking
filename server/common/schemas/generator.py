from fastapi_restful.api_model import APIModel


class GenerationRequest(APIModel):
    n_users: int = 0
    n_labels: int = 0
    n_labelings: int = 0
    n_sectors: int = 0
    n_lots: int = 0
    n_bookings: int = 0
    n_ppolicy: int = 0
    n_epolicy: int = 0
    n_eppermission: int = 0


class GenerationResponse(APIModel):
    n_users: int = 0
    n_labels: int = 0
    n_labelings: int = 0
    n_sectors: int = 0
    n_lots: int = 0
    n_bookings: int = 0
    n_ppolicy: int = 0
    n_epolicy: int = 0
    n_eppermission: int = 0
