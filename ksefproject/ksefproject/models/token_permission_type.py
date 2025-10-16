from enum import Enum

class TokenPermissionType(str, Enum):
    CREDENTIALSMANAGE = "CredentialsManage"
    CREDENTIALSREAD = "CredentialsRead"
    ENFORCEMENTOPERATIONS = "EnforcementOperations"
    INVOICEREAD = "InvoiceRead"
    INVOICEWRITE = "InvoiceWrite"
    SUBUNITMANAGE = "SubunitManage"

    def __str__(self) -> str:
        return str(self.value)
