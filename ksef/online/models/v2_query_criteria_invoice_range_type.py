from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.v2_query_criteria_invoice_type_subject_type import V2QueryCriteriaInvoiceTypeSubjectType
from typing import cast
import datetime
from dateutil.parser import isoparse






T = TypeVar("T", bound="V2QueryCriteriaInvoiceRangeType")


@_attrs_define
class V2QueryCriteriaInvoiceRangeType:
    """ 
        Attributes:
            subject_type (V2QueryCriteriaInvoiceTypeSubjectType):
            type (str):
            invoicing_date_from (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | minimum date range is 2022-01-01
            invoicing_date_to (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | maximum date range is current time (+ max 6
                hours), the difference between date field and #invoicingDateFrom cannot be greater than 24 months, date field
                cannot be before #invoicingDateFrom
     """

    subject_type: V2QueryCriteriaInvoiceTypeSubjectType
    type: str
    invoicing_date_from: datetime.datetime
    invoicing_date_to: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type
        invoicing_date_from = self.invoicing_date_from.isoformat()

        invoicing_date_to = self.invoicing_date_to.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subjectType": subject_type,
            "type": type,
            "invoicingDateFrom": invoicing_date_from,
            "invoicingDateTo": invoicing_date_to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_type = V2QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))




        type = d.pop("type")

        invoicing_date_from = isoparse(d.pop("invoicingDateFrom"))




        invoicing_date_to = isoparse(d.pop("invoicingDateTo"))




        v2_query_criteria_invoice_range_type = cls(
            subject_type=subject_type,
            type=type,
            invoicing_date_from=invoicing_date_from,
            invoicing_date_to=invoicing_date_to,
        )

        v2_query_criteria_invoice_range_type.additional_properties = d
        return v2_query_criteria_invoice_range_type

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
