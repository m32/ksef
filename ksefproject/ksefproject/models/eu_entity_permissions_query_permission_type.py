from enum import Enum

class EuEntityPermissionsQueryPermissionType(str, Enum):
    INTROSPECTION = "Introspection"
    INVOICEREAD = "InvoiceRead"
    INVOICEWRITE = "InvoiceWrite"
    VATUEMANAGE = "VatUeManage"

    def __str__(self) -> str:
        return str(self.value)
