from enum import Enum

class CertificateRevocationReason(str, Enum):
    KEYCOMPROMISE = "KeyCompromise"
    SUPERSEDED = "Superseded"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
