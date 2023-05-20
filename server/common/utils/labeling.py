from datetime import datetime

from server.common.models.labeling import LabelingModel


def get_labeling_is_active(labeling: LabelingModel) -> bool:
    current_time = datetime.now()
    if labeling.start_time and labeling.end_time:
        return labeling.start_time < current_time < labeling.end_time
    if labeling.start_time:
        return bool(labeling.start_time < current_time)
    if labeling.end_time:
        return bool(current_time < labeling.end_time)
    # Both start_time and end_time are null
    return True


def get_labeling_is_expired(labeling: LabelingModel) -> bool:
    current_time = datetime.now()
    if labeling.end_time:
        return current_time > labeling.end_time
    return False
