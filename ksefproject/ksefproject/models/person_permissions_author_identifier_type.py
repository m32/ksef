from enum import Enum

class PersonPermissionsAuthorIdentifierType(str, Enum):
    FINGERPRINT = "Fingerprint"
    NIP = "Nip"
    PESEL = "Pesel"
    SYSTEM = "System"

    def __str__(self) -> str:
        return str(self.value)
