from enum import Enum

class V2CredentialsRoleGrantedForInstitutionInheritanceTypeRoleType(str, Enum):
    INVOICE_READ = "invoice_read"
    INVOICE_WRITE = "invoice_write"
    PAYMENT_CONFIRMATION_WRITE = "payment_confirmation_write"

    def __str__(self) -> str:
        return str(self.value)
