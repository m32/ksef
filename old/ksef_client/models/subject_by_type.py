from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.subject_identifier_by_type import SubjectIdentifierByType
from ..models.subject_name_type import SubjectNameType

T = TypeVar("T", bound="SubjectByType")


@attr.s(auto_attribs=True)
class SubjectByType:
    """
    Attributes:
        issued_by_identifier (SubjectIdentifierByType):
        issued_by_name (SubjectNameType):
    """

    issued_by_identifier: SubjectIdentifierByType
    issued_by_name: SubjectNameType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issued_by_identifier = self.issued_by_identifier.to_dict()

        issued_by_name = self.issued_by_name.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuedByIdentifier": issued_by_identifier,
                "issuedByName": issued_by_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issued_by_identifier = SubjectIdentifierByType.from_dict(d.pop("issuedByIdentifier"))

        issued_by_name = SubjectNameType.from_dict(d.pop("issuedByName"))

        subject_by_type = cls(
            issued_by_identifier=issued_by_identifier,
            issued_by_name=issued_by_name,
        )

        subject_by_type.additional_properties = d
        return subject_by_type

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
