from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.subject_identifier_by_type import SubjectIdentifierByType





T = TypeVar("T", bound="AuthorisationChallengeRequest")


@_attrs_define
class AuthorisationChallengeRequest:
    """ 
        Attributes:
            context_identifier (SubjectIdentifierByType):
     """

    context_identifier: 'SubjectIdentifierByType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        context_identifier = self.context_identifier.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextIdentifier": context_identifier,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        d = src_dict.copy()
        context_identifier = SubjectIdentifierByType.from_dict(d.pop("contextIdentifier"))




        authorisation_challenge_request = cls(
            context_identifier=context_identifier,
        )

        authorisation_challenge_request.additional_properties = d
        return authorisation_challenge_request

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
