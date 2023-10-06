from enum import Enum

class V2QueryCriteriaInvoiceDetailTypeAmountType(str, Enum):
    BRUTTO = "brutto"
    NETTO = "netto"
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
