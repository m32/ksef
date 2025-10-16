from enum import Enum

class IndirectPermissionType(str, Enum):
    INVOICEREAD = "InvoiceRead"
    INVOICEWRITE = "InvoiceWrite"

    def __str__(self) -> str:
        return str(self.value)
