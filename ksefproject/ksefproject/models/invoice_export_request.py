from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.encryption_info import EncryptionInfo
  from ..models.invoice_query_filters import InvoiceQueryFilters





T = TypeVar("T", bound="InvoiceExportRequest")



@_attrs_define
class InvoiceExportRequest:
    """ 
        Attributes:
            encryption (EncryptionInfo):
            filters (InvoiceQueryFilters):
     """

    encryption: 'EncryptionInfo'
    filters: 'InvoiceQueryFilters'





    def to_dict(self) -> dict[str, Any]:
        from ..models.encryption_info import EncryptionInfo
        from ..models.invoice_query_filters import InvoiceQueryFilters
        encryption = self.encryption.to_dict()

        filters = self.filters.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "encryption": encryption,
            "filters": filters,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encryption_info import EncryptionInfo
        from ..models.invoice_query_filters import InvoiceQueryFilters
        d = dict(src_dict)
        encryption = EncryptionInfo.from_dict(d.pop("encryption"))




        filters = InvoiceQueryFilters.from_dict(d.pop("filters"))




        invoice_export_request = cls(
            encryption=encryption,
            filters=filters,
        )

        return invoice_export_request

