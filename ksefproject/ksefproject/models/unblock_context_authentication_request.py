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
  from ..models.test_data_authentication_context_identifier import TestDataAuthenticationContextIdentifier





T = TypeVar("T", bound="UnblockContextAuthenticationRequest")



@_attrs_define
class UnblockContextAuthenticationRequest:
    """ 
        Attributes:
            context_identifier (Union['TestDataAuthenticationContextIdentifier', None, Unset]):
     """

    context_identifier: Union['TestDataAuthenticationContextIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_data_authentication_context_identifier import TestDataAuthenticationContextIdentifier
        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, TestDataAuthenticationContextIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_data_authentication_context_identifier import TestDataAuthenticationContextIdentifier
        d = dict(src_dict)
        def _parse_context_identifier(data: object) -> Union['TestDataAuthenticationContextIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_identifier_type_1 = TestDataAuthenticationContextIdentifier.from_dict(data)



                return context_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TestDataAuthenticationContextIdentifier', None, Unset], data)

        context_identifier = _parse_context_identifier(d.pop("contextIdentifier", UNSET))


        unblock_context_authentication_request = cls(
            context_identifier=context_identifier,
        )

        return unblock_context_authentication_request

