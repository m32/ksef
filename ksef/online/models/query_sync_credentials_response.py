from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import Dict
import datetime
from typing import cast, List
from typing import cast

if TYPE_CHECKING:
  from ..models.credentials_base_type_object_object import CredentialsBaseTypeObjectObject





T = TypeVar("T", bound="QuerySyncCredentialsResponse")


@_attrs_define
class QuerySyncCredentialsResponse:
    """ 
        Attributes:
            credentials_list (List['CredentialsBaseTypeObjectObject']):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    credentials_list: List['CredentialsBaseTypeObjectObject']
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_base_type_object_object import CredentialsBaseTypeObjectObject
        credentials_list = []
        for credentials_list_item_data in self.credentials_list:
            credentials_list_item = credentials_list_item_data.to_dict()

            credentials_list.append(credentials_list_item)




        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credentialsList": credentials_list,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_base_type_object_object import CredentialsBaseTypeObjectObject
        d = src_dict.copy()
        credentials_list = []
        _credentials_list = d.pop("credentialsList")
        for credentials_list_item_data in (_credentials_list):
            credentials_list_item = CredentialsBaseTypeObjectObject.from_dict(credentials_list_item_data)



            credentials_list.append(credentials_list_item)


        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        query_sync_credentials_response = cls(
            credentials_list=credentials_list,
            reference_number=reference_number,
            timestamp=timestamp,
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
