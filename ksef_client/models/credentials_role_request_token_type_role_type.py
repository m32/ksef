from enum import Enum


class CredentialsRoleRequestTokenTypeRoleType(str, Enum):
    INVOICE_READ = "invoice_read"
    INVOICE_WRITE = "invoice_write"
    PAYMENT_CONFIRMATION_WRITE = "payment_confirmation_write"
    CREDENTIALS_READ = "credentials_read"
    CREDENTIALS_MANAGE = "credentials_manage"
    ENFORCEMENT_OPERATIONS = "enforcement_operations"

    def __str__(self) -> str:
        return str(self.value)
