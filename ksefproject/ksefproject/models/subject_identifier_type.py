from enum import Enum

class SubjectIdentifierType(str, Enum):
    FINGERPRINT = "Fingerprint"
    NIP = "Nip"
    PESEL = "Pesel"
    TOKEN = "Token"

    def __str__(self) -> str:
        return str(self.value)
