from enum import Enum

class EntityAuthorizationPermissionType(str, Enum):
    PEFINVOICING = "PefInvoicing"
    RRINVOICING = "RRInvoicing"
    SELFINVOICING = "SelfInvoicing"
    TAXREPRESENTATIVE = "TaxRepresentative"

    def __str__(self) -> str:
        return str(self.value)
