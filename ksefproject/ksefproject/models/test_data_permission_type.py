from enum import Enum

class TestDataPermissionType(str, Enum):
    CREDENTIALSMANAGE = "CredentialsManage"
    CREDENTIALSREAD = "CredentialsRead"
    ENFORCEMENTOPERATIONS = "EnforcementOperations"
    INTROSPECTION = "Introspection"
    INVOICEREAD = "InvoiceRead"
    INVOICEWRITE = "InvoiceWrite"
    SUBUNITMANAGE = "SubunitManage"

    def __str__(self) -> str:
        return str(self.value)
