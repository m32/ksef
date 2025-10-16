from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ExceptionDetails")



@_attrs_define
class ExceptionDetails:
    """ 
        Attributes:
            exception_code (Union[Unset, int]):
            exception_description (Union[None, Unset, str]):
            details (Union[None, Unset, list[str]]):
     """

    exception_code: Union[Unset, int] = UNSET
    exception_description: Union[None, Unset, str] = UNSET
    details: Union[None, Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        exception_code = self.exception_code

        exception_description: Union[None, Unset, str]
        if isinstance(self.exception_description, Unset):
            exception_description = UNSET
        else:
            exception_description = self.exception_description

        details: Union[None, Unset, list[str]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details


        else:
            details = self.details


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if exception_code is not UNSET:
            field_dict["exceptionCode"] = exception_code
        if exception_description is not UNSET:
            field_dict["exceptionDescription"] = exception_description
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exception_code = d.pop("exceptionCode", UNSET)

        def _parse_exception_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exception_description = _parse_exception_description(d.pop("exceptionDescription", UNSET))


        def _parse_details(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        details = _parse_details(d.pop("details", UNSET))


        exception_details = cls(
            exception_code=exception_code,
            exception_description=exception_description,
            details=details,
        )

        return exception_details

