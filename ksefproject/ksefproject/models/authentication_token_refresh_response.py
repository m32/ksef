from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.token_info import TokenInfo





T = TypeVar("T", bound="AuthenticationTokenRefreshResponse")



@_attrs_define
class AuthenticationTokenRefreshResponse:
    """ 
        Attributes:
            access_token (TokenInfo):
     """

    access_token: 'TokenInfo'





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_info import TokenInfo
        access_token = self.access_token.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "accessToken": access_token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_info import TokenInfo
        d = dict(src_dict)
        access_token = TokenInfo.from_dict(d.pop("accessToken"))




        authentication_token_refresh_response = cls(
            access_token=access_token,
        )

        return authentication_token_refresh_response

