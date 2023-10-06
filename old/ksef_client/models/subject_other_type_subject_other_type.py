from enum import Enum


class SubjectOtherTypeSubjectOtherType(str, Enum):
    FACTOR = "factor"
    RECIPIENT = "recipient"
    ORIGINAL_SUBJECT = "original_subject"
    ADDITIONAL_PURCHASER = "additional_purchaser"
    INVOICE_ISSUER = "invoice_issuer"
    PAYER = "payer"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
