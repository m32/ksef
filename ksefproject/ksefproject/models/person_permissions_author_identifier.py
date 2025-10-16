from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.person_permissions_author_identifier_type import PersonPermissionsAuthorIdentifierType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PersonPermissionsAuthorIdentifier")



@_attrs_define
class PersonPermissionsAuthorIdentifier:
    """ Identyfikator osoby lub podmiotu nadającego uprawnienie.
    | Type | Value |
    | --- | --- |
    | Nip | 10 cyfrowy numer NIP |
    | Pesel | 11 cyfrowy numer PESEL |
    | Fingerprint | Odcisk palca certyfikatu |
    | System | Identyfikator systemowy KSeF |

        Attributes:
            type_ (PersonPermissionsAuthorIdentifierType):
            value (Union[None, Unset, str]): Wartość identyfikatora. W przypadku typu System należy pozostawić puste. W
                pozostałych przypadkach pole jest wymagane.
     """

    type_: PersonPermissionsAuthorIdentifierType
    value: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PersonPermissionsAuthorIdentifierType(d.pop("type"))




        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))


        person_permissions_author_identifier = cls(
            type_=type_,
            value=value,
        )

        return person_permissions_author_identifier

