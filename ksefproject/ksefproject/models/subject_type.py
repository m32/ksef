from enum import Enum

class SubjectType(str, Enum):
    ENFORCEMENTAUTHORITY = "EnforcementAuthority"
    JST = "JST"
    VATGROUP = "VatGroup"

    def __str__(self) -> str:
        return str(self.value)
