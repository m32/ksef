from enum import Enum

class AmountType(str, Enum):
    BRUTTO = "Brutto"
    NETTO = "Netto"
    VAT = "Vat"

    def __str__(self) -> str:
        return str(self.value)
