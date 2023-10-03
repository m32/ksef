from enum import Enum


class QueryInvoiceAsyncStatusResponseDivisionType(str, Enum):
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
