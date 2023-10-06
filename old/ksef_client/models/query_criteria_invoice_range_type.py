import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.query_criteria_invoice_type_subject_type import QueryCriteriaInvoiceTypeSubjectType

T = TypeVar("T", bound="QueryCriteriaInvoiceRangeType")


@attr.s(auto_attribs=True)
class QueryCriteriaInvoiceRangeType:
    """
    Attributes:
        subject_type (QueryCriteriaInvoiceTypeSubjectType):
        type (str):
        invoicing_date_from (datetime.datetime):
        invoicing_date_to (datetime.datetime):
    """

    subject_type: QueryCriteriaInvoiceTypeSubjectType
    type: str
    invoicing_date_from: datetime.datetime
    invoicing_date_to: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type
        invoicing_date_from = self.invoicing_date_from.isoformat()

        invoicing_date_to = self.invoicing_date_to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subjectType": subject_type,
                "type": type,
                "invoicingDateFrom": invoicing_date_from,
                "invoicingDateTo": invoicing_date_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_type = QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))

        type = d.pop("type")

        invoicing_date_from = isoparse(d.pop("invoicingDateFrom"))

        invoicing_date_to = isoparse(d.pop("invoicingDateTo"))

        query_criteria_invoice_range_type = cls(
            subject_type=subject_type,
            type=type,
            invoicing_date_from=invoicing_date_from,
            invoicing_date_to=invoicing_date_to,
        )

        query_criteria_invoice_range_type.additional_properties = d
        return query_criteria_invoice_range_type

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
