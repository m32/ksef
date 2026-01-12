from enum import Enum

class EntitySubjectByFingerprintDetailsType(str, Enum):
    ENTITYBYFINGERPRINT = "EntityByFingerprint"

    def __str__(self) -> str:
        return str(self.value)
