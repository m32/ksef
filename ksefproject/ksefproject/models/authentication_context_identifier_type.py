from enum import Enum

class AuthenticationContextIdentifierType(str, Enum):
    INTERNALID = "InternalId"
    NIP = "Nip"
    NIPVATUE = "NipVatUe"
    PEPPOLID = "PeppolId"

    def __str__(self) -> str:
        return str(self.value)
