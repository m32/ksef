from enum import Enum

class AuthenticationMethod(str, Enum):
    INTERNALCERTIFICATE = "InternalCertificate"
    PEPPOLSIGNATURE = "PeppolSignature"
    PERSONALSIGNATURE = "PersonalSignature"
    QUALIFIEDSEAL = "QualifiedSeal"
    QUALIFIEDSIGNATURE = "QualifiedSignature"
    TOKEN = "Token"
    TRUSTEDPROFILE = "TrustedProfile"

    def __str__(self) -> str:
        return str(self.value)
