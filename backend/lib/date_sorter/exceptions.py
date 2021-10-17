

class WrongInputDate(Exception):
    cause: str
    
    def __init__(self, cause: str) -> None:
        self.cause = cause
        super().__init__(cause)