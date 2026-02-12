from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.online_session_context_limits_override import OnlineSessionContextLimitsOverride
  from ..models.batch_session_context_limits_override import BatchSessionContextLimitsOverride





T = TypeVar("T", bound="SetSessionLimitsRequest")



@_attrs_define
class SetSessionLimitsRequest:
    """ 
        Attributes:
            online_session (OnlineSessionContextLimitsOverride):
            batch_session (BatchSessionContextLimitsOverride):
     """

    online_session: 'OnlineSessionContextLimitsOverride'
    batch_session: 'BatchSessionContextLimitsOverride'





    def to_dict(self) -> dict[str, Any]:
        from ..models.online_session_context_limits_override import OnlineSessionContextLimitsOverride
        from ..models.batch_session_context_limits_override import BatchSessionContextLimitsOverride
        online_session = self.online_session.to_dict()

        batch_session = self.batch_session.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "onlineSession": online_session,
            "batchSession": batch_session,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.online_session_context_limits_override import OnlineSessionContextLimitsOverride
        from ..models.batch_session_context_limits_override import BatchSessionContextLimitsOverride
        d = dict(src_dict)
        online_session = OnlineSessionContextLimitsOverride.from_dict(d.pop("onlineSession"))




        batch_session = BatchSessionContextLimitsOverride.from_dict(d.pop("batchSession"))




        set_session_limits_request = cls(
            online_session=online_session,
            batch_session=batch_session,
        )

        return set_session_limits_request

