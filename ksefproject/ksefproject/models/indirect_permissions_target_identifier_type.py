from enum import Enum

class IndirectPermissionsTargetIdentifierType(str, Enum):
    ALLPARTNERS = "AllPartners"
    INTERNALID = "InternalId"
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
