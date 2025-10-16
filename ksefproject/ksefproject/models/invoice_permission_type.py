from enum import Enum

class InvoicePermissionType(str, Enum):
    PEFINVOICING = "PefInvoicing"
    RRINVOICING = "RRInvoicing"
    SELFINVOICING = "SelfInvoicing"
    TAXREPRESENTATIVE = "TaxRepresentative"

    def __str__(self) -> str:
        return str(self.value)
