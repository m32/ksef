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
            reference_number (Union[None, Unset, str]): Numer referencyjny tokena.
            author_identifier (Union['TokenAuthorIdentifierTypeIdentifier', None, Unset]): Identyfikator osoby która
                wygenerowała token.
            context_identifier (Union['TokenContextIdentifierTypeIdentifier', None, Unset]): Identyfikator kontekstu, w
                którym został wygenerowany token i do którego daje dostęp.
            description (Union[None, Unset, str]): Opis tokena.
            requested_permissions (Union[None, Unset, list[TokenPermissionType]]): Uprawnienia przypisane tokenowi.
            date_created (Union[Unset, datetime.datetime]): Data i czas utworzenia tokena.
            last_use_date (Union[None, Unset, datetime.datetime]): Data ostatniego użycia tokena.
            status (Union[Unset, AuthenticationTokenStatus]): | Wartość | Opis |
                | --- | --- |
                | Pending | Token został utworzony ale jest jeszcze w trakcie aktywacji i nadawania uprawnień. Nie może być
                jeszcze wykorzystywany do uwierzytelniania. |
                | Active | Token jest aktywny i może być wykorzystywany do uwierzytelniania. |
                | Revoking | Token jest w trakcie unieważniania. Nie może już być wykorzystywany do uwierzytelniania. |
                | Revoked | Token został unieważniony i nie może być wykorzystywany do uwierzytelniania. |
                | Failed | Nie udało się aktywować tokena. Należy wygenerować nowy token, obecny nie może być wykorzystywany do
                uwierzytelniania. |
            status_details (Union[None, Unset, list[str]]): Dodatkowe informacje na temat statusu, zwracane w przypadku
                błędów.
     """

    reference_number: Union[None, Unset, str] = UNSET
    author_identifier: Union['TokenAuthorIdentifierTypeIdentifier', None, Unset] = UNSET
    context_identifier: Union['TokenContextIdentifierTypeIdentifier', None, Unset] = UNSET
    description: Union[None, Unset, str] = UNSET
    requested_permissions: Union[None, Unset, list[TokenPermissionType]] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_use_date: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[Unset, AuthenticationTokenStatus] = UNSET
    status_details: Union[None, Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_author_identifier_type_identifier import TokenAuthorIdentifierTypeIdentifier
        from ..models.token_context_identifier_type_identifier import TokenContextIdentifierTypeIdentifier
        reference_number: Union[None, Unset, str]
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        author_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.author_identifier, Unset):
            author_identifier = UNSET
        elif isinstance(self.author_identifier, TokenAuthorIdentifierTypeIdentifier):
            author_identifier = self.author_identifier.to_dict()
        else:
            author_identifier = self.author_identifier

        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, TokenContextIdentifierTypeIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        requested_permissions: Union[None, Unset, list[str]]
        if isinstance(self.requested_permissions, Unset):
            requested_permissions = UNSET
        elif isinstance(self.requested_permissions, list):
            requested_permissions = []
            for requested_permissions_type_0_item_data in self.requested_permissions:
                requested_permissions_type_0_item = requested_permissions_type_0_item_data.value
                requested_permissions.append(requested_permissions_type_0_item)


        else:
            requested_permissions = self.requested_permissions

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_use_date: Union[None, Unset, str]
        if isinstance(self.last_use_date, Unset):
            last_use_date = UNSET
        elif isinstance(self.last_use_date, datetime.datetime):
            last_use_date = self.last_use_date.isoformat()
        else:
            last_use_date = self.last_use_date

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        status_details: Union[None, Unset, list[str]]
        if isinstance(self.status_details, Unset):
            status_details = UNSET
        elif isinstance(self.status_details, list):
            status_details = self.status_details


        else:
            status_details = self.status_details


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if author_identifier is not UNSET:
            field_dict["authorIdentifier"] = author_identifier
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if requested_permissions is not UNSET:
            field_dict["requestedPermissions"] = requested_permissions
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_use_date is not UNSET:
            field_dict["lastUseDate"] = last_use_date
        if status is not UNSET:
            field_dict["status"] = status
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_author_identifier_type_identifier import TokenAuthorIdentifierTypeIdentifier
        from ..models.token_context_identifier_type_identifier import TokenContextIdentifierTypeIdentifier
        d = dict(src_dict)
        def _parse_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_number = _parse_reference_number(d.pop("referenceNumber", UNSET))


        def _parse_author_identifier(data: object) -> Union['TokenAuthorIdentifierTypeIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_identifier_type_1 = TokenAuthorIdentifierTypeIdentifier.from_dict(data)



                return author_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TokenAuthorIdentifierTypeIdentifier', None, Unset], data)

        author_identifier = _parse_author_identifier(d.pop("authorIdentifier", UNSET))


        def _parse_context_identifier(data: object) -> Union['TokenContextIdentifierTypeIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_identifier_type_1 = TokenContextIdentifierTypeIdentifier.from_dict(data)



                return context_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TokenContextIdentifierTypeIdentifier', None, Unset], data)

        context_identifier = _parse_context_identifier(d.pop("contextIdentifier", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_requested_permissions(data: object) -> Union[None, Unset, list[TokenPermissionType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requested_permissions_type_0 = []
                _requested_permissions_type_0 = data
                for requested_permissions_type_0_item_data in (_requested_permissions_type_0):
                    requested_permissions_type_0_item = TokenPermissionType(requested_permissions_type_0_item_data)



                    requested_permissions_type_0.append(requested_permissions_type_0_item)

                return requested_permissions_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[TokenPermissionType]], data)

        requested_permissions = _parse_requested_permissions(d.pop("requestedPermissions", UNSET))


        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created,  Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)




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


        _status = d.pop("status", UNSET)
        status: Union[Unset, AuthenticationTokenStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AuthenticationTokenStatus(_status)




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
            last_use_date=last_use_date,
            status=status,
            status_details=status_details,
        )

        return query_tokens_response_item

