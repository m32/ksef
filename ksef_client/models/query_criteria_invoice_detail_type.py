import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.query_criteria_invoice_type_subject_type import QueryCriteriaInvoiceTypeSubjectType
from ..models.subject_by_type import SubjectByType
from ..models.subject_to_type import SubjectToType
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryCriteriaInvoiceDetailType")


@attr.s(auto_attribs=True)
class QueryCriteriaInvoiceDetailType:
    """
    Attributes:
        subject_type (QueryCriteriaInvoiceTypeSubjectType):
        type (str):
        invoicing_date_from (datetime.datetime):
        invoicing_date_to (datetime.datetime):
        invoice_number (Union[Unset, str]):
        ksef_reference_number (Union[Unset, str]):
        subject_by (Union[Unset, SubjectByType]):
        subject_to (Union[Unset, SubjectToType]):
    """

    subject_type: QueryCriteriaInvoiceTypeSubjectType
    type: str
    invoicing_date_from: datetime.datetime
    invoicing_date_to: datetime.datetime
    invoice_number: Union[Unset, str] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    subject_by: Union[Unset, SubjectByType] = UNSET
    subject_to: Union[Unset, SubjectToType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type
        invoicing_date_from = self.invoicing_date_from.isoformat()

        invoicing_date_to = self.invoicing_date_to.isoformat()

        invoice_number = self.invoice_number
        ksef_reference_number = self.ksef_reference_number
        subject_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_by, Unset):
            subject_by = self.subject_by.to_dict()

        subject_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_to, Unset):
            subject_to = self.subject_to.to_dict()

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
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if ksef_reference_number is not UNSET:
            field_dict["ksefReferenceNumber"] = ksef_reference_number
        if subject_by is not UNSET:
            field_dict["subjectBy"] = subject_by
        if subject_to is not UNSET:
            field_dict["subjectTo"] = subject_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_type = QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))

        type = d.pop("type")

        invoicing_date_from = isoparse(d.pop("invoicingDateFrom"))

        invoicing_date_to = isoparse(d.pop("invoicingDateTo"))

        invoice_number = d.pop("invoiceNumber", UNSET)

        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        _subject_by = d.pop("subjectBy", UNSET)
        subject_by: Union[Unset, SubjectByType]
        if isinstance(_subject_by, Unset):
            subject_by = UNSET
        else:
            subject_by = SubjectByType.from_dict(_subject_by)

        _subject_to = d.pop("subjectTo", UNSET)
        subject_to: Union[Unset, SubjectToType]
        if isinstance(_subject_to, Unset):
            subject_to = UNSET
        else:
            subject_to = SubjectToType.from_dict(_subject_to)

        query_criteria_invoice_detail_type = cls(
            subject_type=subject_type,
            type=type,
            invoicing_date_from=invoicing_date_from,
            invoicing_date_to=invoicing_date_to,
            invoice_number=invoice_number,
            ksef_reference_number=ksef_reference_number,
            subject_by=subject_by,
            subject_to=subject_to,
        )

        query_criteria_invoice_detail_type.additional_properties = d
        return query_criteria_invoice_detail_type

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
