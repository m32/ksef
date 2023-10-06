from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.session_context_type import SessionContextType





T = TypeVar("T", bound="InitialisedSessionType")


@_attrs_define
class InitialisedSessionType:
    """ 
        Attributes:
            context (SessionContextType):
            token (str):
     """

    context: 'SessionContextType'
    token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.session_context_type import SessionContextType
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
        from ..models.session_context_type import SessionContextType
        d = src_dict.copy()
        context = SessionContextType.from_dict(d.pop("context"))




        token = d.pop("token")

        initialised_session_type = cls(
            context=context,
            token=token,
        )

        initialised_session_type.additional_properties = d
        return initialised_session_type

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
