from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.subunit_permissions_subject_identifier import SubunitPermissionsSubjectIdentifier
  from ..models.subunit_permissions_context_identifier import SubunitPermissionsContextIdentifier





T = TypeVar("T", bound="SubunitPermissionsGrantRequest")



@_attrs_define
class SubunitPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (SubunitPermissionsSubjectIdentifier): Identyfikator podmiotu lub osoby fizycznej.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            context_identifier (SubunitPermissionsContextIdentifier): Identyfikator podmiotu podrzędnego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
            description (str): Opis uprawnienia
            subunit_name (Union[None, Unset, str]): Nazwa jednostki podrzędnej. W przypadku jednostki podrzędnej z
                identyfikatorem wewnętrznym pole jest wymagane.
     """

    subject_identifier: 'SubunitPermissionsSubjectIdentifier'
    context_identifier: 'SubunitPermissionsContextIdentifier'
    description: str
    subunit_name: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.subunit_permissions_subject_identifier import SubunitPermissionsSubjectIdentifier
        from ..models.subunit_permissions_context_identifier import SubunitPermissionsContextIdentifier
        subject_identifier = self.subject_identifier.to_dict()

        context_identifier = self.context_identifier.to_dict()

        description = self.description

        subunit_name: Union[None, Unset, str]
        if isinstance(self.subunit_name, Unset):
            subunit_name = UNSET
        else:
            subunit_name = self.subunit_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectIdentifier": subject_identifier,
            "contextIdentifier": context_identifier,
            "description": description,
        })
        if subunit_name is not UNSET:
            field_dict["subunitName"] = subunit_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subunit_permissions_subject_identifier import SubunitPermissionsSubjectIdentifier
        from ..models.subunit_permissions_context_identifier import SubunitPermissionsContextIdentifier
        d = dict(src_dict)
        subject_identifier = SubunitPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        context_identifier = SubunitPermissionsContextIdentifier.from_dict(d.pop("contextIdentifier"))




        description = d.pop("description")

        def _parse_subunit_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subunit_name = _parse_subunit_name(d.pop("subunitName", UNSET))


        subunit_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            context_identifier=context_identifier,
            description=description,
            subunit_name=subunit_name,
        )

        return subunit_permissions_grant_request

