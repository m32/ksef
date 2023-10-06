from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import File

T = TypeVar("T", bound="HashSHAType")


@attr.s(auto_attribs=True)
class HashSHAType:
    """
    Attributes:
        algorithm (str):
        encoding (str):
        value (File):
    """

    algorithm: str
    encoding: str
    value: File
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        algorithm = self.algorithm
        encoding = self.encoding
        value = self.value.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "encoding": encoding,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        algorithm = d.pop("algorithm")

        encoding = d.pop("encoding")

        value = File(payload=BytesIO(d.pop("value")))

        hash_sha_type = cls(
            algorithm=algorithm,
            encoding=encoding,
            value=value,
        )

        hash_sha_type.additional_properties = d
        return hash_sha_type

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
