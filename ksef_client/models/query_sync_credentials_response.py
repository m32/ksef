import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.credentials_base_type_object import CredentialsBaseTypeObject

T = TypeVar("T", bound="QuerySyncCredentialsResponse")


@attr.s(auto_attribs=True)
class QuerySyncCredentialsResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        credentials_list (List[CredentialsBaseTypeObject]):
    """

    timestamp: datetime.datetime
    reference_number: str
    credentials_list: List[CredentialsBaseTypeObject]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        credentials_list = []
        for credentials_list_item_data in self.credentials_list:
            credentials_list_item = credentials_list_item_data.to_dict()

            credentials_list.append(credentials_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "credentialsList": credentials_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        credentials_list = []
        _credentials_list = d.pop("credentialsList")
        for credentials_list_item_data in _credentials_list:
            credentials_list_item = CredentialsBaseTypeObject.from_dict(credentials_list_item_data)

            credentials_list.append(credentials_list_item)

        query_sync_credentials_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            credentials_list=credentials_list,
        )

        query_sync_credentials_response.additional_properties = d
        return query_sync_credentials_response

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
