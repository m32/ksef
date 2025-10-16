from enum import Enum

class InvoiceQuerySubjectType(str, Enum):
    SUBJECT1 = "Subject1"
    SUBJECT2 = "Subject2"
    SUBJECT3 = "Subject3"
    SUBJECTAUTHORIZED = "SubjectAuthorized"

    def __str__(self) -> str:
        return str(self.value)
