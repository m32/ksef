from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.hash_sha_type import HashSHAType





T = TypeVar("T", bound="File1MBHashType")


@_attrs_define
class File1MBHashType:
    """ 
        Attributes:
            file_size (int):
            hash_sha (HashSHAType):
     """

    file_size: int
    hash_sha: 'HashSHAType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.hash_sha_type import HashSHAType
        file_size = self.file_size
        hash_sha = self.hash_sha.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fileSize": file_size,
            "hashSHA": hash_sha,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hash_sha_type import HashSHAType
        d = src_dict.copy()
        file_size = d.pop("fileSize")

        hash_sha = HashSHAType.from_dict(d.pop("hashSHA"))




        file_1mb_hash_type = cls(
            file_size=file_size,
            hash_sha=hash_sha,
        )

        file_1mb_hash_type.additional_properties = d
        return file_1mb_hash_type

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
