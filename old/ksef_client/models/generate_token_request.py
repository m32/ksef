from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.generate_token_request_type import GenerateTokenRequestType

T = TypeVar("T", bound="GenerateTokenRequest")


@attr.s(auto_attribs=True)
class GenerateTokenRequest:
    """
    Attributes:
        generate_token (GenerateTokenRequestType):
    """

    generate_token: GenerateTokenRequestType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generate_token = self.generate_token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generateToken": generate_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        generate_token = GenerateTokenRequestType.from_dict(d.pop("generateToken"))

        generate_token_request = cls(
            generate_token=generate_token,
        )

        generate_token_request.additional_properties = d
        return generate_token_request

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
