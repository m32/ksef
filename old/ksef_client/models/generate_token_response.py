import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="GenerateTokenResponse")


@attr.s(auto_attribs=True)
class GenerateTokenResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        processing_code (int):
        processing_description (str):
        element_reference_number (str):
        authorisation_token (str):
    """

    timestamp: datetime.datetime
    reference_number: str
    processing_code: int
    processing_description: str
    element_reference_number: str
    authorisation_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        processing_code = self.processing_code
        processing_description = self.processing_description
        element_reference_number = self.element_reference_number
        authorisation_token = self.authorisation_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "processingCode": processing_code,
                "processingDescription": processing_description,
                "elementReferenceNumber": element_reference_number,
                "authorisationToken": authorisation_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        element_reference_number = d.pop("elementReferenceNumber")

        authorisation_token = d.pop("authorisationToken")

        generate_token_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            processing_code=processing_code,
            processing_description=processing_description,
            element_reference_number=element_reference_number,
            authorisation_token=authorisation_token,
        )

        generate_token_response.additional_properties = d
        return generate_token_response

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
