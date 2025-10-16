from enum import Enum

class SubunitPermissionsSubjectIdentifierType(str, Enum):
    FINGERPRINT = "Fingerprint"
    NIP = "Nip"
    PESEL = "Pesel"

    def __str__(self) -> str:
        return str(self.value)
