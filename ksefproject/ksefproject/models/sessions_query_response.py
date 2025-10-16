from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.sessions_query_response_item import SessionsQueryResponseItem





T = TypeVar("T", bound="SessionsQueryResponse")



@_attrs_define
class SessionsQueryResponse:
    """ 
        Attributes:
            sessions (list['SessionsQueryResponseItem']): Lista sesji.
            continuation_token (Union[None, Unset, str]): Token służący do pobrania kolejnej strony wyników. Jeśli jest
                pusty, to nie ma kolejnych stron.
     """

    sessions: list['SessionsQueryResponseItem']
    continuation_token: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.sessions_query_response_item import SessionsQueryResponseItem
        sessions = []
        for sessions_item_data in self.sessions:
            sessions_item = sessions_item_data.to_dict()
            sessions.append(sessions_item)



        continuation_token: Union[None, Unset, str]
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "sessions": sessions,
        })
        if continuation_token is not UNSET:
            field_dict["continuationToken"] = continuation_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sessions_query_response_item import SessionsQueryResponseItem
        d = dict(src_dict)
        sessions = []
        _sessions = d.pop("sessions")
        for sessions_item_data in (_sessions):
            sessions_item = SessionsQueryResponseItem.from_dict(sessions_item_data)



            sessions.append(sessions_item)


        def _parse_continuation_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        continuation_token = _parse_continuation_token(d.pop("continuationToken", UNSET))


        sessions_query_response = cls(
            sessions=sessions,
            continuation_token=continuation_token,
        )

        return sessions_query_response

