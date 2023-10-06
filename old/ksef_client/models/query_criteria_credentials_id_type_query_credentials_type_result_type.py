from enum import Enum


class QueryCriteriaCredentialsIdTypeQueryCredentialsTypeResultType(str, Enum):
    ALL = "all"
    STANDARD = "standard"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)
