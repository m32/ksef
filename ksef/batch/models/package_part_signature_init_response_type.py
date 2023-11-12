from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from ..models.package_part_signature_init_response_type_method import PackagePartSignatureInitResponseTypeMethod
from typing import Union
from ..types import UNSET, Unset
from typing import cast
from typing import cast, List

if TYPE_CHECKING:
  from ..models.header_entry_type import HeaderEntryType





T = TypeVar("T", bound="PackagePartSignatureInitResponseType")


@_attrs_define
class PackagePartSignatureInitResponseType:
    """ 
        Attributes:
            method (PackagePartSignatureInitResponseTypeMethod):
            ordinal_number (int):
            part_file_name (str):
            url (str):
            header_entry_list (Union[Unset, List['HeaderEntryType']]):
     """

    method: PackagePartSignatureInitResponseTypeMethod
    ordinal_number: int
    part_file_name: str
    url: str
    header_entry_list: Union[Unset, List['HeaderEntryType']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.header_entry_type import HeaderEntryType
        method = self.method.value

        ordinal_number = self.ordinal_number
        part_file_name = self.part_file_name
        url = self.url
        header_entry_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.header_entry_list, Unset):
            header_entry_list = []
            for header_entry_list_item_data in self.header_entry_list:
                header_entry_list_item = header_entry_list_item_data.to_dict()

                header_entry_list.append(header_entry_list_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "ordinalNumber": ordinal_number,
            "partFileName": part_file_name,
            "url": url,
        })
        if header_entry_list is not UNSET:
            field_dict["headerEntryList"] = header_entry_list

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.header_entry_type import HeaderEntryType
        d = src_dict.copy()
        method = PackagePartSignatureInitResponseTypeMethod(d.pop("method"))




        ordinal_number = d.pop("ordinalNumber")

        part_file_name = d.pop("partFileName")

        url = d.pop("url")

        header_entry_list = []
        _header_entry_list = d.pop("headerEntryList", UNSET)
        for header_entry_list_item_data in (_header_entry_list or []):
            header_entry_list_item = HeaderEntryType.from_dict(header_entry_list_item_data)



            header_entry_list.append(header_entry_list_item)


        package_part_signature_init_response_type = cls(
            method=method,
            ordinal_number=ordinal_number,
            part_file_name=part_file_name,
            url=url,
            header_entry_list=header_entry_list,
        )

        package_part_signature_init_response_type.additional_properties = d
        return package_part_signature_init_response_type

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
