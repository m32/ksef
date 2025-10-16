from enum import Enum

class EntityRoleType(str, Enum):
    COURTBAILIFF = "CourtBailiff"
    ENFORCEMENTAUTHORITY = "EnforcementAuthority"
    LOCALGOVERNMENTSUBUNIT = "LocalGovernmentSubUnit"
    LOCALGOVERNMENTUNIT = "LocalGovernmentUnit"
    VATGROUPSUBUNIT = "VatGroupSubUnit"
    VATGROUPUNIT = "VatGroupUnit"

    def __str__(self) -> str:
        return str(self.value)
