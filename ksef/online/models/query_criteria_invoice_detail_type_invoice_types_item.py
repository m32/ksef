from enum import Enum

class QueryCriteriaInvoiceDetailTypeInvoiceTypesItem(str, Enum):
    KOR = "KOR"
    KOR_PEF = "KOR_PEF"
    KOR_ROZ = "KOR_ROZ"
    KOR_ZAL = "KOR_ZAL"
    ROZ = "ROZ"
    UPR = "UPR"
    VAT = "VAT"
    VAT_PEF = "VAT_PEF"
    VAT_PEF_SP = "VAT_PEF_SP"
    ZAL = "ZAL"

    def __str__(self) -> str:
        return str(self.value)
