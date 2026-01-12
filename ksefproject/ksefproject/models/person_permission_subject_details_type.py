from enum import Enum

class PersonPermissionSubjectDetailsType(str, Enum):
    PERSONBYFINGERPRINTWITHIDENTIFIER = "PersonByFingerprintWithIdentifier"
    PERSONBYFINGERPRINTWITHOUTIDENTIFIER = "PersonByFingerprintWithoutIdentifier"
    PERSONBYIDENTIFIER = "PersonByIdentifier"

    def __str__(self) -> str:
        return str(self.value)
