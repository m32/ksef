from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_permission_type import InvoicePermissionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.entity_authorizations_authorizing_entity_identifier import EntityAuthorizationsAuthorizingEntityIdentifier
  from ..models.entity_authorizations_author_identifier import EntityAuthorizationsAuthorIdentifier
  from ..models.entity_authorizations_authorized_entity_identifier import EntityAuthorizationsAuthorizedEntityIdentifier





T = TypeVar("T", bound="EntityAuthorizationGrant")



@_attrs_define
class EntityAuthorizationGrant:
    """ 
        Attributes:
            id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy operacjach odbierania.
            authorized_entity_identifier (EntityAuthorizationsAuthorizedEntityIdentifier): Identyfikator podmiotu
                uprawnionego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | PeppolId | Identyfikator dostawcy usług Peppol |
            authorizing_entity_identifier (EntityAuthorizationsAuthorizingEntityIdentifier): Identyfikator podmiotu
                uprawniającego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
            authorization_scope (InvoicePermissionType):
            description (str): Opis uprawnienia.
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania uprawnienia.
            author_identifier (Union['EntityAuthorizationsAuthorIdentifier', None, Unset]): Identyfikator osoby nadającej
                uprawnienie.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
     """

    id: str
    authorized_entity_identifier: 'EntityAuthorizationsAuthorizedEntityIdentifier'
    authorizing_entity_identifier: 'EntityAuthorizationsAuthorizingEntityIdentifier'
    authorization_scope: InvoicePermissionType
    description: str
    start_date: datetime.datetime
    author_identifier: Union['EntityAuthorizationsAuthorIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_authorizations_authorizing_entity_identifier import EntityAuthorizationsAuthorizingEntityIdentifier
        from ..models.entity_authorizations_author_identifier import EntityAuthorizationsAuthorIdentifier
        from ..models.entity_authorizations_authorized_entity_identifier import EntityAuthorizationsAuthorizedEntityIdentifier
        id = self.id

        authorized_entity_identifier = self.authorized_entity_identifier.to_dict()

        authorizing_entity_identifier = self.authorizing_entity_identifier.to_dict()

        authorization_scope = self.authorization_scope.value

        description = self.description

        start_date = self.start_date.isoformat()

        author_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.author_identifier, Unset):
            author_identifier = UNSET
        elif isinstance(self.author_identifier, EntityAuthorizationsAuthorIdentifier):
            author_identifier = self.author_identifier.to_dict()
        else:
            author_identifier = self.author_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "authorizedEntityIdentifier": authorized_entity_identifier,
            "authorizingEntityIdentifier": authorizing_entity_identifier,
            "authorizationScope": authorization_scope,
            "description": description,
            "startDate": start_date,
        })
        if author_identifier is not UNSET:
            field_dict["authorIdentifier"] = author_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_authorizations_authorizing_entity_identifier import EntityAuthorizationsAuthorizingEntityIdentifier
        from ..models.entity_authorizations_author_identifier import EntityAuthorizationsAuthorIdentifier
        from ..models.entity_authorizations_authorized_entity_identifier import EntityAuthorizationsAuthorizedEntityIdentifier
        d = dict(src_dict)
        id = d.pop("id")

        authorized_entity_identifier = EntityAuthorizationsAuthorizedEntityIdentifier.from_dict(d.pop("authorizedEntityIdentifier"))




        authorizing_entity_identifier = EntityAuthorizationsAuthorizingEntityIdentifier.from_dict(d.pop("authorizingEntityIdentifier"))




        authorization_scope = InvoicePermissionType(d.pop("authorizationScope"))




        description = d.pop("description")

        start_date = isoparse(d.pop("startDate"))




        def _parse_author_identifier(data: object) -> Union['EntityAuthorizationsAuthorIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_identifier_type_1 = EntityAuthorizationsAuthorIdentifier.from_dict(data)



                return author_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['EntityAuthorizationsAuthorIdentifier', None, Unset], data)

        author_identifier = _parse_author_identifier(d.pop("authorIdentifier", UNSET))


        entity_authorization_grant = cls(
            id=id,
            authorized_entity_identifier=authorized_entity_identifier,
            authorizing_entity_identifier=authorizing_entity_identifier,
            authorization_scope=authorization_scope,
            description=description,
            start_date=start_date,
            author_identifier=author_identifier,
        )

        return entity_authorization_grant

