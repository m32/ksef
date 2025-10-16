from enum import Enum

class EntityAuthorizationsAuthorizedEntityIdentifierType(str, Enum):
    NIP = "Nip"
    PEPPOLID = "PeppolId"

    def __str__(self) -> str:
        return str(self.value)
