from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.exception_type import ExceptionType





T = TypeVar("T", bound="ExceptionResponse")


@_attrs_define
class ExceptionResponse:
    """ 
        Attributes:
            exception (ExceptionType):
     """

    exception: 'ExceptionType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.exception_type import ExceptionType
        exception = self.exception.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exception": exception,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exception_type import ExceptionType
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
