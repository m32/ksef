from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.indirect_permission_type import IndirectPermissionType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.indirect_permissions_target_identifier import IndirectPermissionsTargetIdentifier
  from ..models.indirect_permissions_subject_identifier import IndirectPermissionsSubjectIdentifier





T = TypeVar("T", bound="IndirectPermissionsGrantRequest")



@_attrs_define
class IndirectPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (IndirectPermissionsSubjectIdentifier): Identyfikator osoby fizycznej.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            permissions (list[IndirectPermissionType]): Lista nadawanych uprawnień. Każda wartość może wystąpić tylko raz.
            description (str): Opis uprawnienia
            target_identifier (Union['IndirectPermissionsTargetIdentifier', None, Unset]): Identyfikator kontekstu klienta.
                Nie przekazanie identyfikatora oznacza, że uprawnienie nadane w sposób pośredni jest typu generalnego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | AllPartners | Identyfikator oznaczający, że uprawnienie nadane w sposób pośredni jest typu generalnego |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
     """

    subject_identifier: 'IndirectPermissionsSubjectIdentifier'
    permissions: list[IndirectPermissionType]
    description: str
    target_identifier: Union['IndirectPermissionsTargetIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.indirect_permissions_target_identifier import IndirectPermissionsTargetIdentifier
        from ..models.indirect_permissions_subject_identifier import IndirectPermissionsSubjectIdentifier
        subject_identifier = self.subject_identifier.to_dict()

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)



        description = self.description

        target_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.target_identifier, Unset):
            target_identifier = UNSET
        elif isinstance(self.target_identifier, IndirectPermissionsTargetIdentifier):
            target_identifier = self.target_identifier.to_dict()
        else:
            target_identifier = self.target_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectIdentifier": subject_identifier,
            "permissions": permissions,
            "description": description,
        })
        if target_identifier is not UNSET:
            field_dict["targetIdentifier"] = target_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.indirect_permissions_target_identifier import IndirectPermissionsTargetIdentifier
        from ..models.indirect_permissions_subject_identifier import IndirectPermissionsSubjectIdentifier
        d = dict(src_dict)
        subject_identifier = IndirectPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = IndirectPermissionType(permissions_item_data)



            permissions.append(permissions_item)


        description = d.pop("description")

        def _parse_target_identifier(data: object) -> Union['IndirectPermissionsTargetIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_identifier_type_1 = IndirectPermissionsTargetIdentifier.from_dict(data)



                return target_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['IndirectPermissionsTargetIdentifier', None, Unset], data)

        target_identifier = _parse_target_identifier(d.pop("targetIdentifier", UNSET))


        indirect_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            permissions=permissions,
            description=description,
            target_identifier=target_identifier,
        )

        return indirect_permissions_grant_request

