from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from typing import Union
from dateutil.parser import isoparse
import datetime
from typing import cast, List
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.upo_page_type import UpoPageType





T = TypeVar("T", bound="V4StatusResponse")


@_attrs_define
class V4StatusResponse:
    """ 
        Attributes:
            processing_code (int):
            processing_description (str):
            reference_number (str):
            timestamp (datetime.datetime):
            upo_page_count (int):
            upo_page_list (Union[Unset, List['UpoPageType']]):
     """

    processing_code: int
    processing_description: str
    reference_number: str
    timestamp: datetime.datetime
    upo_page_count: int
    upo_page_list: Union[Unset, List['UpoPageType']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.upo_page_type import UpoPageType
        processing_code = self.processing_code
        processing_description = self.processing_description
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()

        upo_page_count = self.upo_page_count
        upo_page_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.upo_page_list, Unset):
            upo_page_list = []
            for upo_page_list_item_data in self.upo_page_list:
                upo_page_list_item = upo_page_list_item_data.to_dict()

                upo_page_list.append(upo_page_list_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "processingCode": processing_code,
            "processingDescription": processing_description,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
            "upoPageCount": upo_page_count,
        })
        if upo_page_list is not UNSET:
            field_dict["upoPageList"] = upo_page_list

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.upo_page_type import UpoPageType
        d = src_dict.copy()
        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        upo_page_count = d.pop("upoPageCount")

        upo_page_list = []
        _upo_page_list = d.pop("upoPageList", UNSET)
        for upo_page_list_item_data in (_upo_page_list or []):
            upo_page_list_item = UpoPageType.from_dict(upo_page_list_item_data)



            upo_page_list.append(upo_page_list_item)


        v4_status_response = cls(
            processing_code=processing_code,
            processing_description=processing_description,
            reference_number=reference_number,
            timestamp=timestamp,
            upo_page_count=upo_page_count,
            upo_page_list=upo_page_list,
        )

        v4_status_response.additional_properties = d
        return v4_status_response

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
