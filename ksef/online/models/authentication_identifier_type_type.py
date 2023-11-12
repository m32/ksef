from enum import Enum

class AuthenticationIdentifierTypeType(str, Enum):
    FINGERPRINT = "fingerprint"
    NIP = "nip"
    ONIP = "onip"
    PESEL = "pesel"

    def __str__(self) -> str:
        return str(self.value)
