from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

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
     """

    has_more: bool
    is_truncated: bool
    invoices: list['InvoiceMetadata']





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_metadata import InvoiceMetadata
        has_more = self.has_more

        is_truncated = self.is_truncated

        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hasMore": has_more,
            "isTruncated": is_truncated,
            "invoices": invoices,
        })

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


        query_invoices_metadata_response = cls(
            has_more=has_more,
            is_truncated=is_truncated,
            invoices=invoices,
        )

        return query_invoices_metadata_response

