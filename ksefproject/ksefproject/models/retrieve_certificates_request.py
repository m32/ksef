from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RetrieveCertificatesRequest")



@_attrs_define
class RetrieveCertificatesRequest:
    """ 
        Attributes:
            certificate_serial_numbers (list[str]): Numery seryjne certyfikatów do pobrania.
     """

    certificate_serial_numbers: list[str]





    def to_dict(self) -> dict[str, Any]:
        certificate_serial_numbers = self.certificate_serial_numbers




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificateSerialNumbers": certificate_serial_numbers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_serial_numbers = cast(list[str], d.pop("certificateSerialNumbers"))


        retrieve_certificates_request = cls(
            certificate_serial_numbers=certificate_serial_numbers,
        )

        return retrieve_certificates_request

