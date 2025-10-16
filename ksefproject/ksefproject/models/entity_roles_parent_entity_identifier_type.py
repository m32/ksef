from enum import Enum

class EntityRolesParentEntityIdentifierType(str, Enum):
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
