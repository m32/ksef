from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="OpenOnlineSessionResponse")



@_attrs_define
class OpenOnlineSessionResponse:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            valid_until (datetime.datetime): Termin ważności sesji. Po jego upływie sesja zostanie automatycznie zamknięta.
     """

    reference_number: str
    valid_until: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        reference_number = self.reference_number

        valid_until = self.valid_until.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "validUntil": valid_until,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        valid_until = isoparse(d.pop("validUntil"))




        open_online_session_response = cls(
            reference_number=reference_number,
            valid_until=valid_until,
        )

        return open_online_session_response

