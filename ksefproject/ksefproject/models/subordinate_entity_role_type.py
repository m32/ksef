from enum import Enum

class SubordinateEntityRoleType(str, Enum):
    LOCALGOVERNMENTSUBUNIT = "LocalGovernmentSubUnit"
    VATGROUPSUBUNIT = "VatGroupSubUnit"

    def __str__(self) -> str:
        return str(self.value)
