from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from ..models.v2_credentials_role_granted_for_institution_inheritance_type_role_type import V2CredentialsRoleGrantedForInstitutionInheritanceTypeRoleType

if TYPE_CHECKING:
  from ..models.credentials_identifier_response_institutional_nip_type import CredentialsIdentifierResponseInstitutionalNipType





T = TypeVar("T", bound="V2CredentialsRoleGrantedForInstitutionInheritanceType")


@_attrs_define
class V2CredentialsRoleGrantedForInstitutionInheritanceType:
    """ 
        Attributes:
            grantee_identifier (Union[Unset, CredentialsIdentifierResponseInstitutionalNipType]):
            role_description (Union[Unset, str]):
            role_type (Union[Unset, V2CredentialsRoleGrantedForInstitutionInheritanceTypeRoleType]):
     """

    grantee_identifier: Union[Unset, 'CredentialsIdentifierResponseInstitutionalNipType'] = UNSET
    role_description: Union[Unset, str] = UNSET
    role_type: Union[Unset, V2CredentialsRoleGrantedForInstitutionInheritanceTypeRoleType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_identifier_response_institutional_nip_type import CredentialsIdentifierResponseInstitutionalNipType
        grantee_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grantee_identifier, Unset):
            grantee_identifier = self.grantee_identifier.to_dict()

        role_description = self.role_description
        role_type: Union[Unset, str] = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if grantee_identifier is not UNSET:
            field_dict["granteeIdentifier"] = grantee_identifier
        if role_description is not UNSET:
            field_dict["roleDescription"] = role_description
        if role_type is not UNSET:
            field_dict["roleType"] = role_type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_identifier_response_institutional_nip_type import CredentialsIdentifierResponseInstitutionalNipType
        d = src_dict.copy()
        _grantee_identifier = d.pop("granteeIdentifier", UNSET)
        grantee_identifier: Union[Unset, CredentialsIdentifierResponseInstitutionalNipType]
        if isinstance(_grantee_identifier,  Unset):
            grantee_identifier = UNSET
        else:
            grantee_identifier = CredentialsIdentifierResponseInstitutionalNipType.from_dict(_grantee_identifier)




        role_description = d.pop("roleDescription", UNSET)

        _role_type = d.pop("roleType", UNSET)
        role_type: Union[Unset, V2CredentialsRoleGrantedForInstitutionInheritanceTypeRoleType]
        if isinstance(_role_type,  Unset):
            role_type = UNSET
        else:
            role_type = V2CredentialsRoleGrantedForInstitutionInheritanceTypeRoleType(_role_type)




        v2_credentials_role_granted_for_institution_inheritance_type = cls(
            grantee_identifier=grantee_identifier,
            role_description=role_description,
            role_type=role_type,
        )

        v2_credentials_role_granted_for_institution_inheritance_type.additional_properties = d
        return v2_credentials_role_granted_for_institution_inheritance_type

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
