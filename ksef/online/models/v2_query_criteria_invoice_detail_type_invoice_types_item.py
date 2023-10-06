from enum import Enum

class V2QueryCriteriaInvoiceDetailTypeInvoiceTypesItem(str, Enum):
    KOR = "KOR"
    KOR_ROZ = "KOR_ROZ"
    KOR_ZAL = "KOR_ZAL"
    ROZ = "ROZ"
    UPR = "UPR"
    VAT = "VAT"
    ZAL = "ZAL"

    def __str__(self) -> str:
        return str(self.value)
