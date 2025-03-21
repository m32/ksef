from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
  from ..models.credentials_identifier_request_accounting_type import CredentialsIdentifierRequestAccountingType
  from ..models.credential_role_request_accounting_base_type import CredentialRoleRequestAccountingBaseType





T = TypeVar("T", bound="CredentialAccountingRequestType")


@_attrs_define
class CredentialAccountingRequestType:
    """ 
        Attributes:
            credentials_role_list (List['CredentialRoleRequestAccountingBaseType']):
            partner_credential_identifier (CredentialsIdentifierRequestAccountingType):
            target_credential_identifier (CredentialsIdentifierRequestType):
     """

    credentials_role_list: List['CredentialRoleRequestAccountingBaseType']
    partner_credential_identifier: 'CredentialsIdentifierRequestAccountingType'
    target_credential_identifier: 'CredentialsIdentifierRequestType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
        from ..models.credentials_identifier_request_accounting_type import CredentialsIdentifierRequestAccountingType
        from ..models.credential_role_request_accounting_base_type import CredentialRoleRequestAccountingBaseType
        credentials_role_list = []
        for credentials_role_list_item_data in self.credentials_role_list:
            credentials_role_list_item = credentials_role_list_item_data.to_dict()

            credentials_role_list.append(credentials_role_list_item)




        partner_credential_identifier = self.partner_credential_identifier.to_dict()

        target_credential_identifier = self.target_credential_identifier.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credentialsRoleList": credentials_role_list,
            "partnerCredentialIdentifier": partner_credential_identifier,
            "targetCredentialIdentifier": target_credential_identifier,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
        from ..models.credentials_identifier_request_accounting_type import CredentialsIdentifierRequestAccountingType
        from ..models.credential_role_request_accounting_base_type import CredentialRoleRequestAccountingBaseType
        d = src_dict.copy()
        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList")
        for credentials_role_list_item_data in (_credentials_role_list):
            credentials_role_list_item = CredentialRoleRequestAccountingBaseType.from_dict(credentials_role_list_item_data)



            credentials_role_list.append(credentials_role_list_item)


        partner_credential_identifier = CredentialsIdentifierRequestAccountingType.from_dict(d.pop("partnerCredentialIdentifier"))




        target_credential_identifier = CredentialsIdentifierRequestType.from_dict(d.pop("targetCredentialIdentifier"))




        credential_accounting_request_type = cls(
            credentials_role_list=credentials_role_list,
            partner_credential_identifier=partner_credential_identifier,
            target_credential_identifier=target_credential_identifier,
        )

        credential_accounting_request_type.additional_properties = d
        return credential_accounting_request_type

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
