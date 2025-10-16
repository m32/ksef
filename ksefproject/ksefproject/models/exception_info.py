from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.exception_details import ExceptionDetails





T = TypeVar("T", bound="ExceptionInfo")



@_attrs_define
class ExceptionInfo:
    """ 
        Attributes:
            exception_detail_list (Union[None, Unset, list['ExceptionDetails']]):
            reference_number (Union[None, Unset, str]):
            service_code (Union[None, Unset, str]):
            service_ctx (Union[None, Unset, str]):
            service_name (Union[None, Unset, str]):
            timestamp (Union[Unset, datetime.datetime]):
     """

    exception_detail_list: Union[None, Unset, list['ExceptionDetails']] = UNSET
    reference_number: Union[None, Unset, str] = UNSET
    service_code: Union[None, Unset, str] = UNSET
    service_ctx: Union[None, Unset, str] = UNSET
    service_name: Union[None, Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.exception_details import ExceptionDetails
        exception_detail_list: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.exception_detail_list, Unset):
            exception_detail_list = UNSET
        elif isinstance(self.exception_detail_list, list):
            exception_detail_list = []
            for exception_detail_list_type_0_item_data in self.exception_detail_list:
                exception_detail_list_type_0_item = exception_detail_list_type_0_item_data.to_dict()
                exception_detail_list.append(exception_detail_list_type_0_item)


        else:
            exception_detail_list = self.exception_detail_list

        reference_number: Union[None, Unset, str]
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        service_code: Union[None, Unset, str]
        if isinstance(self.service_code, Unset):
            service_code = UNSET
        else:
            service_code = self.service_code

        service_ctx: Union[None, Unset, str]
        if isinstance(self.service_ctx, Unset):
            service_ctx = UNSET
        else:
            service_ctx = self.service_ctx

        service_name: Union[None, Unset, str]
        if isinstance(self.service_name, Unset):
            service_name = UNSET
        else:
            service_name = self.service_name

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if exception_detail_list is not UNSET:
            field_dict["exceptionDetailList"] = exception_detail_list
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if service_code is not UNSET:
            field_dict["serviceCode"] = service_code
        if service_ctx is not UNSET:
            field_dict["serviceCtx"] = service_ctx
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exception_details import ExceptionDetails
        d = dict(src_dict)
        def _parse_exception_detail_list(data: object) -> Union[None, Unset, list['ExceptionDetails']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exception_detail_list_type_0 = []
                _exception_detail_list_type_0 = data
                for exception_detail_list_type_0_item_data in (_exception_detail_list_type_0):
                    exception_detail_list_type_0_item = ExceptionDetails.from_dict(exception_detail_list_type_0_item_data)



                    exception_detail_list_type_0.append(exception_detail_list_type_0_item)

                return exception_detail_list_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['ExceptionDetails']], data)

        exception_detail_list = _parse_exception_detail_list(d.pop("exceptionDetailList", UNSET))


        def _parse_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_number = _parse_reference_number(d.pop("referenceNumber", UNSET))


        def _parse_service_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_code = _parse_service_code(d.pop("serviceCode", UNSET))


        def _parse_service_ctx(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_ctx = _parse_service_ctx(d.pop("serviceCtx", UNSET))


        def _parse_service_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_name = _parse_service_name(d.pop("serviceName", UNSET))


        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        exception_info = cls(
            exception_detail_list=exception_detail_list,
            reference_number=reference_number,
            service_code=service_code,
            service_ctx=service_ctx,
            service_name=service_name,
            timestamp=timestamp,
        )

        return exception_info

