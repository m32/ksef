from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ExportInvoicesResponse")



@_attrs_define
class ExportInvoicesResponse:
    """ 
        Attributes:
            operation_reference_number (str): Numer referencyjny operacji.
     """

    operation_reference_number: str





    def to_dict(self) -> dict[str, Any]:
        operation_reference_number = self.operation_reference_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "operationReferenceNumber": operation_reference_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_reference_number = d.pop("operationReferenceNumber")

        export_invoices_response = cls(
            operation_reference_number=operation_reference_number,
        )

        return export_invoices_response

