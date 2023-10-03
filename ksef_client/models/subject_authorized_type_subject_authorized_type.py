from enum import Enum


class SubjectAuthorizedTypeSubjectAuthorizedType(str, Enum):
    ENFORCEMENT_AUTHORITY = "enforcement_authority"
    COURT_BAILIFF = "court_bailiff"
    TAX_REPRESENTATIVE = "tax_representative"

    def __str__(self) -> str:
        return str(self.value)
