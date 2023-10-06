from enum import Enum


class QueryCriteriaCredentialsAllTypeQueryCredentialsScopeResultType(str, Enum):
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
