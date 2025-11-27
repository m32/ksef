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
            reference_number (str): Numer referencyjny.
     """

    reference_number: str





    def to_dict(self) -> dict[str, Any]:
        reference_number = self.reference_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        export_invoices_response = cls(
            reference_number=reference_number,
        )

        return export_invoices_response

