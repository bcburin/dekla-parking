from fastapi_restful.api_model import APIModel


class GenerationRequest(APIModel):
    n_users: int = 100
    n_labels: int = 10
    n_labelings: int = 100
    n_sectors: int = 10
    n_lots: int = 100
    n_bookings: int = 100


class GenerationResponse(APIModel):
    n_users: int = 0
    n_labels: int = 0
    n_labelings: int = 0
    n_sectors: int = 0
    n_lots: int = 0
    n_bookings: int = 0
