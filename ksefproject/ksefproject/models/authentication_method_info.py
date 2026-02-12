from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authentication_method_category import AuthenticationMethodCategory






T = TypeVar("T", bound="AuthenticationMethodInfo")



@_attrs_define
class AuthenticationMethodInfo:
    """ 
        Attributes:
            category (AuthenticationMethodCategory): | Wartość | Opis |
                | --- | --- |
                | XadesSignature | Uwierzytelnienie podpisem Xades. |
                | NationalNode | Uwierzytelnienie za pomocą Węzła Krajowego (login.gov.pl). |
                | Token | Uwierzytelnienie tokenem. |
                | Other | Uwierzytelnienie inną metodą. |
            code (str): Kod metody uwierzytelnienia.
            display_name (str): Nazwa metody uwierzytelnienia do wyświetlenia użytkownikowi.
     """

    category: AuthenticationMethodCategory
    code: str
    display_name: str





    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        code = self.code

        display_name = self.display_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "category": category,
            "code": code,
            "displayName": display_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = AuthenticationMethodCategory(d.pop("category"))




        code = d.pop("code")

        display_name = d.pop("displayName")

        authentication_method_info = cls(
            category=category,
            code=code,
            display_name=display_name,
        )

        return authentication_method_info

