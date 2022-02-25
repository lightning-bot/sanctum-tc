__all__ = ("HTTPException", )

class HTTPException(Exception):
    def __init__(self, status_code, data) -> None:
        self.status_code = status_code
        self.data = data
        super().__init__(f"Got {status_code} with message {data}")