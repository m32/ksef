from enum import Enum

class ThirdSubjectIdentifierType(str, Enum):
    INTERNALID = "InternalId"
    NIP = "Nip"
    NONE = "None"
    OTHER = "Other"
    VATUE = "VatUe"

    def __str__(self) -> str:
        return str(self.value)
