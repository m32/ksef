from enum import Enum


class QueryCriteriaCredentialsAllTypeQueryCredentialsTypeResultType(str, Enum):
    ALL = "all"
    STANDARD = "standard"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)
