from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
  from ..models.test_data_context_identifier import TestDataContextIdentifier





T = TypeVar("T", bound="TestDataPermissionsRevokeRequest")



@_attrs_define
class TestDataPermissionsRevokeRequest:
    """ 
        Attributes:
            context_identifier (TestDataContextIdentifier):
            authorized_identifier (TestDataAuthorizedIdentifier):
     """

    context_identifier: 'TestDataContextIdentifier'
    authorized_identifier: 'TestDataAuthorizedIdentifier'





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        context_identifier = self.context_identifier.to_dict()

        authorized_identifier = self.authorized_identifier.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "contextIdentifier": context_identifier,
            "authorizedIdentifier": authorized_identifier,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        d = dict(src_dict)
        context_identifier = TestDataContextIdentifier.from_dict(d.pop("contextIdentifier"))




        authorized_identifier = TestDataAuthorizedIdentifier.from_dict(d.pop("authorizedIdentifier"))




        test_data_permissions_revoke_request = cls(
            context_identifier=context_identifier,
            authorized_identifier=authorized_identifier,
        )

        return test_data_permissions_revoke_request

