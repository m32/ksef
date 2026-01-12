from enum import Enum

class PersonSubjectByFingerprintDetailsType(str, Enum):
    PERSONBYFINGERPRINTWITHIDENTIFIER = "PersonByFingerprintWithIdentifier"
    PERSONBYFINGERPRINTWITHOUTIDENTIFIER = "PersonByFingerprintWithoutIdentifier"

    def __str__(self) -> str:
        return str(self.value)
