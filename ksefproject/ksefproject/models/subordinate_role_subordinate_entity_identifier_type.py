from enum import Enum

class SubordinateRoleSubordinateEntityIdentifierType(str, Enum):
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
