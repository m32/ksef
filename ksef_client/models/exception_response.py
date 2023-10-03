from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.exception_type import ExceptionType

T = TypeVar("T", bound="ExceptionResponse")


@attr.s(auto_attribs=True)
class ExceptionResponse:
    """
    Attributes:
        exception (ExceptionType):
    """

    exception: ExceptionType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exception = self.exception.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exception": exception,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exception = ExceptionType.from_dict(d.pop("exception"))

        exception_response = cls(
            exception=exception,
        )

        exception_response.additional_properties = d
        return exception_response

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
