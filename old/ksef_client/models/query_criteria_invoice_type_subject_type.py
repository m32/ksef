from enum import Enum


class QueryCriteriaInvoiceTypeSubjectType(str, Enum):
    SUBJECT1 = "subject1"
    SUBJECT2 = "subject2"
    SUBJECT3 = "subject3"
    SUBJECTAUTHORIZED = "subjectAuthorized"

    def __str__(self) -> str:
        return str(self.value)
