from enum import Enum

class BuyerIdentifierType(str, Enum):
    NIP = "Nip"
    NONE = "None"
    OTHER = "Other"
    VATUE = "VatUe"

    def __str__(self) -> str:
        return str(self.value)
