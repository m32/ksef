from enum import Enum

class CredentialsRoleRequestContextDescribedTypeRoleType(str, Enum):
    CREDENTIALS_MANAGE = "credentials_manage"

    def __str__(self) -> str:
        return str(self.value)
