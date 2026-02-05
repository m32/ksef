from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.online_session_effective_context_limits import OnlineSessionEffectiveContextLimits
  from ..models.batch_session_effective_context_limits import BatchSessionEffectiveContextLimits





T = TypeVar("T", bound="EffectiveContextLimits")



@_attrs_define
class EffectiveContextLimits:
    """ 
        Attributes:
            online_session (OnlineSessionEffectiveContextLimits):
            batch_session (BatchSessionEffectiveContextLimits):
     """

    online_session: 'OnlineSessionEffectiveContextLimits'
    batch_session: 'BatchSessionEffectiveContextLimits'





    def to_dict(self) -> dict[str, Any]:
        from ..models.online_session_effective_context_limits import OnlineSessionEffectiveContextLimits
        from ..models.batch_session_effective_context_limits import BatchSessionEffectiveContextLimits
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
        from ..models.online_session_effective_context_limits import OnlineSessionEffectiveContextLimits
        from ..models.batch_session_effective_context_limits import BatchSessionEffectiveContextLimits
        d = dict(src_dict)
        online_session = OnlineSessionEffectiveContextLimits.from_dict(d.pop("onlineSession"))




        batch_session = BatchSessionEffectiveContextLimits.from_dict(d.pop("batchSession"))




        effective_context_limits = cls(
            online_session=online_session,
            batch_session=batch_session,
        )

        return effective_context_limits

