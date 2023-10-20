from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.credentials_identifier_request_individual_type import CredentialsIdentifierRequestIndividualType
  from ..models.credentials_role_request_context_described_type import CredentialsRoleRequestContextDescribedType
  from ..models.credentials_identifier_request_institutional_type import CredentialsIdentifierRequestInstitutionalType





T = TypeVar("T", bound="GrantContextCredentialsRequestType")


@_attrs_define
class GrantContextCredentialsRequestType:
    """ 
        Attributes:
            context_identifier (CredentialsIdentifierRequestInstitutionalType):
            credentials_identifier (CredentialsIdentifierRequestIndividualType):
            credentials_role (CredentialsRoleRequestContextDescribedType):
     """

    context_identifier: 'CredentialsIdentifierRequestInstitutionalType'
    credentials_identifier: 'CredentialsIdentifierRequestIndividualType'
    credentials_role: 'CredentialsRoleRequestContextDescribedType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_identifier_request_individual_type import CredentialsIdentifierRequestIndividualType
        from ..models.credentials_role_request_context_described_type import CredentialsRoleRequestContextDescribedType
        from ..models.credentials_identifier_request_institutional_type import CredentialsIdentifierRequestInstitutionalType
        context_identifier = self.context_identifier.to_dict()

        credentials_identifier = self.credentials_identifier.to_dict()

        credentials_role = self.credentials_role.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextIdentifier": context_identifier,
            "credentialsIdentifier": credentials_identifier,
            "credentialsRole": credentials_role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_identifier_request_individual_type import CredentialsIdentifierRequestIndividualType
        from ..models.credentials_role_request_context_described_type import CredentialsRoleRequestContextDescribedType
        from ..models.credentials_identifier_request_institutional_type import CredentialsIdentifierRequestInstitutionalType
        d = src_dict.copy()
        context_identifier = CredentialsIdentifierRequestInstitutionalType.from_dict(d.pop("contextIdentifier"))




        credentials_identifier = CredentialsIdentifierRequestIndividualType.from_dict(d.pop("credentialsIdentifier"))




        credentials_role = CredentialsRoleRequestContextDescribedType.from_dict(d.pop("credentialsRole"))




        grant_context_credentials_request_type = cls(
            context_identifier=context_identifier,
            credentials_identifier=credentials_identifier,
            credentials_role=credentials_role,
        )

        grant_context_credentials_request_type.additional_properties = d
        return grant_context_credentials_request_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
