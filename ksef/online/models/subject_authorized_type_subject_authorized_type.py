from enum import Enum

class SubjectAuthorizedTypeSubjectAuthorizedType(str, Enum):
    COURT_BAILIFF = "court_bailiff"
    ENFORCEMENT_AUTHORITY = "enforcement_authority"
    TAX_REPRESENTATIVE = "tax_representative"

    def __str__(self) -> str:
        return str(self.value)
