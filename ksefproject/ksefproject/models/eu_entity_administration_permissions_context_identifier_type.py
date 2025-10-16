from enum import Enum

class EuEntityAdministrationPermissionsContextIdentifierType(str, Enum):
    NIPVATUE = "NipVatUe"

    def __str__(self) -> str:
        return str(self.value)
