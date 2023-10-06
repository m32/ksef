import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.initialised_session_type import InitialisedSessionType

T = TypeVar("T", bound="InitSessionResponse")


@attr.s(auto_attribs=True)
class InitSessionResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        session_token (InitialisedSessionType):
    """

    timestamp: datetime.datetime
    reference_number: str
    session_token: InitialisedSessionType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        session_token = self.session_token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "sessionToken": session_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        session_token = InitialisedSessionType.from_dict(d.pop("sessionToken"))

        init_session_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            session_token=session_token,
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
