from enum import Enum

class CertificateListItemStatus(str, Enum):
    ACTIVE = "Active"
    BLOCKED = "Blocked"
    EXPIRED = "Expired"
    REVOKED = "Revoked"

    def __str__(self) -> str:
        return str(self.value)
