from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.token_info import TokenInfo





T = TypeVar("T", bound="AuthenticationTokensResponse")



@_attrs_define
class AuthenticationTokensResponse:
    """ 
        Attributes:
            access_token (TokenInfo):
            refresh_token (TokenInfo):
     """

    access_token: 'TokenInfo'
    refresh_token: 'TokenInfo'





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_info import TokenInfo
        access_token = self.access_token.to_dict()

        refresh_token = self.refresh_token.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "accessToken": access_token,
            "refreshToken": refresh_token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_info import TokenInfo
        d = dict(src_dict)
        access_token = TokenInfo.from_dict(d.pop("accessToken"))




        refresh_token = TokenInfo.from_dict(d.pop("refreshToken"))




        authentication_tokens_response = cls(
            access_token=access_token,
            refresh_token=refresh_token,
        )

        return authentication_tokens_response

