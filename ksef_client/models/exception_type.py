import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.exception_detail_type import ExceptionDetailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExceptionType")


@attr.s(auto_attribs=True)
class ExceptionType:
    """
    Attributes:
        service_ctx (str):
        service_code (str):
        service_name (str):
        timestamp (datetime.datetime):
        exception_detail_list (List[ExceptionDetailType]):
        reference_number (Union[Unset, str]):
    """

    service_ctx: str
    service_code: str
    service_name: str
    timestamp: datetime.datetime
    exception_detail_list: List[ExceptionDetailType]
    reference_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_ctx = self.service_ctx
        service_code = self.service_code
        service_name = self.service_name
        timestamp = self.timestamp.isoformat()

        exception_detail_list = []
        for exception_detail_list_item_data in self.exception_detail_list:
            exception_detail_list_item = exception_detail_list_item_data.to_dict()

            exception_detail_list.append(exception_detail_list_item)

        reference_number = self.reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceCtx": service_ctx,
                "serviceCode": service_code,
                "serviceName": service_name,
                "timestamp": timestamp,
                "exceptionDetailList": exception_detail_list,
            }
        )
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_ctx = d.pop("serviceCtx")

        service_code = d.pop("serviceCode")

        service_name = d.pop("serviceName")

        timestamp = isoparse(d.pop("timestamp"))

        exception_detail_list = []
        _exception_detail_list = d.pop("exceptionDetailList")
        for exception_detail_list_item_data in _exception_detail_list:
            exception_detail_list_item = ExceptionDetailType.from_dict(exception_detail_list_item_data)

            exception_detail_list.append(exception_detail_list_item)

        reference_number = d.pop("referenceNumber", UNSET)

        exception_type = cls(
            service_ctx=service_ctx,
            service_code=service_code,
            service_name=service_name,
            timestamp=timestamp,
            exception_detail_list=exception_detail_list,
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
