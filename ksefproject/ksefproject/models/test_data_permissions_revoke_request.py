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
  from ..models.test_data_context_identifier import TestDataContextIdentifier
  from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier





T = TypeVar("T", bound="TestDataPermissionsRevokeRequest")



@_attrs_define
class TestDataPermissionsRevokeRequest:
    """ 
        Attributes:
            context_identifier (Union['TestDataContextIdentifier', None, Unset]):
            authorized_identifier (Union['TestDataAuthorizedIdentifier', None, Unset]):
     """

    context_identifier: Union['TestDataContextIdentifier', None, Unset] = UNSET
    authorized_identifier: Union['TestDataAuthorizedIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, TestDataContextIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier

        authorized_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorized_identifier, Unset):
            authorized_identifier = UNSET
        elif isinstance(self.authorized_identifier, TestDataAuthorizedIdentifier):
            authorized_identifier = self.authorized_identifier.to_dict()
        else:
            authorized_identifier = self.authorized_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier
        if authorized_identifier is not UNSET:
            field_dict["authorizedIdentifier"] = authorized_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        d = dict(src_dict)
        def _parse_context_identifier(data: object) -> Union['TestDataContextIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_identifier_type_1 = TestDataContextIdentifier.from_dict(data)



                return context_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TestDataContextIdentifier', None, Unset], data)

        context_identifier = _parse_context_identifier(d.pop("contextIdentifier", UNSET))


        def _parse_authorized_identifier(data: object) -> Union['TestDataAuthorizedIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorized_identifier_type_1 = TestDataAuthorizedIdentifier.from_dict(data)



                return authorized_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TestDataAuthorizedIdentifier', None, Unset], data)

        authorized_identifier = _parse_authorized_identifier(d.pop("authorizedIdentifier", UNSET))


        test_data_permissions_revoke_request = cls(
            context_identifier=context_identifier,
            authorized_identifier=authorized_identifier,
        )

        return test_data_permissions_revoke_request

