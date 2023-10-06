import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.query_criteria_invoice_type_subject_type import QueryCriteriaInvoiceTypeSubjectType

T = TypeVar("T", bound="QueryCriteriaInvoiceIncrementalType")


@attr.s(auto_attribs=True)
class QueryCriteriaInvoiceIncrementalType:
    """
    Attributes:
        subject_type (QueryCriteriaInvoiceTypeSubjectType):
        type (str):
        acquisition_timestamp_threshold_from (datetime.datetime):
        acquisition_timestamp_threshold_to (datetime.datetime):
    """

    subject_type: QueryCriteriaInvoiceTypeSubjectType
    type: str
    acquisition_timestamp_threshold_from: datetime.datetime
    acquisition_timestamp_threshold_to: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type
        acquisition_timestamp_threshold_from = self.acquisition_timestamp_threshold_from.isoformat()

        acquisition_timestamp_threshold_to = self.acquisition_timestamp_threshold_to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subjectType": subject_type,
                "type": type,
                "acquisitionTimestampThresholdFrom": acquisition_timestamp_threshold_from,
                "acquisitionTimestampThresholdTo": acquisition_timestamp_threshold_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_type = QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))

        type = d.pop("type")

        acquisition_timestamp_threshold_from = isoparse(d.pop("acquisitionTimestampThresholdFrom"))

        acquisition_timestamp_threshold_to = isoparse(d.pop("acquisitionTimestampThresholdTo"))

        query_criteria_invoice_incremental_type = cls(
            subject_type=subject_type,
            type=type,
            acquisition_timestamp_threshold_from=acquisition_timestamp_threshold_from,
            acquisition_timestamp_threshold_to=acquisition_timestamp_threshold_to,
        )

        query_criteria_invoice_incremental_type.additional_properties = d
        return query_criteria_invoice_incremental_type

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
