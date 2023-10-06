from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import cast
from ..models.subject_authorized_type_subject_authorized_type import SubjectAuthorizedTypeSubjectAuthorizedType
from typing import Dict

if TYPE_CHECKING:
  from ..models.subject_name_type import SubjectNameType
  from ..models.subject_identifier_to_type import SubjectIdentifierToType





T = TypeVar("T", bound="SubjectAuthorizedType")


@_attrs_define
class SubjectAuthorizedType:
    """ 
        Attributes:
            issued_to_identifier (SubjectIdentifierToType):
            subject_authorized_type (SubjectAuthorizedTypeSubjectAuthorizedType):
            issued_to_name (Union[Unset, SubjectNameType]):
     """

    issued_to_identifier: 'SubjectIdentifierToType'
    subject_authorized_type: SubjectAuthorizedTypeSubjectAuthorizedType
    issued_to_name: Union[Unset, 'SubjectNameType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_name_type import SubjectNameType
        from ..models.subject_identifier_to_type import SubjectIdentifierToType
        issued_to_identifier = self.issued_to_identifier.to_dict()

        subject_authorized_type = self.subject_authorized_type.value

        issued_to_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issued_to_name, Unset):
            issued_to_name = self.issued_to_name.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "issuedToIdentifier": issued_to_identifier,
            "subjectAuthorizedType": subject_authorized_type,
        })
        if issued_to_name is not UNSET:
            field_dict["issuedToName"] = issued_to_name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_name_type import SubjectNameType
        from ..models.subject_identifier_to_type import SubjectIdentifierToType
        d = src_dict.copy()
        issued_to_identifier = SubjectIdentifierToType.from_dict(d.pop("issuedToIdentifier"))




        subject_authorized_type = SubjectAuthorizedTypeSubjectAuthorizedType(d.pop("subjectAuthorizedType"))




        _issued_to_name = d.pop("issuedToName", UNSET)
        issued_to_name: Union[Unset, SubjectNameType]
        if isinstance(_issued_to_name,  Unset):
            issued_to_name = UNSET
        else:
            issued_to_name = SubjectNameType.from_dict(_issued_to_name)




        subject_authorized_type = cls(
            issued_to_identifier=issued_to_identifier,
            subject_authorized_type=subject_authorized_type,
            issued_to_name=issued_to_name,
        )

        subject_authorized_type.additional_properties = d
        return subject_authorized_type

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
