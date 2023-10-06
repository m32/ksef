from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.hash_sha_type import HashSHAType

T = TypeVar("T", bound="FileUnlimitedHashType")


@attr.s(auto_attribs=True)
class FileUnlimitedHashType:
    """
    Attributes:
        hash_sha (HashSHAType):
        file_size (int):
    """

    hash_sha: HashSHAType
    file_size: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hash_sha = self.hash_sha.to_dict()

        file_size = self.file_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hashSHA": hash_sha,
                "fileSize": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hash_sha = HashSHAType.from_dict(d.pop("hashSHA"))

        file_size = d.pop("fileSize")

        file_unlimited_hash_type = cls(
            hash_sha=hash_sha,
            file_size=file_size,
        )

        file_unlimited_hash_type.additional_properties = d
        return file_unlimited_hash_type

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
