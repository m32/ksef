from enum import Enum

class SubunitPermissionsContextIdentifierType(str, Enum):
    INTERNALID = "InternalId"
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
