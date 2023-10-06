from enum import Enum

class QueryCriteriaInvoiceDetailTypeAmountType(str, Enum):
    BRUTTO = "brutto"
    NETTO = "netto"
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
