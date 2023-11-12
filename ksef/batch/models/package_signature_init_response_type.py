from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from typing import cast, List

if TYPE_CHECKING:
  from ..models.package_part_signature_init_response_type import PackagePartSignatureInitResponseType





T = TypeVar("T", bound="PackageSignatureInitResponseType")


@_attrs_define
class PackageSignatureInitResponseType:
    """ 
        Attributes:
            package_name (str):
            package_part_signature_list (List['PackagePartSignatureInitResponseType']):
     """

    package_name: str
    package_part_signature_list: List['PackagePartSignatureInitResponseType']
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.package_part_signature_init_response_type import PackagePartSignatureInitResponseType
        package_name = self.package_name
        package_part_signature_list = []
        for package_part_signature_list_item_data in self.package_part_signature_list:
            package_part_signature_list_item = package_part_signature_list_item_data.to_dict()

            package_part_signature_list.append(package_part_signature_list_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "packageName": package_name,
            "packagePartSignatureList": package_part_signature_list,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_part_signature_init_response_type import PackagePartSignatureInitResponseType
        d = src_dict.copy()
        package_name = d.pop("packageName")

        package_part_signature_list = []
        _package_part_signature_list = d.pop("packagePartSignatureList")
        for package_part_signature_list_item_data in (_package_part_signature_list):
            package_part_signature_list_item = PackagePartSignatureInitResponseType.from_dict(package_part_signature_list_item_data)



            package_part_signature_list.append(package_part_signature_list_item)


        package_signature_init_response_type = cls(
            package_name=package_name,
            package_part_signature_list=package_part_signature_list,
        )

        package_signature_init_response_type.additional_properties = d
        return package_signature_init_response_type

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
