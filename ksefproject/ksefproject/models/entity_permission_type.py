from enum import Enum

class EntityPermissionType(str, Enum):
    INVOICEREAD = "InvoiceRead"
    INVOICEWRITE = "InvoiceWrite"

    def __str__(self) -> str:
        return str(self.value)
