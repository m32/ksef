from enum import Enum

class PersonPermissionsQueryType(str, Enum):
    PERMISSIONSGRANTEDINCURRENTCONTEXT = "PermissionsGrantedInCurrentContext"
    PERMISSIONSINCURRENTCONTEXT = "PermissionsInCurrentContext"

    def __str__(self) -> str:
        return str(self.value)
