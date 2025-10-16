from enum import Enum

class PersonalPermissionScope(str, Enum):
    CREDENTIALSMANAGE = "CredentialsManage"
    CREDENTIALSREAD = "CredentialsRead"
    ENFORCEMENTOPERATIONS = "EnforcementOperations"
    INTROSPECTION = "Introspection"
    INVOICEREAD = "InvoiceRead"
    INVOICEWRITE = "InvoiceWrite"
    OWNER = "Owner"
    SUBUNITMANAGE = "SubunitManage"
    VATUEMANAGE = "VatUeManage"

    def __str__(self) -> str:
        return str(self.value)
