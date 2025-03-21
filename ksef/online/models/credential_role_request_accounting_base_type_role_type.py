from enum import Enum

class CredentialRoleRequestAccountingBaseTypeRoleType(str, Enum):
    INVOICE_READ = "invoice_read"
    INVOICE_WRITE = "invoice_write"

    def __str__(self) -> str:
        return str(self.value)
