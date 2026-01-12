from enum import Enum

class EntitySubjectByIdentifierDetailsType(str, Enum):
    ENTITYBYIDENTIFIER = "EntityByIdentifier"

    def __str__(self) -> str:
        return str(self.value)
