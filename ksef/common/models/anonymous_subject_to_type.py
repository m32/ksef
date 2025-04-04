from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.anonymous_subject_identifier_to_type import AnonymousSubjectIdentifierToType
  from ..models.subject_name_type import SubjectNameType





T = TypeVar("T", bound="AnonymousSubjectToType")


@_attrs_define
class AnonymousSubjectToType:
    """ 
        Attributes:
            issued_to_identifier (AnonymousSubjectIdentifierToType):
            issued_to_name (SubjectNameType):
     """

    issued_to_identifier: 'AnonymousSubjectIdentifierToType'
    issued_to_name: 'SubjectNameType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.anonymous_subject_identifier_to_type import AnonymousSubjectIdentifierToType
        from ..models.subject_name_type import SubjectNameType
        issued_to_identifier = self.issued_to_identifier.to_dict()

        issued_to_name = self.issued_to_name.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "issuedToIdentifier": issued_to_identifier,
            "issuedToName": issued_to_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.anonymous_subject_identifier_to_type import AnonymousSubjectIdentifierToType
        from ..models.subject_name_type import SubjectNameType
        d = src_dict.copy()
        issued_to_identifier = AnonymousSubjectIdentifierToType.from_dict(d.pop("issuedToIdentifier"))




        issued_to_name = SubjectNameType.from_dict(d.pop("issuedToName"))




        anonymous_subject_to_type = cls(
            issued_to_identifier=issued_to_identifier,
            issued_to_name=issued_to_name,
        )

        anonymous_subject_to_type.additional_properties = d
        return anonymous_subject_to_type

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
