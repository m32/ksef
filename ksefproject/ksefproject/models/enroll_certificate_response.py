from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="EnrollCertificateResponse")



@_attrs_define
class EnrollCertificateResponse:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            timestamp (datetime.datetime): Data złożenia wniosku certyfikacyjnego.
     """

    reference_number: str
    timestamp: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        reference_number = self.reference_number

        timestamp = self.timestamp.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        enroll_certificate_response = cls(
            reference_number=reference_number,
            timestamp=timestamp,
        )

        return enroll_certificate_response

