from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.query_criteria_invoice_type_subject_type import QueryCriteriaInvoiceTypeSubjectType
import datetime
from typing import cast
from dateutil.parser import isoparse






T = TypeVar("T", bound="QueryCriteriaInvoiceIncrementalType")


@_attrs_define
class QueryCriteriaInvoiceIncrementalType:
    """ 
        Attributes:
            subject_type (QueryCriteriaInvoiceTypeSubjectType):
            type (str):
            acquisition_timestamp_threshold_from (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | minimum date range is
                2022-01-01
            acquisition_timestamp_threshold_to (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | maximum date range is current
                time (+ max 6 hours), the difference between date field and #acquisitionTimestampThresholdFrom cannot be greater
                than 24 months, date field cannot be before #acquisitionTimestampThresholdFrom
     """

    subject_type: QueryCriteriaInvoiceTypeSubjectType
    type: str
    acquisition_timestamp_threshold_from: datetime.datetime
    acquisition_timestamp_threshold_to: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type
        acquisition_timestamp_threshold_from = self.acquisition_timestamp_threshold_from.isoformat()

        acquisition_timestamp_threshold_to = self.acquisition_timestamp_threshold_to.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subjectType": subject_type,
            "type": type,
            "acquisitionTimestampThresholdFrom": acquisition_timestamp_threshold_from,
            "acquisitionTimestampThresholdTo": acquisition_timestamp_threshold_to,
        })

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
