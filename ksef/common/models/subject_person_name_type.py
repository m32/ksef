from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Optional
from typing import Union
from ..types import UNSET, Unset






T = TypeVar("T", bound="SubjectPersonNameType")


@_attrs_define
class SubjectPersonNameType:
    """ 
        Attributes:
            type (str):
            first_name (str):
            surname (str):
            trade_name (Union[Unset, None, str]):
     """

    type: str
    first_name: str
    surname: str
    trade_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        first_name = self.first_name
        surname = self.surname
        trade_name = self.trade_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
            "firstName": first_name,
            "surname": surname,
        })
        if trade_name is not UNSET:
            field_dict["tradeName"] = trade_name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        first_name = d.pop("firstName")

        surname = d.pop("surname")

        trade_name = d.pop("tradeName", UNSET)

        subject_person_name_type = cls(
            type=type,
            first_name=first_name,
            surname=surname,
            trade_name=trade_name,
        )

        subject_person_name_type.additional_properties = d
        return subject_person_name_type

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
