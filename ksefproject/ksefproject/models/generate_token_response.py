from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="GenerateTokenResponse")



@_attrs_define
class GenerateTokenResponse:
    """ 
        Attributes:
            reference_number (Union[None, Unset, str]): Numer referencyjny tokena KSeF. Za jego pomocą można sprawdzić jego
                status lub go unieważnić.
            token (Union[None, Unset, str]): Token KSeF.
     """

    reference_number: Union[None, Unset, str] = UNSET
    token: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        reference_number: Union[None, Unset, str]
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        token: Union[None, Unset, str]
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_number = _parse_reference_number(d.pop("referenceNumber", UNSET))


        def _parse_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        token = _parse_token(d.pop("token", UNSET))


        generate_token_response = cls(
            reference_number=reference_number,
            token=token,
        )

        return generate_token_response

