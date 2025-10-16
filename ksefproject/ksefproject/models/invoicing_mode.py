from enum import Enum

class InvoicingMode(str, Enum):
    OFFLINE = "Offline"
    ONLINE = "Online"

    def __str__(self) -> str:
        return str(self.value)
