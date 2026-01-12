from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TooManyRequestsResponseStatus")



@_attrs_define
class TooManyRequestsResponseStatus:
    """ Informacje o błędzie związanym z przekroczeniem limitu żądań.

        Attributes:
            code (int): Kod statusu HTTP odpowiadający błędowi. Zawsze ma wartość 429.
            description (str): Opis błędu zgodny z nazwą statusu HTTP.
            details (list[str]): Lista szczegółowych informacji opisujących przyczynę przekroczenia limitu żądań oraz
                wskazówki dotyczące ponowienia żądania.
     """

    code: int
    description: str
    details: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        details = self.details




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "description": description,
            "details": details,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        description = d.pop("description")

        details = cast(list[str], d.pop("details"))


        too_many_requests_response_status = cls(
            code=code,
            description=description,
            details=details,
        )


        too_many_requests_response_status.additional_properties = d
        return too_many_requests_response_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
