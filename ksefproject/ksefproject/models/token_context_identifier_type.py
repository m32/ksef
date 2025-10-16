from enum import Enum

class TokenContextIdentifierType(str, Enum):
    INTERNALID = "InternalId"
    NIP = "Nip"
    NIPVATUE = "NipVatUe"
    PEPPOLID = "PeppolId"

    def __str__(self) -> str:
        return str(self.value)
