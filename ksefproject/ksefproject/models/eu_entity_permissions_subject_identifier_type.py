from enum import Enum

class EuEntityPermissionsSubjectIdentifierType(str, Enum):
    FINGERPRINT = "Fingerprint"

    def __str__(self) -> str:
        return str(self.value)
