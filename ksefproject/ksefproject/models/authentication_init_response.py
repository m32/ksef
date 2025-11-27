from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.token_info import TokenInfo





T = TypeVar("T", bound="AuthenticationInitResponse")



@_attrs_define
class AuthenticationInitResponse:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            authentication_token (TokenInfo):
     """

    reference_number: str
    authentication_token: 'TokenInfo'





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_info import TokenInfo
        reference_number = self.reference_number

        authentication_token = self.authentication_token.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "authenticationToken": authentication_token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_info import TokenInfo
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        authentication_token = TokenInfo.from_dict(d.pop("authenticationToken"))




        authentication_init_response = cls(
            reference_number=reference_number,
            authentication_token=authentication_token,
        )

        return authentication_init_response

