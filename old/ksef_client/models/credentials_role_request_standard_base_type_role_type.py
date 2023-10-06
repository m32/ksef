from enum import Enum


class CredentialsRoleRequestStandardBaseTypeRoleType(str, Enum):
    INVOICE_READ = "invoice_read"
    INVOICE_WRITE = "invoice_write"
    PAYMENT_CONFIRMATION_WRITE = "payment_confirmation_write"
    CREDENTIALS_READ = "credentials_read"
    CREDENTIALS_MANAGE = "credentials_manage"
    SELF_INVOICING = "self_invoicing"
    TAX_REPRESENTATIVE = "tax_representative"
    ENFORCEMENT_OPERATIONS = "enforcement_operations"

    def __str__(self) -> str:
        return str(self.value)
