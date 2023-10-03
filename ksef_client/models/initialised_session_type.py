from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.session_context_type import SessionContextType

T = TypeVar("T", bound="InitialisedSessionType")


@attr.s(auto_attribs=True)
class InitialisedSessionType:
    """
    Attributes:
        token (str):
        context (SessionContextType):
    """

    token: str
    context: SessionContextType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        context = self.context.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "context": context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        context = SessionContextType.from_dict(d.pop("context"))

        initialised_session_type = cls(
            token=token,
            context=context,
        )

        initialised_session_type.additional_properties = d
        return initialised_session_type

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
