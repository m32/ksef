from enum import Enum

class CredentialsRoleRequestStandardBaseTypeRoleType(str, Enum):
    CREDENTIALS_MANAGE = "credentials_manage"
    CREDENTIALS_READ = "credentials_read"
    ENFORCEMENT_OPERATIONS = "enforcement_operations"
    INTROSPECTION = "introspection"
    INVOICE_READ = "invoice_read"
    INVOICE_WRITE = "invoice_write"
    PAYMENT_CONFIRMATION_WRITE = "payment_confirmation_write"
    SELF_INVOICING = "self_invoicing"
    SUBUNIT_MANAGE = "subunit_manage"
    TAX_REPRESENTATIVE = "tax_representative"

    def __str__(self) -> str:
        return str(self.value)
