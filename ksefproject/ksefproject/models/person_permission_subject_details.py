from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.person_permission_subject_details_type import PersonPermissionSubjectDetailsType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.person_by_fingerprint_with_identifier_details import PersonByFingerprintWithIdentifierDetails
  from ..models.person_details import PersonDetails
  from ..models.person_by_fingerprint_without_identifier_details import PersonByFingerprintWithoutIdentifierDetails





T = TypeVar("T", bound="PersonPermissionSubjectDetails")



@_attrs_define
class PersonPermissionSubjectDetails:
    """ 
        Attributes:
            subject_details_type (PersonPermissionSubjectDetailsType): | Wartość | Opis |
                | --- | --- |
                | PersonByIdentifier | Osoba fizyczna posługująca się Profilem Zaufanym lub certyfikatem zawierającym
                identyfikator NIP lub PESEL. |
                | PersonByFingerprintWithIdentifier | Osoba fizyczna posługująca się certyfikatem niezawierającym identyfikatora
                NIP ani PESEL, ale mająca NIP lub PESEL. |
                | PersonByFingerprintWithoutIdentifier | Osoba fizyczna posługująca się certyfikatem niezawierającym
                identyfikatora NIP ani PESEL i niemająca NIP ani PESEL. |
            person_by_id (Union['PersonDetails', None, Unset]): Dane podmiotu.
                *Wymagane, gdy subjectDetailsType = PersonByIdentifier.*
            person_by_fp_with_id (Union['PersonByFingerprintWithIdentifierDetails', None, Unset]): Dane podmiotu.
                *Wymagane, gdy subjectDetailsType = PersonByFingerprintWithIdentifier.*
            person_by_fp_no_id (Union['PersonByFingerprintWithoutIdentifierDetails', None, Unset]): Dane podmiotu.
                *Wymagane, gdy subjectDetailsType = PersonByFingerprintWithoutIdentifier.*
     """

    subject_details_type: PersonPermissionSubjectDetailsType
    person_by_id: Union['PersonDetails', None, Unset] = UNSET
    person_by_fp_with_id: Union['PersonByFingerprintWithIdentifierDetails', None, Unset] = UNSET
    person_by_fp_no_id: Union['PersonByFingerprintWithoutIdentifierDetails', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_by_fingerprint_with_identifier_details import PersonByFingerprintWithIdentifierDetails
        from ..models.person_details import PersonDetails
        from ..models.person_by_fingerprint_without_identifier_details import PersonByFingerprintWithoutIdentifierDetails
        subject_details_type = self.subject_details_type.value

        person_by_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.person_by_id, Unset):
            person_by_id = UNSET
        elif isinstance(self.person_by_id, PersonDetails):
            person_by_id = self.person_by_id.to_dict()
        else:
            person_by_id = self.person_by_id

        person_by_fp_with_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.person_by_fp_with_id, Unset):
            person_by_fp_with_id = UNSET
        elif isinstance(self.person_by_fp_with_id, PersonByFingerprintWithIdentifierDetails):
            person_by_fp_with_id = self.person_by_fp_with_id.to_dict()
        else:
            person_by_fp_with_id = self.person_by_fp_with_id

        person_by_fp_no_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.person_by_fp_no_id, Unset):
            person_by_fp_no_id = UNSET
        elif isinstance(self.person_by_fp_no_id, PersonByFingerprintWithoutIdentifierDetails):
            person_by_fp_no_id = self.person_by_fp_no_id.to_dict()
        else:
            person_by_fp_no_id = self.person_by_fp_no_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectDetailsType": subject_details_type,
        })
        if person_by_id is not UNSET:
            field_dict["personById"] = person_by_id
        if person_by_fp_with_id is not UNSET:
            field_dict["personByFpWithId"] = person_by_fp_with_id
        if person_by_fp_no_id is not UNSET:
            field_dict["personByFpNoId"] = person_by_fp_no_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_by_fingerprint_with_identifier_details import PersonByFingerprintWithIdentifierDetails
        from ..models.person_details import PersonDetails
        from ..models.person_by_fingerprint_without_identifier_details import PersonByFingerprintWithoutIdentifierDetails
        d = dict(src_dict)
        subject_details_type = PersonPermissionSubjectDetailsType(d.pop("subjectDetailsType"))




        def _parse_person_by_id(data: object) -> Union['PersonDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_by_id_type_1 = PersonDetails.from_dict(data)



                return person_by_id_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonDetails', None, Unset], data)

        person_by_id = _parse_person_by_id(d.pop("personById", UNSET))


        def _parse_person_by_fp_with_id(data: object) -> Union['PersonByFingerprintWithIdentifierDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_by_fp_with_id_type_1 = PersonByFingerprintWithIdentifierDetails.from_dict(data)



                return person_by_fp_with_id_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonByFingerprintWithIdentifierDetails', None, Unset], data)

        person_by_fp_with_id = _parse_person_by_fp_with_id(d.pop("personByFpWithId", UNSET))


        def _parse_person_by_fp_no_id(data: object) -> Union['PersonByFingerprintWithoutIdentifierDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_by_fp_no_id_type_1 = PersonByFingerprintWithoutIdentifierDetails.from_dict(data)



                return person_by_fp_no_id_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonByFingerprintWithoutIdentifierDetails', None, Unset], data)

        person_by_fp_no_id = _parse_person_by_fp_no_id(d.pop("personByFpNoId", UNSET))


        person_permission_subject_details = cls(
            subject_details_type=subject_details_type,
            person_by_id=person_by_id,
            person_by_fp_with_id=person_by_fp_with_id,
            person_by_fp_no_id=person_by_fp_no_id,
        )

        return person_permission_subject_details

