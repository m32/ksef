from enum import Enum

class PersonPermissionsTargetIdentifierType(str, Enum):
    ALLPARTNERS = "AllPartners"
    INTERNALID = "InternalId"
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
