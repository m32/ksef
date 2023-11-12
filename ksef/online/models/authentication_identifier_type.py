from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authentication_identifier_type_type import AuthenticationIdentifierTypeType






T = TypeVar("T", bound="AuthenticationIdentifierType")


@_attrs_define
class AuthenticationIdentifierType:
    """ 
        Attributes:
            identifier (str):
            type (AuthenticationIdentifierTypeType):
     """

    identifier: str
    type: AuthenticationIdentifierTypeType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        type = self.type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "identifier": identifier,
            "type": type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        type = AuthenticationIdentifierTypeType(d.pop("type"))




        authentication_identifier_type = cls(
            identifier=identifier,
            type=type,
        )

        authentication_identifier_type.additional_properties = d
        return authentication_identifier_type

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
