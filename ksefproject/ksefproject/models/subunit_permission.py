from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subunit_permission_scope import SubunitPermissionScope
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.subunit_permissions_subunit_identifier import SubunitPermissionsSubunitIdentifier
  from ..models.subunit_permissions_authorized_identifier import SubunitPermissionsAuthorizedIdentifier
  from ..models.subunit_permissions_author_identifier import SubunitPermissionsAuthorIdentifier





T = TypeVar("T", bound="SubunitPermission")



@_attrs_define
class SubunitPermission:
    """ 
        Attributes:
            id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy operacjach odbierania.
            authorized_identifier (SubunitPermissionsAuthorizedIdentifier): Identyfikator uprawnionego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            subunit_identifier (SubunitPermissionsSubunitIdentifier): Identyfikator jednostki lub podmiotu podrzędnego.
                | Type | Value |
                | --- | --- |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
                | Nip | 10 cyfrowy numer NIP |
            author_identifier (SubunitPermissionsAuthorIdentifier): Identyfikator uprawniającego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            permission_scope (SubunitPermissionScope):
            description (str): Opis uprawnienia.
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania uprawnienia.
            subunit_name (Union[None, Unset, str]): Nazwa jednostki podrzędnej.
     """

    id: str
    authorized_identifier: 'SubunitPermissionsAuthorizedIdentifier'
    subunit_identifier: 'SubunitPermissionsSubunitIdentifier'
    author_identifier: 'SubunitPermissionsAuthorIdentifier'
    permission_scope: SubunitPermissionScope
    description: str
    start_date: datetime.datetime
    subunit_name: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.subunit_permissions_subunit_identifier import SubunitPermissionsSubunitIdentifier
        from ..models.subunit_permissions_authorized_identifier import SubunitPermissionsAuthorizedIdentifier
        from ..models.subunit_permissions_author_identifier import SubunitPermissionsAuthorIdentifier
        id = self.id

        authorized_identifier = self.authorized_identifier.to_dict()

        subunit_identifier = self.subunit_identifier.to_dict()

        author_identifier = self.author_identifier.to_dict()

        permission_scope = self.permission_scope.value

        description = self.description

        start_date = self.start_date.isoformat()

        subunit_name: Union[None, Unset, str]
        if isinstance(self.subunit_name, Unset):
            subunit_name = UNSET
        else:
            subunit_name = self.subunit_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "authorizedIdentifier": authorized_identifier,
            "subunitIdentifier": subunit_identifier,
            "authorIdentifier": author_identifier,
            "permissionScope": permission_scope,
            "description": description,
            "startDate": start_date,
        })
        if subunit_name is not UNSET:
            field_dict["subunitName"] = subunit_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subunit_permissions_subunit_identifier import SubunitPermissionsSubunitIdentifier
        from ..models.subunit_permissions_authorized_identifier import SubunitPermissionsAuthorizedIdentifier
        from ..models.subunit_permissions_author_identifier import SubunitPermissionsAuthorIdentifier
        d = dict(src_dict)
        id = d.pop("id")

        authorized_identifier = SubunitPermissionsAuthorizedIdentifier.from_dict(d.pop("authorizedIdentifier"))




        subunit_identifier = SubunitPermissionsSubunitIdentifier.from_dict(d.pop("subunitIdentifier"))




        author_identifier = SubunitPermissionsAuthorIdentifier.from_dict(d.pop("authorIdentifier"))




        permission_scope = SubunitPermissionScope(d.pop("permissionScope"))




        description = d.pop("description")

        start_date = isoparse(d.pop("startDate"))




        def _parse_subunit_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subunit_name = _parse_subunit_name(d.pop("subunitName", UNSET))


        subunit_permission = cls(
            id=id,
            authorized_identifier=authorized_identifier,
            subunit_identifier=subunit_identifier,
            author_identifier=author_identifier,
            permission_scope=permission_scope,
            description=description,
            start_date=start_date,
            subunit_name=subunit_name,
        )

        return subunit_permission

