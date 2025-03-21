from enum import Enum

class V2QueryCriteriaInvoiceDetailTypeSchemaType(str, Enum):
    PEF = "PEF"
    VAT = "VAT"
    VAT_RR = "VAT_RR"

    def __str__(self) -> str:
        return str(self.value)
