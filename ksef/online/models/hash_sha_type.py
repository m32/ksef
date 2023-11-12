from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from io import BytesIO






T = TypeVar("T", bound="HashSHAType")


@_attrs_define
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
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        algorithm = self.algorithm
        encoding = self.encoding
        value = self.value.to_tuple()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "algorithm": algorithm,
            "encoding": encoding,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        algorithm = d.pop("algorithm")

        encoding = d.pop("encoding")

        value = File(
             payload = BytesIO(d.pop("value").encode())
        )




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
