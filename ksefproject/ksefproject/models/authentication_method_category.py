from enum import Enum

class AuthenticationMethodCategory(str, Enum):
    NATIONALNODE = "NationalNode"
    OTHER = "Other"
    TOKEN = "Token"
    XADESSIGNATURE = "XadesSignature"

    def __str__(self) -> str:
        return str(self.value)
