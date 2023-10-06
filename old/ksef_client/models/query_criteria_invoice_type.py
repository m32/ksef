from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_criteria_invoice_type_subject_type import QueryCriteriaInvoiceTypeSubjectType

T = TypeVar("T", bound="QueryCriteriaInvoiceType")


@attr.s(auto_attribs=True)
class QueryCriteriaInvoiceType:
    """
    Attributes:
        subject_type (QueryCriteriaInvoiceTypeSubjectType):
        type (str):
    """

    subject_type: QueryCriteriaInvoiceTypeSubjectType
    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subjectType": subject_type,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_type = QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))

        type = d.pop("type")

        query_criteria_invoice_type = cls(
            subject_type=subject_type,
            type=type,
        )

        query_criteria_invoice_type.additional_properties = d
        return query_criteria_invoice_type

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
