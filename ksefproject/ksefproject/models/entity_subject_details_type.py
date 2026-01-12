from enum import Enum

class EntitySubjectDetailsType(str, Enum):
    ENTITYBYFINGERPRINT = "EntityByFingerprint"
    ENTITYBYIDENTIFIER = "EntityByIdentifier"

    def __str__(self) -> str:
        return str(self.value)
