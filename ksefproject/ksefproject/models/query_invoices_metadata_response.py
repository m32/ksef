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
  from ..models.invoice_metadata import InvoiceMetadata





T = TypeVar("T", bound="QueryInvoicesMetadataResponse")



@_attrs_define
class QueryInvoicesMetadataResponse:
    """ 
        Attributes:
            has_more (bool): Określa, czy istnieją kolejne wyniki zapytania.
            is_truncated (bool): Określa, czy osiągnięto maksymalny dopuszczalny zakres wyników zapytania (10 000).
            invoices (list['InvoiceMetadata']): Lista faktur spełniających kryteria.
            permanent_storage_hwm_date (Union[None, Unset, datetime.datetime]): Dotyczy wyłącznie zapytań filtrowanych po
                typie daty <b>PermanentStorage</b>.
                Jeśli zapytanie dotyczyło najnowszego okresu, wartość ta może być wartością nieznacznie skorygowaną względem
                górnej granicy podanej w warunkach zapytania.
                Dla okresów starszych, będzie to zgodne z warunkami zapytania.

                Wartość jest stała dla wszystkich stron tego samego zapytania
                i nie zależy od paginacji ani sortowania.

                System gwarantuje, że dane poniżej tej wartości są spójne i kompletne.
                Ponowne zapytania obejmujące zakresem dane poniżej tego kroczącego znacznika czasu nie zwrócą w przyszłości
                innych wyników (np.dodatkowych faktur).

                Dla dateType = Issue lub Invoicing – null.
     """

    has_more: bool
    is_truncated: bool
    invoices: list['InvoiceMetadata']
    permanent_storage_hwm_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_metadata import InvoiceMetadata
        has_more = self.has_more

        is_truncated = self.is_truncated

        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)



        permanent_storage_hwm_date: Union[None, Unset, str]
        if isinstance(self.permanent_storage_hwm_date, Unset):
            permanent_storage_hwm_date = UNSET
        elif isinstance(self.permanent_storage_hwm_date, datetime.datetime):
            permanent_storage_hwm_date = self.permanent_storage_hwm_date.isoformat()
        else:
            permanent_storage_hwm_date = self.permanent_storage_hwm_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hasMore": has_more,
            "isTruncated": is_truncated,
            "invoices": invoices,
        })
        if permanent_storage_hwm_date is not UNSET:
            field_dict["permanentStorageHwmDate"] = permanent_storage_hwm_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_metadata import InvoiceMetadata
        d = dict(src_dict)
        has_more = d.pop("hasMore")

        is_truncated = d.pop("isTruncated")

        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in (_invoices):
            invoices_item = InvoiceMetadata.from_dict(invoices_item_data)



            invoices.append(invoices_item)


        def _parse_permanent_storage_hwm_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                permanent_storage_hwm_date_type_0 = isoparse(data)



                return permanent_storage_hwm_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        permanent_storage_hwm_date = _parse_permanent_storage_hwm_date(d.pop("permanentStorageHwmDate", UNSET))


        query_invoices_metadata_response = cls(
            has_more=has_more,
            is_truncated=is_truncated,
            invoices=invoices,
            permanent_storage_hwm_date=permanent_storage_hwm_date,
        )

        return query_invoices_metadata_response

