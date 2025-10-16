from enum import Enum

class InvoiceQueryDateType(str, Enum):
    INVOICING = "Invoicing"
    ISSUE = "Issue"
    PERMANENTSTORAGE = "PermanentStorage"

    def __str__(self) -> str:
        return str(self.value)
