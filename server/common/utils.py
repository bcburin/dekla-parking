from abc import ABC, abstractmethod
from datetime import datetime

from server.common.models.base import IntervalModel, BaseModel


def get_is_active(*, obj: type[IntervalModel], ref_time: datetime = datetime.now()) -> bool:
    if obj.start_time and obj.end_time:
        return obj.start_time < ref_time < obj.end_time
    if obj.start_time:
        return bool(obj.start_time < ref_time)
    if obj.end_time:
        return bool(ref_time < obj.end_time)
    # Both start_time and end_time are null
    return True


def get_is_expired(*, obj: type[IntervalModel], ref_time: datetime = datetime.now()) -> bool:
    if obj.end_time:
        return ref_time > obj.end_time
    return False


class IMockDataGenerator(ABC):

    @abstractmethod
    def generate_mock_data(self, n: int, /) -> list[BaseModel]:
        """
        :param n: number of mock entries to create
        :return: list of entries created
        """
        pass
