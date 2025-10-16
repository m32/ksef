from enum import Enum

class SessionType(str, Enum):
    BATCH = "Batch"
    ONLINE = "Online"

    def __str__(self) -> str:
        return str(self.value)
