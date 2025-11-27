from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.indirect_permissions_target_identifier_type import IndirectPermissionsTargetIdentifierType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="IndirectPermissionsTargetIdentifier")



@_attrs_define
class IndirectPermissionsTargetIdentifier:
    """ Identyfikator kontekstu klienta. Nie przekazanie identyfikatora oznacza, że uprawnienie nadane w sposób pośredni
    jest typu generalnego.
    | Type | Value |
    | --- | --- |
    | Nip | 10 cyfrowy numer NIP |
    | AllPartners | Identyfikator oznaczający, że uprawnienie nadane w sposób pośredni jest typu generalnego |
    | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |

        Attributes:
            type_ (IndirectPermissionsTargetIdentifierType):
            value (Union[None, Unset, str]): Wartość identyfikatora. W przypadku typu AllPartners należy pozostawić puste. W
                pozostałych przypadkach pole jest wymagane.
     """

    type_: IndirectPermissionsTargetIdentifierType
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
        type_ = IndirectPermissionsTargetIdentifierType(d.pop("type"))




        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))


        indirect_permissions_target_identifier = cls(
            type_=type_,
            value=value,
        )

        return indirect_permissions_target_identifier

