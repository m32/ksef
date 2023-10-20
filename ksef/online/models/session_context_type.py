from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, List
from ..types import UNSET, Unset
from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.subject_complete_name_type import SubjectCompleteNameType
  from ..models.subject_identifier_by_type import SubjectIdentifierByType
  from ..models.credentials_role_response_base_type_object import CredentialsRoleResponseBaseTypeObject





T = TypeVar("T", bound="SessionContextType")


@_attrs_define
class SessionContextType:
    """ 
        Attributes:
            context_identifier (SubjectIdentifierByType):
            credentials_role_list (List['CredentialsRoleResponseBaseTypeObject']):
            context_name (Union[Unset, SubjectCompleteNameType]):
     """

    context_identifier: 'SubjectIdentifierByType'
    credentials_role_list: List['CredentialsRoleResponseBaseTypeObject']
    context_name: Union[Unset, 'SubjectCompleteNameType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_complete_name_type import SubjectCompleteNameType
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        from ..models.credentials_role_response_base_type_object import CredentialsRoleResponseBaseTypeObject
        context_identifier = self.context_identifier.to_dict()

        credentials_role_list = []
        for credentials_role_list_item_data in self.credentials_role_list:
            credentials_role_list_item = credentials_role_list_item_data.to_dict()

            credentials_role_list.append(credentials_role_list_item)




        context_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context_name, Unset):
            context_name = self.context_name.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextIdentifier": context_identifier,
            "credentialsRoleList": credentials_role_list,
        })
        if context_name is not UNSET:
            field_dict["contextName"] = context_name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_complete_name_type import SubjectCompleteNameType
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        from ..models.credentials_role_response_base_type_object import CredentialsRoleResponseBaseTypeObject
        d = src_dict.copy()
        context_identifier = SubjectIdentifierByType.from_dict(d.pop("contextIdentifier"))




        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList")
        for credentials_role_list_item_data in (_credentials_role_list):
            credentials_role_list_item = CredentialsRoleResponseBaseTypeObject.from_dict(credentials_role_list_item_data)



            credentials_role_list.append(credentials_role_list_item)


        _context_name = d.pop("contextName", UNSET)
        context_name: Union[Unset, SubjectCompleteNameType]
        if isinstance(_context_name,  Unset):
            context_name = UNSET
        else:
            context_name = SubjectCompleteNameType.from_dict(_context_name)




        session_context_type = cls(
            context_identifier=context_identifier,
            credentials_role_list=credentials_role_list,
            context_name=context_name,
        )

        session_context_type.additional_properties = d
        return session_context_type

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
