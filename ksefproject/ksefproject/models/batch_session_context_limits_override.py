from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BatchSessionContextLimitsOverride")



@_attrs_define
class BatchSessionContextLimitsOverride:
    """ 
        Attributes:
            max_invoice_size_in_mb (int): Maksymalny rozmiar faktury w MB.
            max_invoice_with_attachment_size_in_mb (int): Maksymalny rozmiar faktury z załącznikiem w MB.
            max_invoices (int): Maksymalna ilość faktur które można przesłać w pojedynczej sesji.
     """

    max_invoice_size_in_mb: int
    max_invoice_with_attachment_size_in_mb: int
    max_invoices: int





    def to_dict(self) -> dict[str, Any]:
        max_invoice_size_in_mb = self.max_invoice_size_in_mb

        max_invoice_with_attachment_size_in_mb = self.max_invoice_with_attachment_size_in_mb

        max_invoices = self.max_invoices


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "maxInvoiceSizeInMB": max_invoice_size_in_mb,
            "maxInvoiceWithAttachmentSizeInMB": max_invoice_with_attachment_size_in_mb,
            "maxInvoices": max_invoices,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_invoice_size_in_mb = d.pop("maxInvoiceSizeInMB")

        max_invoice_with_attachment_size_in_mb = d.pop("maxInvoiceWithAttachmentSizeInMB")

        max_invoices = d.pop("maxInvoices")

        batch_session_context_limits_override = cls(
            max_invoice_size_in_mb=max_invoice_size_in_mb,
            max_invoice_with_attachment_size_in_mb=max_invoice_with_attachment_size_in_mb,
            max_invoices=max_invoices,
        )

        return batch_session_context_limits_override

