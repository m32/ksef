from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
import datetime
from typing import cast
from dateutil.parser import isoparse

if TYPE_CHECKING:
  from ..models.initialised_session_type import InitialisedSessionType





T = TypeVar("T", bound="InitSessionResponse")


@_attrs_define
class InitSessionResponse:
    """ 
        Attributes:
            reference_number (str):
            session_token (InitialisedSessionType):
            timestamp (datetime.datetime):
     """

    reference_number: str
    session_token: 'InitialisedSessionType'
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.initialised_session_type import InitialisedSessionType
        reference_number = self.reference_number
        session_token = self.session_token.to_dict()

        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "referenceNumber": reference_number,
            "sessionToken": session_token,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.initialised_session_type import InitialisedSessionType
        d = src_dict.copy()
        reference_number = d.pop("referenceNumber")

        session_token = InitialisedSessionType.from_dict(d.pop("sessionToken"))




        timestamp = isoparse(d.pop("timestamp"))




        init_session_response = cls(
            reference_number=reference_number,
            session_token=session_token,
            timestamp=timestamp,
        )

        init_session_response.additional_properties = d
        return init_session_response

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
