from enum import Enum

class KsefCertificateType(str, Enum):
    AUTHENTICATION = "Authentication"
    OFFLINE = "Offline"

    def __str__(self) -> str:
        return str(self.value)
