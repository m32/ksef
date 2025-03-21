from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from typing import cast






T = TypeVar("T", bound="InternalIdentifierGeneratedResponse")


@_attrs_define
class InternalIdentifierGeneratedResponse:
    """ 
        Attributes:
            internal_identifier (str):
            timestamp (datetime.datetime):
     """

    internal_identifier: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        internal_identifier = self.internal_identifier
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "internalIdentifier": internal_identifier,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        internal_identifier = d.pop("internalIdentifier")

        timestamp = isoparse(d.pop("timestamp"))




        internal_identifier_generated_response = cls(
            internal_identifier=internal_identifier,
            timestamp=timestamp,
        )

        internal_identifier_generated_response.additional_properties = d
        return internal_identifier_generated_response

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
