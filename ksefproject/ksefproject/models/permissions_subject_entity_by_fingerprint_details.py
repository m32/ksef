from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.entity_subject_by_fingerprint_details_type import EntitySubjectByFingerprintDetailsType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PermissionsSubjectEntityByFingerprintDetails")



@_attrs_define
class PermissionsSubjectEntityByFingerprintDetails:
    """ 
        Attributes:
            subject_details_type (EntitySubjectByFingerprintDetailsType): | Wartość | Opis |
                | --- | --- |
                | EntityByFingerprint | Podmiot identyfikowany odciskiem palca pieczęci kwalifikowanej. |
            full_name (str): Pełna nazwa podmiotu.
            address (Union[None, Unset, str]): Adres podmiotu.
     """

    subject_details_type: EntitySubjectByFingerprintDetailsType
    full_name: str
    address: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        subject_details_type = self.subject_details_type.value

        full_name = self.full_name

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectDetailsType": subject_details_type,
            "fullName": full_name,
        })
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject_details_type = EntitySubjectByFingerprintDetailsType(d.pop("subjectDetailsType"))




        full_name = d.pop("fullName")

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))


        permissions_subject_entity_by_fingerprint_details = cls(
            subject_details_type=subject_details_type,
            full_name=full_name,
            address=address,
        )

        return permissions_subject_entity_by_fingerprint_details

