from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import Dict
import datetime
from ..models.v2_query_criteria_invoice_detail_type_currency_codes_item import V2QueryCriteriaInvoiceDetailTypeCurrencyCodesItem
from ..models.v2_query_criteria_invoice_detail_type_amount_type import V2QueryCriteriaInvoiceDetailTypeAmountType
from ..models.v2_query_criteria_invoice_detail_type_invoice_types_item import V2QueryCriteriaInvoiceDetailTypeInvoiceTypesItem
from ..types import UNSET, Unset
from typing import cast, List
from typing import Union
from typing import cast
from ..models.v2_query_criteria_invoice_type_subject_type import V2QueryCriteriaInvoiceTypeSubjectType

if TYPE_CHECKING:
  from ..models.v2_subject_by_query_type import V2SubjectByQueryType
  from ..models.v2_subject_to_query_type import V2SubjectToQueryType





T = TypeVar("T", bound="V2QueryCriteriaInvoiceDetailType")


@_attrs_define
class V2QueryCriteriaInvoiceDetailType:
    """ 
        Attributes:
            subject_type (V2QueryCriteriaInvoiceTypeSubjectType):
            type (str):
            invoicing_date_from (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | minimum date range is 2022-01-01
            invoicing_date_to (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | maximum date range is current time (+ max 6
                hours), the difference between date field and #invoicingDateFrom cannot be greater than 24 months, date field
                cannot be before #invoicingDateFrom
            amount_from (Union[Unset, float]):
            amount_to (Union[Unset, float]):
            amount_type (Union[Unset, V2QueryCriteriaInvoiceDetailTypeAmountType]):
            currency_codes (Union[Unset, List[V2QueryCriteriaInvoiceDetailTypeCurrencyCodesItem]]):
            fa_p17_annotation (Union[Unset, bool]):
            invoice_number (Union[Unset, str]):
            invoice_types (Union[Unset, List[V2QueryCriteriaInvoiceDetailTypeInvoiceTypesItem]]):
            ksef_reference_number (Union[Unset, str]):
            subject_by (Union[Unset, V2SubjectByQueryType]):
            subject_to (Union[Unset, V2SubjectToQueryType]):
     """

    subject_type: V2QueryCriteriaInvoiceTypeSubjectType
    type: str
    invoicing_date_from: datetime.datetime
    invoicing_date_to: datetime.datetime
    amount_from: Union[Unset, float] = UNSET
    amount_to: Union[Unset, float] = UNSET
    amount_type: Union[Unset, V2QueryCriteriaInvoiceDetailTypeAmountType] = UNSET
    currency_codes: Union[Unset, List[V2QueryCriteriaInvoiceDetailTypeCurrencyCodesItem]] = UNSET
    fa_p17_annotation: Union[Unset, bool] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    invoice_types: Union[Unset, List[V2QueryCriteriaInvoiceDetailTypeInvoiceTypesItem]] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    subject_by: Union[Unset, 'V2SubjectByQueryType'] = UNSET
    subject_to: Union[Unset, 'V2SubjectToQueryType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.v2_subject_by_query_type import V2SubjectByQueryType
        from ..models.v2_subject_to_query_type import V2SubjectToQueryType
        subject_type = self.subject_type.value

        type = self.type
        invoicing_date_from = self.invoicing_date_from.isoformat()

        invoicing_date_to = self.invoicing_date_to.isoformat()

        amount_from = self.amount_from
        amount_to = self.amount_to
        amount_type: Union[Unset, str] = UNSET
        if not isinstance(self.amount_type, Unset):
            amount_type = self.amount_type.value

        currency_codes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.currency_codes, Unset):
            currency_codes = []
            for currency_codes_item_data in self.currency_codes:
                currency_codes_item = currency_codes_item_data.value

                currency_codes.append(currency_codes_item)




        fa_p17_annotation = self.fa_p17_annotation
        invoice_number = self.invoice_number
        invoice_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.invoice_types, Unset):
            invoice_types = []
            for invoice_types_item_data in self.invoice_types:
                invoice_types_item = invoice_types_item_data.value

                invoice_types.append(invoice_types_item)




        ksef_reference_number = self.ksef_reference_number
        subject_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_by, Unset):
            subject_by = self.subject_by.to_dict()

        subject_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_to, Unset):
            subject_to = self.subject_to.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subjectType": subject_type,
            "type": type,
            "invoicingDateFrom": invoicing_date_from,
            "invoicingDateTo": invoicing_date_to,
        })
        if amount_from is not UNSET:
            field_dict["amountFrom"] = amount_from
        if amount_to is not UNSET:
            field_dict["amountTo"] = amount_to
        if amount_type is not UNSET:
            field_dict["amountType"] = amount_type
        if currency_codes is not UNSET:
            field_dict["currencyCodes"] = currency_codes
        if fa_p17_annotation is not UNSET:
            field_dict["faP17Annotation"] = fa_p17_annotation
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if invoice_types is not UNSET:
            field_dict["invoiceTypes"] = invoice_types
        if ksef_reference_number is not UNSET:
            field_dict["ksefReferenceNumber"] = ksef_reference_number
        if subject_by is not UNSET:
            field_dict["subjectBy"] = subject_by
        if subject_to is not UNSET:
            field_dict["subjectTo"] = subject_to

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v2_subject_by_query_type import V2SubjectByQueryType
        from ..models.v2_subject_to_query_type import V2SubjectToQueryType
        d = src_dict.copy()
        subject_type = V2QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))




        type = d.pop("type")

        invoicing_date_from = isoparse(d.pop("invoicingDateFrom"))




        invoicing_date_to = isoparse(d.pop("invoicingDateTo"))




        amount_from = d.pop("amountFrom", UNSET)

        amount_to = d.pop("amountTo", UNSET)

        _amount_type = d.pop("amountType", UNSET)
        amount_type: Union[Unset, V2QueryCriteriaInvoiceDetailTypeAmountType]
        if isinstance(_amount_type,  Unset):
            amount_type = UNSET
        else:
            amount_type = V2QueryCriteriaInvoiceDetailTypeAmountType(_amount_type)




        currency_codes = []
        _currency_codes = d.pop("currencyCodes", UNSET)
        for currency_codes_item_data in (_currency_codes or []):
            currency_codes_item = V2QueryCriteriaInvoiceDetailTypeCurrencyCodesItem(currency_codes_item_data)



            currency_codes.append(currency_codes_item)


        fa_p17_annotation = d.pop("faP17Annotation", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        invoice_types = []
        _invoice_types = d.pop("invoiceTypes", UNSET)
        for invoice_types_item_data in (_invoice_types or []):
            invoice_types_item = V2QueryCriteriaInvoiceDetailTypeInvoiceTypesItem(invoice_types_item_data)



            invoice_types.append(invoice_types_item)


        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        _subject_by = d.pop("subjectBy", UNSET)
        subject_by: Union[Unset, V2SubjectByQueryType]
        if isinstance(_subject_by,  Unset):
            subject_by = UNSET
        else:
            subject_by = V2SubjectByQueryType.from_dict(_subject_by)




        _subject_to = d.pop("subjectTo", UNSET)
        subject_to: Union[Unset, V2SubjectToQueryType]
        if isinstance(_subject_to,  Unset):
            subject_to = UNSET
        else:
            subject_to = V2SubjectToQueryType.from_dict(_subject_to)




        v2_query_criteria_invoice_detail_type = cls(
            subject_type=subject_type,
            type=type,
            invoicing_date_from=invoicing_date_from,
            invoicing_date_to=invoicing_date_to,
            amount_from=amount_from,
            amount_to=amount_to,
            amount_type=amount_type,
            currency_codes=currency_codes,
            fa_p17_annotation=fa_p17_annotation,
            invoice_number=invoice_number,
            invoice_types=invoice_types,
            ksef_reference_number=ksef_reference_number,
            subject_by=subject_by,
            subject_to=subject_to,
        )

        v2_query_criteria_invoice_detail_type.additional_properties = d
        return v2_query_criteria_invoice_detail_type

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
