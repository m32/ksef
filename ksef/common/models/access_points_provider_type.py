from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AccessPointsProviderType")


@_attrs_define
class AccessPointsProviderType:
    """ 
        Attributes:
            name_app (str):
            numer_app (str):
     """

    name_app: str
    numer_app: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name_app = self.name_app
        numer_app = self.numer_app

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nameAPP": name_app,
            "numerAPP": numer_app,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name_app = d.pop("nameAPP")

        numer_app = d.pop("numerAPP")

        access_points_provider_type = cls(
            name_app=name_app,
            numer_app=numer_app,
        )

        access_points_provider_type.additional_properties = d
        return access_points_provider_type

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
