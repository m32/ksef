from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectFullNameType")


@attr.s(auto_attribs=True)
class SubjectFullNameType:
    """
    Attributes:
        type (str):
        full_name (str):
        trade_name (Union[Unset, str]):
    """

    type: str
    full_name: str
    trade_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        full_name = self.full_name
        trade_name = self.trade_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "fullName": full_name,
            }
        )
        if trade_name is not UNSET:
            field_dict["tradeName"] = trade_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        full_name = d.pop("fullName")

        trade_name = d.pop("tradeName", UNSET)

        subject_full_name_type = cls(
            type=type,
            full_name=full_name,
            trade_name=trade_name,
        )

        subject_full_name_type.additional_properties = d
        return subject_full_name_type

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
