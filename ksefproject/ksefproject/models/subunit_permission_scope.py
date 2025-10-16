from enum import Enum

class SubunitPermissionScope(str, Enum):
    CREDENTIALSMANAGE = "CredentialsManage"

    def __str__(self) -> str:
        return str(self.value)
