from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Union
from dateutil.parser import isoparse
from io import BytesIO
import datetime
from ..types import File, FileJsonType
from ..types import UNSET, Unset






T = TypeVar("T", bound="StatusResponse")


@_attrs_define
class StatusResponse:
    """ 
        Attributes:
            processing_code (int):
            processing_description (str):
            reference_number (str):
            timestamp (datetime.datetime):
            upo (Union[Unset, File]):
     """

    processing_code: int
    processing_description: str
    reference_number: str
    timestamp: datetime.datetime
    upo: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        processing_code = self.processing_code
        processing_description = self.processing_description
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()

        upo: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.upo, Unset):
            upo = self.upo.to_tuple()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "processingCode": processing_code,
            "processingDescription": processing_description,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })
        if upo is not UNSET:
            field_dict["upo"] = upo

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        _upo = d.pop("upo", UNSET)
        upo: Union[Unset, File]
        if isinstance(_upo,  Unset):
            upo = UNSET
        else:
            upo = File(
             payload = BytesIO(_upo.encode())
        )




        status_response = cls(
            processing_code=processing_code,
            processing_description=processing_description,
            reference_number=reference_number,
            timestamp=timestamp,
            upo=upo,
        )

        status_response.additional_properties = d
        return status_response

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
