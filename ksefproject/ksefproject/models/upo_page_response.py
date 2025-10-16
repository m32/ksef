from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpoPageResponse")



@_attrs_define
class UpoPageResponse:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny strony UPO.
            download_url (str): Adres do pobrania strony UPO.
     """

    reference_number: str
    download_url: str





    def to_dict(self) -> dict[str, Any]:
        reference_number = self.reference_number

        download_url = self.download_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "downloadUrl": download_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        download_url = d.pop("downloadUrl")

        upo_page_response = cls(
            reference_number=reference_number,
            download_url=download_url,
        )

        return upo_page_response

