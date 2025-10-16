from enum import Enum

class AuthenticationTokenStatus(str, Enum):
    ACTIVE = "Active"
    FAILED = "Failed"
    PENDING = "Pending"
    REVOKED = "Revoked"
    REVOKING = "Revoking"

    def __str__(self) -> str:
        return str(self.value)
