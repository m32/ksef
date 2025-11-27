from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authentication_token_status import AuthenticationTokenStatus
from ..models.token_permission_type import TokenPermissionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.token_author_identifier_type_identifier import TokenAuthorIdentifierTypeIdentifier
  from ..models.token_context_identifier_type_identifier import TokenContextIdentifierTypeIdentifier





T = TypeVar("T", bound="QueryTokensResponseItem")



@_attrs_define
class QueryTokensResponseItem:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            author_identifier (TokenAuthorIdentifierTypeIdentifier):
            context_identifier (TokenContextIdentifierTypeIdentifier):
            description (str): Opis tokena.
            requested_permissions (list[TokenPermissionType]): Uprawnienia przypisane tokenowi.
            date_created (datetime.datetime): Data i czas utworzenia tokena.
            status (AuthenticationTokenStatus): | Wartość | Opis |
                | --- | --- |
                | Pending | Token został utworzony ale jest jeszcze w trakcie aktywacji i nadawania uprawnień. Nie może być
                jeszcze wykorzystywany do uwierzytelniania. |
                | Active | Token jest aktywny i może być wykorzystywany do uwierzytelniania. |
                | Revoking | Token jest w trakcie unieważniania. Nie może już być wykorzystywany do uwierzytelniania. |
                | Revoked | Token został unieważniony i nie może być wykorzystywany do uwierzytelniania. |
                | Failed | Nie udało się aktywować tokena. Należy wygenerować nowy token, obecny nie może być wykorzystywany do
                uwierzytelniania. |
            last_use_date (Union[None, Unset, datetime.datetime]): Data ostatniego użycia tokena.
            status_details (Union[None, Unset, list[str]]): Dodatkowe informacje na temat statusu, zwracane w przypadku
                błędów.
     """

    reference_number: str
    author_identifier: 'TokenAuthorIdentifierTypeIdentifier'
    context_identifier: 'TokenContextIdentifierTypeIdentifier'
    description: str
    requested_permissions: list[TokenPermissionType]
    date_created: datetime.datetime
    status: AuthenticationTokenStatus
    last_use_date: Union[None, Unset, datetime.datetime] = UNSET
    status_details: Union[None, Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_author_identifier_type_identifier import TokenAuthorIdentifierTypeIdentifier
        from ..models.token_context_identifier_type_identifier import TokenContextIdentifierTypeIdentifier
        reference_number = self.reference_number

        author_identifier = self.author_identifier.to_dict()

        context_identifier = self.context_identifier.to_dict()

        description = self.description

        requested_permissions = []
        for requested_permissions_item_data in self.requested_permissions:
            requested_permissions_item = requested_permissions_item_data.value
            requested_permissions.append(requested_permissions_item)



        date_created = self.date_created.isoformat()

        status = self.status.value

        last_use_date: Union[None, Unset, str]
        if isinstance(self.last_use_date, Unset):
            last_use_date = UNSET
        elif isinstance(self.last_use_date, datetime.datetime):
            last_use_date = self.last_use_date.isoformat()
        else:
            last_use_date = self.last_use_date

        status_details: Union[None, Unset, list[str]]
        if isinstance(self.status_details, Unset):
            status_details = UNSET
        elif isinstance(self.status_details, list):
            status_details = self.status_details


        else:
            status_details = self.status_details


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "authorIdentifier": author_identifier,
            "contextIdentifier": context_identifier,
            "description": description,
            "requestedPermissions": requested_permissions,
            "dateCreated": date_created,
            "status": status,
        })
        if last_use_date is not UNSET:
            field_dict["lastUseDate"] = last_use_date
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_author_identifier_type_identifier import TokenAuthorIdentifierTypeIdentifier
        from ..models.token_context_identifier_type_identifier import TokenContextIdentifierTypeIdentifier
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        author_identifier = TokenAuthorIdentifierTypeIdentifier.from_dict(d.pop("authorIdentifier"))




        context_identifier = TokenContextIdentifierTypeIdentifier.from_dict(d.pop("contextIdentifier"))




        description = d.pop("description")

        requested_permissions = []
        _requested_permissions = d.pop("requestedPermissions")
        for requested_permissions_item_data in (_requested_permissions):
            requested_permissions_item = TokenPermissionType(requested_permissions_item_data)



            requested_permissions.append(requested_permissions_item)


        date_created = isoparse(d.pop("dateCreated"))




        status = AuthenticationTokenStatus(d.pop("status"))




        def _parse_last_use_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_use_date_type_0 = isoparse(data)



                return last_use_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_use_date = _parse_last_use_date(d.pop("lastUseDate", UNSET))


        def _parse_status_details(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_details_type_0 = cast(list[str], data)

                return status_details_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        status_details = _parse_status_details(d.pop("statusDetails", UNSET))


        query_tokens_response_item = cls(
            reference_number=reference_number,
            author_identifier=author_identifier,
            context_identifier=context_identifier,
            description=description,
            requested_permissions=requested_permissions,
            date_created=date_created,
            status=status,
            last_use_date=last_use_date,
            status_details=status_details,
        )

        return query_tokens_response_item

