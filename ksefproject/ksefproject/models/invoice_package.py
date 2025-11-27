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
  from ..models.invoice_package_part import InvoicePackagePart





T = TypeVar("T", bound="InvoicePackage")



@_attrs_define
class InvoicePackage:
    """ 
        Attributes:
            invoice_count (int): Łączna liczba faktur w paczce.
            size (int): Rozmiar paczki w bajtach.
            parts (list['InvoicePackagePart']): Lista dostępnych części paczki do pobrania.
            is_truncated (bool): Określa, czy wynik eksportu został ucięty z powodu przekroczenia limitu liczby faktur lub
                wielkości paczki.
            last_issue_date (Union[None, Unset, datetime.date]): Data wystawienia ostatniej faktury ujętej w paczce.
                Pole występuje wyłącznie wtedy, gdy paczka została ucięta i eksport był filtrowany po typie daty `Issue`.
            last_invoicing_date (Union[None, Unset, datetime.datetime]): Data przyjęcia ostatniej faktury ujętej w paczce.
                Pole występuje wyłącznie wtedy, gdy paczka została ucięta i eksport był filtrowany po typie daty `Invoicing`.
            last_permanent_storage_date (Union[None, Unset, datetime.datetime]): Data trwałego zapisu ostatniej faktury
                ujętej w paczce.
                Pole występuje wyłącznie wtedy, gdy paczka została ucięta i eksport był filtrowany po typie daty
                `PermanentStorage`.
     """

    invoice_count: int
    size: int
    parts: list['InvoicePackagePart']
    is_truncated: bool
    last_issue_date: Union[None, Unset, datetime.date] = UNSET
    last_invoicing_date: Union[None, Unset, datetime.datetime] = UNSET
    last_permanent_storage_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_package_part import InvoicePackagePart
        invoice_count = self.invoice_count

        size = self.size

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)



        is_truncated = self.is_truncated

        last_issue_date: Union[None, Unset, str]
        if isinstance(self.last_issue_date, Unset):
            last_issue_date = UNSET
        elif isinstance(self.last_issue_date, datetime.date):
            last_issue_date = self.last_issue_date.isoformat()
        else:
            last_issue_date = self.last_issue_date

        last_invoicing_date: Union[None, Unset, str]
        if isinstance(self.last_invoicing_date, Unset):
            last_invoicing_date = UNSET
        elif isinstance(self.last_invoicing_date, datetime.datetime):
            last_invoicing_date = self.last_invoicing_date.isoformat()
        else:
            last_invoicing_date = self.last_invoicing_date

        last_permanent_storage_date: Union[None, Unset, str]
        if isinstance(self.last_permanent_storage_date, Unset):
            last_permanent_storage_date = UNSET
        elif isinstance(self.last_permanent_storage_date, datetime.datetime):
            last_permanent_storage_date = self.last_permanent_storage_date.isoformat()
        else:
            last_permanent_storage_date = self.last_permanent_storage_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "invoiceCount": invoice_count,
            "size": size,
            "parts": parts,
            "isTruncated": is_truncated,
        })
        if last_issue_date is not UNSET:
            field_dict["lastIssueDate"] = last_issue_date
        if last_invoicing_date is not UNSET:
            field_dict["lastInvoicingDate"] = last_invoicing_date
        if last_permanent_storage_date is not UNSET:
            field_dict["lastPermanentStorageDate"] = last_permanent_storage_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_package_part import InvoicePackagePart
        d = dict(src_dict)
        invoice_count = d.pop("invoiceCount")

        size = d.pop("size")

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in (_parts):
            parts_item = InvoicePackagePart.from_dict(parts_item_data)



            parts.append(parts_item)


        is_truncated = d.pop("isTruncated")

        def _parse_last_issue_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_issue_date_type_0 = isoparse(data).date()



                return last_issue_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        last_issue_date = _parse_last_issue_date(d.pop("lastIssueDate", UNSET))


        def _parse_last_invoicing_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_invoicing_date_type_0 = isoparse(data)



                return last_invoicing_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_invoicing_date = _parse_last_invoicing_date(d.pop("lastInvoicingDate", UNSET))


        def _parse_last_permanent_storage_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_permanent_storage_date_type_0 = isoparse(data)



                return last_permanent_storage_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_permanent_storage_date = _parse_last_permanent_storage_date(d.pop("lastPermanentStorageDate", UNSET))


        invoice_package = cls(
            invoice_count=invoice_count,
            size=size,
            parts=parts,
            is_truncated=is_truncated,
            last_issue_date=last_issue_date,
            last_invoicing_date=last_invoicing_date,
            last_permanent_storage_date=last_permanent_storage_date,
        )

        return invoice_package

