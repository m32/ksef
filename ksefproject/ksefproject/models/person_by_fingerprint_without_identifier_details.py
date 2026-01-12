from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.id_document import IdDocument





T = TypeVar("T", bound="PersonByFingerprintWithoutIdentifierDetails")



@_attrs_define
class PersonByFingerprintWithoutIdentifierDetails:
    """ 
        Attributes:
            first_name (str): Imię osoby fizycznej.
            last_name (str): Nazwisko osoby fizycznej.
            birth_date (datetime.date): Data urodzenia osoby fizycznej.
            id_document (IdDocument): Dane dokumentu tożsamości osoby fizycznej.
     """

    first_name: str
    last_name: str
    birth_date: datetime.date
    id_document: 'IdDocument'





    def to_dict(self) -> dict[str, Any]:
        from ..models.id_document import IdDocument
        first_name = self.first_name

        last_name = self.last_name

        birth_date = self.birth_date.isoformat()

        id_document = self.id_document.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "firstName": first_name,
            "lastName": last_name,
            "birthDate": birth_date,
            "idDocument": id_document,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_document import IdDocument
        d = dict(src_dict)
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        birth_date = isoparse(d.pop("birthDate")).date()




        id_document = IdDocument.from_dict(d.pop("idDocument"))




        person_by_fingerprint_without_identifier_details = cls(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            id_document=id_document,
        )

        return person_by_fingerprint_without_identifier_details

