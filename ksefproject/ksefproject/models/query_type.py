from enum import Enum

class QueryType(str, Enum):
    GRANTED = "Granted"
    RECEIVED = "Received"

    def __str__(self) -> str:
        return str(self.value)
