class ObjectDoesNotExist(Exception):
    def __init__(self, err_msg: str) -> None:
        self.msg = err_msg


class DuplicateRecordError(Exception):
    def __init__(self, err_msg: str) -> None:
        self.msg = err_msg
