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
  from ..models.status_info import StatusInfo





T = TypeVar("T", bound="CertificateEnrollmentStatusResponse")



@_attrs_define
class CertificateEnrollmentStatusResponse:
    """ 
        Attributes:
            request_date (datetime.datetime): Data złożenia wniosku certyfikacyjnego.
            status (StatusInfo):
            certificate_serial_number (Union[None, Unset, str]): Numer seryjny wygenerowanego certyfikatu (w formacie
                szesnastkowym).
                Zwracany w przypadku prawidłowego przeprocesowania wniosku certyfikacyjnego.
     """

    request_date: datetime.datetime
    status: 'StatusInfo'
    certificate_serial_number: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_info import StatusInfo
        request_date = self.request_date.isoformat()

        status = self.status.to_dict()

        certificate_serial_number: Union[None, Unset, str]
        if isinstance(self.certificate_serial_number, Unset):
            certificate_serial_number = UNSET
        else:
            certificate_serial_number = self.certificate_serial_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "requestDate": request_date,
            "status": status,
        })
        if certificate_serial_number is not UNSET:
            field_dict["certificateSerialNumber"] = certificate_serial_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        request_date = isoparse(d.pop("requestDate"))




        status = StatusInfo.from_dict(d.pop("status"))




        def _parse_certificate_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        certificate_serial_number = _parse_certificate_serial_number(d.pop("certificateSerialNumber", UNSET))


        certificate_enrollment_status_response = cls(
            request_date=request_date,
            status=status,
            certificate_serial_number=certificate_serial_number,
        )

        return certificate_enrollment_status_response

