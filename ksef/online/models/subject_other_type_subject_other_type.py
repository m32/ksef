from enum import Enum

class SubjectOtherTypeSubjectOtherType(str, Enum):
    ADDITIONAL_PURCHASER = "additional_purchaser"
    FACTOR = "factor"
    INVOICE_ISSUER = "invoice_issuer"
    ORIGINAL_SUBJECT = "original_subject"
    OTHER = "other"
    PAYER = "payer"
    RECIPIENT = "recipient"

    def __str__(self) -> str:
        return str(self.value)
