from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpoPageType")


@_attrs_define
class UpoPageType:
    """ 
        Attributes:
            upo_page_number (int):
            upo_reference_number (str):
            upo_url (str):
     """

    upo_page_number: int
    upo_reference_number: str
    upo_url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        upo_page_number = self.upo_page_number
        upo_reference_number = self.upo_reference_number
        upo_url = self.upo_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "upoPageNumber": upo_page_number,
            "upoReferenceNumber": upo_reference_number,
            "upoUrl": upo_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upo_page_number = d.pop("upoPageNumber")

        upo_reference_number = d.pop("upoReferenceNumber")

        upo_url = d.pop("upoUrl")

        upo_page_type = cls(
            upo_page_number=upo_page_number,
            upo_reference_number=upo_reference_number,
            upo_url=upo_url,
        )

        upo_page_type.additional_properties = d
        return upo_page_type

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
