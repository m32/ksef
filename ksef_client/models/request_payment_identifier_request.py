from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="RequestPaymentIdentifierRequest")


@attr.s(auto_attribs=True)
class RequestPaymentIdentifierRequest:
    """
    Attributes:
        ksef_reference_number_list (List[str]):
    """

    ksef_reference_number_list: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ksef_reference_number_list = self.ksef_reference_number_list

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ksefReferenceNumberList": ksef_reference_number_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ksef_reference_number_list = cast(List[str], d.pop("ksefReferenceNumberList"))

        request_payment_identifier_request = cls(
            ksef_reference_number_list=ksef_reference_number_list,
        )

        request_payment_identifier_request.additional_properties = d
        return request_payment_identifier_request

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
