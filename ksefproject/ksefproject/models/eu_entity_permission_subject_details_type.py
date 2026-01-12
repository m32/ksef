from enum import Enum

class EuEntityPermissionSubjectDetailsType(str, Enum):
    ENTITYBYFINGERPRINT = "EntityByFingerprint"
    PERSONBYFINGERPRINTWITHIDENTIFIER = "PersonByFingerprintWithIdentifier"
    PERSONBYFINGERPRINTWITHOUTIDENTIFIER = "PersonByFingerprintWithoutIdentifier"

    def __str__(self) -> str:
        return str(self.value)
