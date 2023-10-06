from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credentials_base_type_object_identifier import CredentialsBaseTypeObjectIdentifier
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialsBaseTypeObject")


@attr.s(auto_attribs=True)
class CredentialsBaseTypeObject:
    """
    Attributes:
        type (str):
        identifier (Union[Unset, CredentialsBaseTypeObjectIdentifier]):
    """

    type: str
    identifier: Union[Unset, CredentialsBaseTypeObjectIdentifier] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _identifier = d.pop("identifier", UNSET)
        identifier: Union[Unset, CredentialsBaseTypeObjectIdentifier]
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = CredentialsBaseTypeObjectIdentifier.from_dict(_identifier)

        credentials_base_type_object = cls(
            type=type,
            identifier=identifier,
        )

        credentials_base_type_object.additional_properties = d
        return credentials_base_type_object

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
