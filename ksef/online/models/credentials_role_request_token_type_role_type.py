from enum import Enum

class CredentialsRoleRequestTokenTypeRoleType(str, Enum):
    CREDENTIALS_MANAGE = "credentials_manage"
    CREDENTIALS_READ = "credentials_read"
    ENFORCEMENT_OPERATIONS = "enforcement_operations"
    INVOICE_READ = "invoice_read"
    INVOICE_WRITE = "invoice_write"
    PAYMENT_CONFIRMATION_WRITE = "payment_confirmation_write"

    def __str__(self) -> str:
        return str(self.value)
