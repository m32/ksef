from enum import Enum

class PublicKeyCertificateUsage(str, Enum):
    KSEFTOKENENCRYPTION = "KsefTokenEncryption"
    SYMMETRICKEYENCRYPTION = "SymmetricKeyEncryption"

    def __str__(self) -> str:
        return str(self.value)
