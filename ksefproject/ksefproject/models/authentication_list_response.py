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
  from ..models.authentication_list_item import AuthenticationListItem





T = TypeVar("T", bound="AuthenticationListResponse")



@_attrs_define
class AuthenticationListResponse:
    """ 
        Attributes:
            items (list['AuthenticationListItem']): Lista sesji uwierzytelniania.
            continuation_token (Union[None, Unset, str]): Token służący do pobrania kolejnej strony wyników. Jeśli jest
                pusty, to nie ma kolejnych stron.
     """

    items: list['AuthenticationListItem']
    continuation_token: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.authentication_list_item import AuthenticationListItem
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)



        continuation_token: Union[None, Unset, str]
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "items": items,
        })
        if continuation_token is not UNSET:
            field_dict["continuationToken"] = continuation_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication_list_item import AuthenticationListItem
        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = AuthenticationListItem.from_dict(items_item_data)



            items.append(items_item)


        def _parse_continuation_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        continuation_token = _parse_continuation_token(d.pop("continuationToken", UNSET))


        authentication_list_response = cls(
            items=items,
            continuation_token=continuation_token,
        )

        return authentication_list_response

