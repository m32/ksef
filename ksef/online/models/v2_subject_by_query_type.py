from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from ..types import UNSET, Unset
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.subject_name_type import SubjectNameType
  from ..models.subject_identifier_by_type import SubjectIdentifierByType





T = TypeVar("T", bound="V2SubjectByQueryType")


@_attrs_define
class V2SubjectByQueryType:
    """ 
        Attributes:
            issued_by_identifier (SubjectIdentifierByType):
            issued_by_name (Union[Unset, SubjectNameType]):
     """

    issued_by_identifier: 'SubjectIdentifierByType'
    issued_by_name: Union[Unset, 'SubjectNameType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_name_type import SubjectNameType
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        issued_by_identifier = self.issued_by_identifier.to_dict()

        issued_by_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issued_by_name, Unset):
            issued_by_name = self.issued_by_name.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "issuedByIdentifier": issued_by_identifier,
        })
        if issued_by_name is not UNSET:
            field_dict["issuedByName"] = issued_by_name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_name_type import SubjectNameType
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        d = src_dict.copy()
        issued_by_identifier = SubjectIdentifierByType.from_dict(d.pop("issuedByIdentifier"))




        _issued_by_name = d.pop("issuedByName", UNSET)
        issued_by_name: Union[Unset, SubjectNameType]
        if isinstance(_issued_by_name,  Unset):
            issued_by_name = UNSET
        else:
            issued_by_name = SubjectNameType.from_dict(_issued_by_name)




        v2_subject_by_query_type = cls(
            issued_by_identifier=issued_by_identifier,
            issued_by_name=issued_by_name,
        )

        v2_subject_by_query_type.additional_properties = d
        return v2_subject_by_query_type

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
