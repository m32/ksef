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





T = TypeVar("T", bound="SessionsQueryResponseItem")



@_attrs_define
class SessionsQueryResponseItem:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            status (StatusInfo):
            date_created (datetime.datetime): Data utworzenia sesji.
            date_updated (datetime.datetime): Data ostatniej aktywności w ramach sesji.
            total_invoice_count (int): Łączna liczba faktur (uwzględnia również te w trakcie przetwarzania).
            successful_invoice_count (int): Liczba poprawnie przetworzonych faktur.
            failed_invoice_count (int): Liczba błędnie przetworzonych faktur.
            valid_until (Union[None, Unset, datetime.datetime]): Termin ważności sesji. Po jego upływie sesja interaktywna
                zostanie automatycznie zamknięta.
     """

    reference_number: str
    status: 'StatusInfo'
    date_created: datetime.datetime
    date_updated: datetime.datetime
    total_invoice_count: int
    successful_invoice_count: int
    failed_invoice_count: int
    valid_until: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_info import StatusInfo
        reference_number = self.reference_number

        status = self.status.to_dict()

        date_created = self.date_created.isoformat()

        date_updated = self.date_updated.isoformat()

        total_invoice_count = self.total_invoice_count

        successful_invoice_count = self.successful_invoice_count

        failed_invoice_count = self.failed_invoice_count

        valid_until: Union[None, Unset, str]
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "status": status,
            "dateCreated": date_created,
            "dateUpdated": date_updated,
            "totalInvoiceCount": total_invoice_count,
            "successfulInvoiceCount": successful_invoice_count,
            "failedInvoiceCount": failed_invoice_count,
        })
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        status = StatusInfo.from_dict(d.pop("status"))




        date_created = isoparse(d.pop("dateCreated"))




        date_updated = isoparse(d.pop("dateUpdated"))




        total_invoice_count = d.pop("totalInvoiceCount")

        successful_invoice_count = d.pop("successfulInvoiceCount")

        failed_invoice_count = d.pop("failedInvoiceCount")

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


        sessions_query_response_item = cls(
            reference_number=reference_number,
            status=status,
            date_created=date_created,
            date_updated=date_updated,
            total_invoice_count=total_invoice_count,
            successful_invoice_count=successful_invoice_count,
            failed_invoice_count=failed_invoice_count,
            valid_until=valid_until,
        )

        return sessions_query_response_item

