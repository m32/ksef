from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ExceptionDetailType")


@attr.s(auto_attribs=True)
class ExceptionDetailType:
    """
    Attributes:
        exception_code (int):
        exception_description (str):
    """

    exception_code: int
    exception_description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exception_code = self.exception_code
        exception_description = self.exception_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exceptionCode": exception_code,
                "exceptionDescription": exception_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exception_code = d.pop("exceptionCode")

        exception_description = d.pop("exceptionDescription")

        exception_detail_type = cls(
            exception_code=exception_code,
            exception_description=exception_description,
        )

        exception_detail_type.additional_properties = d
        return exception_detail_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
