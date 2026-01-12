from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IdDocument")



@_attrs_define
class IdDocument:
    """ Dane dokumentu tożsamości osoby fizycznej.

        Attributes:
            type_ (str): Rodzaj dokumentu tożsamości.
            number (str): Seria i numer dokumentu tożsamości.
            country (str): Kraj wydania dokumentu tożsamości. Musi być zgodny z ISO 3166-1 alpha-2 (np. PL, DE, US) oraz
                zawierać dokładnie 2 wielkie litery.
     """

    type_: str
    number: str
    country: str





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        number = self.number

        country = self.country


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "number": number,
            "country": country,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        number = d.pop("number")

        country = d.pop("country")

        id_document = cls(
            type_=type_,
            number=number,
            country=country,
        )

        return id_document

