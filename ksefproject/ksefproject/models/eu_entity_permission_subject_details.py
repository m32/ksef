from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eu_entity_permission_subject_details_type import EuEntityPermissionSubjectDetailsType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.person_by_fingerprint_with_identifier_details import PersonByFingerprintWithIdentifierDetails
  from ..models.person_by_fingerprint_without_identifier_details import PersonByFingerprintWithoutIdentifierDetails
  from ..models.entity_by_fingerprint_details import EntityByFingerprintDetails





T = TypeVar("T", bound="EuEntityPermissionSubjectDetails")



@_attrs_define
class EuEntityPermissionSubjectDetails:
    """ 
        Attributes:
            subject_details_type (EuEntityPermissionSubjectDetailsType): | Wartość | Opis |
                | --- | --- |
                | PersonByFingerprintWithIdentifier | Osoba fizyczna posługująca się certyfikatem niezawierającym identyfikatora
                NIP ani PESEL, ale mająca NIP lub PESEL. |
                | PersonByFingerprintWithoutIdentifier | Osoba fizyczna posługująca się certyfikatem niezawierającym
                identyfikatora NIP ani PESEL i niemająca NIP ani PESEL. |
                | EntityByFingerprint | Podmiot identyfikowany odciskiem palca pieczęci kwalifikowanej. |
            person_by_fp_with_id (Union['PersonByFingerprintWithIdentifierDetails', None, Unset]): Dane podmiotu.
                *Wymagane, gdy subjectDetailsType = PersonByFingerprintWithIdentifier.*
            person_by_fp_no_id (Union['PersonByFingerprintWithoutIdentifierDetails', None, Unset]): Dane podmiotu.
                *Wymagane, gdy subjectDetailsType = PersonByFingerprintWithoutIdentifier.*
            entity_by_fp (Union['EntityByFingerprintDetails', None, Unset]): Dane podmiotu.
                *Wymagane, gdy subjectDetailsType = EntityByFingerprint.*
     """

    subject_details_type: EuEntityPermissionSubjectDetailsType
    person_by_fp_with_id: Union['PersonByFingerprintWithIdentifierDetails', None, Unset] = UNSET
    person_by_fp_no_id: Union['PersonByFingerprintWithoutIdentifierDetails', None, Unset] = UNSET
    entity_by_fp: Union['EntityByFingerprintDetails', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_by_fingerprint_with_identifier_details import PersonByFingerprintWithIdentifierDetails
        from ..models.person_by_fingerprint_without_identifier_details import PersonByFingerprintWithoutIdentifierDetails
        from ..models.entity_by_fingerprint_details import EntityByFingerprintDetails
        subject_details_type = self.subject_details_type.value

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

        entity_by_fp: Union[None, Unset, dict[str, Any]]
        if isinstance(self.entity_by_fp, Unset):
            entity_by_fp = UNSET
        elif isinstance(self.entity_by_fp, EntityByFingerprintDetails):
            entity_by_fp = self.entity_by_fp.to_dict()
        else:
            entity_by_fp = self.entity_by_fp


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectDetailsType": subject_details_type,
        })
        if person_by_fp_with_id is not UNSET:
            field_dict["personByFpWithId"] = person_by_fp_with_id
        if person_by_fp_no_id is not UNSET:
            field_dict["personByFpNoId"] = person_by_fp_no_id
        if entity_by_fp is not UNSET:
            field_dict["entityByFp"] = entity_by_fp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_by_fingerprint_with_identifier_details import PersonByFingerprintWithIdentifierDetails
        from ..models.person_by_fingerprint_without_identifier_details import PersonByFingerprintWithoutIdentifierDetails
        from ..models.entity_by_fingerprint_details import EntityByFingerprintDetails
        d = dict(src_dict)
        subject_details_type = EuEntityPermissionSubjectDetailsType(d.pop("subjectDetailsType"))




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


        def _parse_entity_by_fp(data: object) -> Union['EntityByFingerprintDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_by_fp_type_1 = EntityByFingerprintDetails.from_dict(data)



                return entity_by_fp_type_1
            except: # noqa: E722
                pass
            return cast(Union['EntityByFingerprintDetails', None, Unset], data)

        entity_by_fp = _parse_entity_by_fp(d.pop("entityByFp", UNSET))


        eu_entity_permission_subject_details = cls(
            subject_details_type=subject_details_type,
            person_by_fp_with_id=person_by_fp_with_id,
            person_by_fp_no_id=person_by_fp_no_id,
            entity_by_fp=entity_by_fp,
        )

        return eu_entity_permission_subject_details

