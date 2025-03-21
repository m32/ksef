from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from ..types import UNSET, Unset
from typing import Dict

if TYPE_CHECKING:
  from ..models.credential_accounting_request_type import CredentialAccountingRequestType





T = TypeVar("T", bound="RevokeAccountingCredentialsRequest")


@_attrs_define
class RevokeAccountingCredentialsRequest:
    """ 
        Attributes:
            revoke_credentials (CredentialAccountingRequestType):
            revoke_credential (Union[Unset, CredentialAccountingRequestType]):
     """

    revoke_credentials: 'CredentialAccountingRequestType'
    revoke_credential: Union[Unset, 'CredentialAccountingRequestType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credential_accounting_request_type import CredentialAccountingRequestType
        revoke_credentials = self.revoke_credentials.to_dict()

        revoke_credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revoke_credential, Unset):
            revoke_credential = self.revoke_credential.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "revokeCredentials": revoke_credentials,
        })
        if revoke_credential is not UNSET:
            field_dict["revokeCredential"] = revoke_credential

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credential_accounting_request_type import CredentialAccountingRequestType
        d = src_dict.copy()
        revoke_credentials = CredentialAccountingRequestType.from_dict(d.pop("revokeCredentials"))




        _revoke_credential = d.pop("revokeCredential", UNSET)
        revoke_credential: Union[Unset, CredentialAccountingRequestType]
        if isinstance(_revoke_credential,  Unset):
            revoke_credential = UNSET
        else:
            revoke_credential = CredentialAccountingRequestType.from_dict(_revoke_credential)




        revoke_accounting_credentials_request = cls(
            revoke_credentials=revoke_credentials,
            revoke_credential=revoke_credential,
        )

        revoke_accounting_credentials_request.additional_properties = d
        return revoke_accounting_credentials_request

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
