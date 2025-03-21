from enum import Enum

class AuthenticationIdentifierTypeType(str, Enum):
    FINGERPRINT = "fingerprint"
    NIP = "nip"
    ONIP = "onip"
    PEPPOL = "peppol"
    PESEL = "pesel"

    def __str__(self) -> str:
        return str(self.value)
