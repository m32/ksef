from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from typing import Union
from dateutil.parser import isoparse
import datetime
from typing import cast, List
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.access_points_provider_type import AccessPointsProviderType





T = TypeVar("T", bound="AccessPointsProvidersListResponse")


@_attrs_define
class AccessPointsProvidersListResponse:
    """ 
        Attributes:
            number_of_elements (int):
            page_offset (int):
            page_size (int):
            reference_number (str):
            timestamp (datetime.datetime):
            access_points_provider_list (Union[Unset, List['AccessPointsProviderType']]):
     """

    number_of_elements: int
    page_offset: int
    page_size: int
    reference_number: str
    timestamp: datetime.datetime
    access_points_provider_list: Union[Unset, List['AccessPointsProviderType']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.access_points_provider_type import AccessPointsProviderType
        number_of_elements = self.number_of_elements
        page_offset = self.page_offset
        page_size = self.page_size
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()

        access_points_provider_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access_points_provider_list, Unset):
            access_points_provider_list = []
            for access_points_provider_list_item_data in self.access_points_provider_list:
                access_points_provider_list_item = access_points_provider_list_item_data.to_dict()

                access_points_provider_list.append(access_points_provider_list_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "numberOfElements": number_of_elements,
            "pageOffset": page_offset,
            "pageSize": page_size,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })
        if access_points_provider_list is not UNSET:
            field_dict["accessPointsProviderList"] = access_points_provider_list

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_points_provider_type import AccessPointsProviderType
        d = src_dict.copy()
        number_of_elements = d.pop("numberOfElements")

        page_offset = d.pop("pageOffset")

        page_size = d.pop("pageSize")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        access_points_provider_list = []
        _access_points_provider_list = d.pop("accessPointsProviderList", UNSET)
        for access_points_provider_list_item_data in (_access_points_provider_list or []):
            access_points_provider_list_item = AccessPointsProviderType.from_dict(access_points_provider_list_item_data)



            access_points_provider_list.append(access_points_provider_list_item)


        access_points_providers_list_response = cls(
            number_of_elements=number_of_elements,
            page_offset=page_offset,
            page_size=page_size,
            reference_number=reference_number,
            timestamp=timestamp,
            access_points_provider_list=access_points_provider_list,
        )

        access_points_providers_list_response.additional_properties = d
        return access_points_providers_list_response

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
