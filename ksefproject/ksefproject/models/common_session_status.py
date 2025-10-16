from enum import Enum

class CommonSessionStatus(str, Enum):
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    INPROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
