from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_criteria_invoice_type import QueryCriteriaInvoiceType

T = TypeVar("T", bound="QueryInvoiceRequest")


@attr.s(auto_attribs=True)
class QueryInvoiceRequest:
    """
    Attributes:
        query_criteria (QueryCriteriaInvoiceType):
    """

    query_criteria: QueryCriteriaInvoiceType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_criteria = self.query_criteria.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queryCriteria": query_criteria,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query_criteria = QueryCriteriaInvoiceType.from_dict(d.pop("queryCriteria"))

        query_invoice_request = cls(
            query_criteria=query_criteria,
        )

        query_invoice_request.additional_properties = d
        return query_invoice_request

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
