from enum import Enum

class PersonalPermissionsContextIdentifierType(str, Enum):
    NIP = "Nip"

    def __str__(self) -> str:
        return str(self.value)
