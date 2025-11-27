from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PeppolProvider")



@_attrs_define
class PeppolProvider:
    """ 
        Attributes:
            id (str): Identyfikator dostawcy usług Peppol.
            name (str): Nazwa dostawcy usług Peppol.
            date_created (datetime.datetime): Data rejestracji dostawcy usług Peppol w systemie.
     """

    id: str
    name: str
    date_created: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        date_created = self.date_created.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "dateCreated": date_created,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        date_created = isoparse(d.pop("dateCreated"))




        peppol_provider = cls(
            id=id,
            name=name,
            date_created=date_created,
        )

        return peppol_provider

