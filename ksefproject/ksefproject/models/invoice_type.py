from enum import Enum

class InvoiceType(str, Enum):
    KOR = "Kor"
    KORPEF = "KorPef"
    KORROZ = "KorRoz"
    KORVATRR = "KorVatRr"
    KORZAL = "KorZal"
    ROZ = "Roz"
    UPR = "Upr"
    VAT = "Vat"
    VATPEF = "VatPef"
    VATPEFSP = "VatPefSp"
    VATRR = "VatRr"
    ZAL = "Zal"

    def __str__(self) -> str:
        return str(self.value)
