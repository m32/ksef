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
  from ..models.upo_response import UpoResponse
  from ..models.status_info import StatusInfo





T = TypeVar("T", bound="SessionStatusResponse")



@_attrs_define
class SessionStatusResponse:
    """ 
        Attributes:
            status (StatusInfo):
            valid_until (Union[None, Unset, datetime.datetime]): Termin ważności sesji. Po jego upływie sesja zostanie
                automatycznie zamknięta.
            upo (Union['UpoResponse', None, Unset]): Informacja o UPO sesyjnym, zwracana gdy sesja została zamknięta i UPO
                zostało wygenerowane.
            invoice_count (Union[None, Unset, int]): Liczba przyjętych faktur w ramach sesji.
            successful_invoice_count (Union[None, Unset, int]): Liczba faktur przeprocesowanych w ramach sesji z sukcesem .
            failed_invoice_count (Union[None, Unset, int]): Liczba faktur przeprocesowanych w ramach sesji z błędem.
     """

    status: 'StatusInfo'
    valid_until: Union[None, Unset, datetime.datetime] = UNSET
    upo: Union['UpoResponse', None, Unset] = UNSET
    invoice_count: Union[None, Unset, int] = UNSET
    successful_invoice_count: Union[None, Unset, int] = UNSET
    failed_invoice_count: Union[None, Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.upo_response import UpoResponse
        from ..models.status_info import StatusInfo
        status = self.status.to_dict()

        valid_until: Union[None, Unset, str]
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        upo: Union[None, Unset, dict[str, Any]]
        if isinstance(self.upo, Unset):
            upo = UNSET
        elif isinstance(self.upo, UpoResponse):
            upo = self.upo.to_dict()
        else:
            upo = self.upo

        invoice_count: Union[None, Unset, int]
        if isinstance(self.invoice_count, Unset):
            invoice_count = UNSET
        else:
            invoice_count = self.invoice_count

        successful_invoice_count: Union[None, Unset, int]
        if isinstance(self.successful_invoice_count, Unset):
            successful_invoice_count = UNSET
        else:
            successful_invoice_count = self.successful_invoice_count

        failed_invoice_count: Union[None, Unset, int]
        if isinstance(self.failed_invoice_count, Unset):
            failed_invoice_count = UNSET
        else:
            failed_invoice_count = self.failed_invoice_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if upo is not UNSET:
            field_dict["upo"] = upo
        if invoice_count is not UNSET:
            field_dict["invoiceCount"] = invoice_count
        if successful_invoice_count is not UNSET:
            field_dict["successfulInvoiceCount"] = successful_invoice_count
        if failed_invoice_count is not UNSET:
            field_dict["failedInvoiceCount"] = failed_invoice_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upo_response import UpoResponse
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        status = StatusInfo.from_dict(d.pop("status"))




        def _parse_valid_until(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = isoparse(data)



                return valid_until_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        valid_until = _parse_valid_until(d.pop("validUntil", UNSET))


        def _parse_upo(data: object) -> Union['UpoResponse', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upo_type_1 = UpoResponse.from_dict(data)



                return upo_type_1
            except: # noqa: E722
                pass
            return cast(Union['UpoResponse', None, Unset], data)

        upo = _parse_upo(d.pop("upo", UNSET))


        def _parse_invoice_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        invoice_count = _parse_invoice_count(d.pop("invoiceCount", UNSET))


        def _parse_successful_invoice_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        successful_invoice_count = _parse_successful_invoice_count(d.pop("successfulInvoiceCount", UNSET))


        def _parse_failed_invoice_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        failed_invoice_count = _parse_failed_invoice_count(d.pop("failedInvoiceCount", UNSET))


        session_status_response = cls(
            status=status,
            valid_until=valid_until,
            upo=upo,
            invoice_count=invoice_count,
            successful_invoice_count=successful_invoice_count,
            failed_invoice_count=failed_invoice_count,
        )

        return session_status_response

