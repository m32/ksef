from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.person_subject_by_fingerprint_details_type import PersonSubjectByFingerprintDetailsType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.id_document import IdDocument
  from ..models.person_identifier import PersonIdentifier





T = TypeVar("T", bound="PermissionsSubjectPersonByFingerprintDetails")



@_attrs_define
class PermissionsSubjectPersonByFingerprintDetails:
    """ 
        Attributes:
            subject_details_type (PersonSubjectByFingerprintDetailsType): | Wartość | Opis |
                | --- | --- |
                | PersonByFingerprintWithIdentifier | Osoba fizyczna posługująca się certyfikatem niezawierającym identyfikatora
                NIP ani PESEL, ale mająca NIP lub PESEL. |
                | PersonByFingerprintWithoutIdentifier | Osoba fizyczna posługująca się certyfikatem niezawierającym
                identyfikatora NIP ani PESEL i niemająca NIP ani PESEL. |
            first_name (str): Imię osoby fizycznej.
            last_name (str): Nazwisko osoby fizycznej.
            person_identifier (Union['PersonIdentifier', None, Unset]): Identyfikator osoby fizycznej.
            birth_date (Union[None, Unset, datetime.date]): Data urodzenia osoby fizycznej.
            id_document (Union['IdDocument', None, Unset]): Dane dokumentu tożsamości osoby fizycznej.
     """

    subject_details_type: PersonSubjectByFingerprintDetailsType
    first_name: str
    last_name: str
    person_identifier: Union['PersonIdentifier', None, Unset] = UNSET
    birth_date: Union[None, Unset, datetime.date] = UNSET
    id_document: Union['IdDocument', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.id_document import IdDocument
        from ..models.person_identifier import PersonIdentifier
        subject_details_type = self.subject_details_type.value

        first_name = self.first_name

        last_name = self.last_name

        person_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.person_identifier, Unset):
            person_identifier = UNSET
        elif isinstance(self.person_identifier, PersonIdentifier):
            person_identifier = self.person_identifier.to_dict()
        else:
            person_identifier = self.person_identifier

        birth_date: Union[None, Unset, str]
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        elif isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        id_document: Union[None, Unset, dict[str, Any]]
        if isinstance(self.id_document, Unset):
            id_document = UNSET
        elif isinstance(self.id_document, IdDocument):
            id_document = self.id_document.to_dict()
        else:
            id_document = self.id_document


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectDetailsType": subject_details_type,
            "firstName": first_name,
            "lastName": last_name,
        })
        if person_identifier is not UNSET:
            field_dict["personIdentifier"] = person_identifier
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if id_document is not UNSET:
            field_dict["idDocument"] = id_document

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_document import IdDocument
        from ..models.person_identifier import PersonIdentifier
        d = dict(src_dict)
        subject_details_type = PersonSubjectByFingerprintDetailsType(d.pop("subjectDetailsType"))




        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        def _parse_person_identifier(data: object) -> Union['PersonIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_identifier_type_1 = PersonIdentifier.from_dict(data)



                return person_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonIdentifier', None, Unset], data)

        person_identifier = _parse_person_identifier(d.pop("personIdentifier", UNSET))


        def _parse_birth_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = isoparse(data).date()



                return birth_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        birth_date = _parse_birth_date(d.pop("birthDate", UNSET))


        def _parse_id_document(data: object) -> Union['IdDocument', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                id_document_type_1 = IdDocument.from_dict(data)



                return id_document_type_1
            except: # noqa: E722
                pass
            return cast(Union['IdDocument', None, Unset], data)

        id_document = _parse_id_document(d.pop("idDocument", UNSET))


        permissions_subject_person_by_fingerprint_details = cls(
            subject_details_type=subject_details_type,
            first_name=first_name,
            last_name=last_name,
            person_identifier=person_identifier,
            birth_date=birth_date,
            id_document=id_document,
        )

        return permissions_subject_person_by_fingerprint_details

