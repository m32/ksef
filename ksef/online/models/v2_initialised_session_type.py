from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.v2_session_context_type import V2SessionContextType





T = TypeVar("T", bound="V2InitialisedSessionType")


@_attrs_define
class V2InitialisedSessionType:
    """ 
        Attributes:
            context (V2SessionContextType):
            token (str):
     """

    context: 'V2SessionContextType'
    token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.v2_session_context_type import V2SessionContextType
        context = self.context.to_dict()

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "context": context,
            "token": token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v2_session_context_type import V2SessionContextType
        d = src_dict.copy()
        context = V2SessionContextType.from_dict(d.pop("context"))




        token = d.pop("token")

        v2_initialised_session_type = cls(
            context=context,
            token=token,
        )

        v2_initialised_session_type.additional_properties = d
        return v2_initialised_session_type

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
