from enum import Enum

class IndirectPermissionsTargetIdentifierType(str, Enum):
    ALLPARTNERS = "AllPartners"
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
