from enum import Enum

class InvoiceQueryFormType(str, Enum):
    FA = "FA"
    PEF = "PEF"
    RR = "RR"

    def __str__(self) -> str:
        return str(self.value)
