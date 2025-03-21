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
  from ..models.exception_detail_type import ExceptionDetailType





T = TypeVar("T", bound="ExceptionType")


@_attrs_define
class ExceptionType:
    """ 
        Attributes:
            exception_detail_list (List['ExceptionDetailType']):
            service_code (str):
            service_ctx (str):
            service_name (str):
            timestamp (datetime.datetime):
            reference_number (Union[Unset, str]):
     """

    exception_detail_list: List['ExceptionDetailType']
    service_code: str
    service_ctx: str
    service_name: str
    timestamp: datetime.datetime
    reference_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.exception_detail_type import ExceptionDetailType
        exception_detail_list = []
        for exception_detail_list_item_data in self.exception_detail_list:
            exception_detail_list_item = exception_detail_list_item_data.to_dict()

            exception_detail_list.append(exception_detail_list_item)




        service_code = self.service_code
        service_ctx = self.service_ctx
        service_name = self.service_name
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exceptionDetailList": exception_detail_list,
            "serviceCode": service_code,
            "serviceCtx": service_ctx,
            "serviceName": service_name,
            "timestamp": timestamp,
        })
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exception_detail_type import ExceptionDetailType
        d = src_dict.copy()
        exception_detail_list = []
        _exception_detail_list = d.pop("exceptionDetailList")
        for exception_detail_list_item_data in (_exception_detail_list):
            exception_detail_list_item = ExceptionDetailType.from_dict(exception_detail_list_item_data)



            exception_detail_list.append(exception_detail_list_item)


        service_code = d.pop("serviceCode")

        service_ctx = d.pop("serviceCtx")

        service_name = d.pop("serviceName")

        timestamp = isoparse(d.pop("timestamp"))




        reference_number = d.pop("referenceNumber", UNSET)

        exception_type = cls(
            exception_detail_list=exception_detail_list,
            service_code=service_code,
            service_ctx=service_ctx,
            service_name=service_name,
            timestamp=timestamp,
            reference_number=reference_number,
        )

        exception_type.additional_properties = d
        return exception_type

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
