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
  from ..models.query_tokens_response_item import QueryTokensResponseItem





T = TypeVar("T", bound="QueryTokensResponse")



@_attrs_define
class QueryTokensResponse:
    """ 
        Attributes:
            tokens (list['QueryTokensResponseItem']): Lista tokenów uwierzytelniających.
            continuation_token (Union[None, Unset, str]): Token służący do pobrania kolejnej strony wyników. Jeśli jest
                pusty, to nie ma kolejnych stron.
     """

    tokens: list['QueryTokensResponseItem']
    continuation_token: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_tokens_response_item import QueryTokensResponseItem
        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)



        continuation_token: Union[None, Unset, str]
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tokens": tokens,
        })
        if continuation_token is not UNSET:
            field_dict["continuationToken"] = continuation_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_tokens_response_item import QueryTokensResponseItem
        d = dict(src_dict)
        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in (_tokens):
            tokens_item = QueryTokensResponseItem.from_dict(tokens_item_data)



            tokens.append(tokens_item)


        def _parse_continuation_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        continuation_token = _parse_continuation_token(d.pop("continuationToken", UNSET))


        query_tokens_response = cls(
            tokens=tokens,
            continuation_token=continuation_token,
        )

        return query_tokens_response

