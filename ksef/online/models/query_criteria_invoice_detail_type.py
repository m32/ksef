from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.query_criteria_invoice_detail_type_amount_type import QueryCriteriaInvoiceDetailTypeAmountType
from ..models.query_criteria_invoice_type_subject_type import QueryCriteriaInvoiceTypeSubjectType
from dateutil.parser import isoparse
from typing import Union
from typing import Dict
from ..models.query_criteria_invoice_detail_type_invoice_types_item import QueryCriteriaInvoiceDetailTypeInvoiceTypesItem
from typing import cast, List
from ..models.query_criteria_invoice_detail_type_schema_type import QueryCriteriaInvoiceDetailTypeSchemaType
from typing import cast
import datetime
from ..types import UNSET, Unset
from ..models.query_criteria_invoice_detail_type_currency_codes_item import QueryCriteriaInvoiceDetailTypeCurrencyCodesItem

if TYPE_CHECKING:
  from ..models.subject_by_type import SubjectByType
  from ..models.subject_to_type import SubjectToType





T = TypeVar("T", bound="QueryCriteriaInvoiceDetailType")


@_attrs_define
class QueryCriteriaInvoiceDetailType:
    """ 
        Attributes:
            subject_type (QueryCriteriaInvoiceTypeSubjectType):
            type (str):
            invoicing_date_from (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | minimum date range is 2022-01-01
            invoicing_date_to (datetime.datetime): yyyy-MM-dd'T'HH:mm:ss | maximum date range is current time (+ max 6
                hours), the difference between date field and #invoicingDateFrom cannot be greater than 24 months, date field
                cannot be before #invoicingDateFrom
            hiding_date_from (Union[Unset, datetime.datetime]): yyyy-MM-dd'T'HH:mm:ss
            hiding_date_to (Union[Unset, datetime.datetime]): yyyy-MM-dd'T'HH:mm:ss
            is_hidden (Union[Unset, bool]):
            amount_from (Union[Unset, float]):
            amount_to (Union[Unset, float]):
            amount_type (Union[Unset, QueryCriteriaInvoiceDetailTypeAmountType]):
            currency_codes (Union[Unset, List[QueryCriteriaInvoiceDetailTypeCurrencyCodesItem]]):
            fa_p17_annotation (Union[Unset, bool]):
            invoice_number (Union[Unset, str]):
            invoice_types (Union[Unset, List[QueryCriteriaInvoiceDetailTypeInvoiceTypesItem]]):
            ksef_reference_number (Union[Unset, str]):
            schema_type (Union[Unset, QueryCriteriaInvoiceDetailTypeSchemaType]):
            subject_by (Union[Unset, SubjectByType]):
            subject_to (Union[Unset, SubjectToType]):
     """

    subject_type: QueryCriteriaInvoiceTypeSubjectType
    type: str
    invoicing_date_from: datetime.datetime
    invoicing_date_to: datetime.datetime
    hiding_date_from: Union[Unset, datetime.datetime] = UNSET
    hiding_date_to: Union[Unset, datetime.datetime] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    amount_from: Union[Unset, float] = UNSET
    amount_to: Union[Unset, float] = UNSET
    amount_type: Union[Unset, QueryCriteriaInvoiceDetailTypeAmountType] = UNSET
    currency_codes: Union[Unset, List[QueryCriteriaInvoiceDetailTypeCurrencyCodesItem]] = UNSET
    fa_p17_annotation: Union[Unset, bool] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    invoice_types: Union[Unset, List[QueryCriteriaInvoiceDetailTypeInvoiceTypesItem]] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    schema_type: Union[Unset, QueryCriteriaInvoiceDetailTypeSchemaType] = UNSET
    subject_by: Union[Unset, 'SubjectByType'] = UNSET
    subject_to: Union[Unset, 'SubjectToType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_by_type import SubjectByType
        from ..models.subject_to_type import SubjectToType
        subject_type = self.subject_type.value

        type = self.type
        invoicing_date_from = self.invoicing_date_from.isoformat()

        invoicing_date_to = self.invoicing_date_to.isoformat()

        hiding_date_from: Union[Unset, str] = UNSET
        if not isinstance(self.hiding_date_from, Unset):
            hiding_date_from = self.hiding_date_from.isoformat()

        hiding_date_to: Union[Unset, str] = UNSET
        if not isinstance(self.hiding_date_to, Unset):
            hiding_date_to = self.hiding_date_to.isoformat()

        is_hidden = self.is_hidden
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
        schema_type: Union[Unset, str] = UNSET
        if not isinstance(self.schema_type, Unset):
            schema_type = self.schema_type.value

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
        if hiding_date_from is not UNSET:
            field_dict["hidingDateFrom"] = hiding_date_from
        if hiding_date_to is not UNSET:
            field_dict["hidingDateTo"] = hiding_date_to
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
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
        if schema_type is not UNSET:
            field_dict["schemaType"] = schema_type
        if subject_by is not UNSET:
            field_dict["subjectBy"] = subject_by
        if subject_to is not UNSET:
            field_dict["subjectTo"] = subject_to

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_by_type import SubjectByType
        from ..models.subject_to_type import SubjectToType
        d = src_dict.copy()
        subject_type = QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))




        type = d.pop("type")

        invoicing_date_from = isoparse(d.pop("invoicingDateFrom"))




        invoicing_date_to = isoparse(d.pop("invoicingDateTo"))




        _hiding_date_from = d.pop("hidingDateFrom", UNSET)
        hiding_date_from: Union[Unset, datetime.datetime]
        if isinstance(_hiding_date_from,  Unset):
            hiding_date_from = UNSET
        else:
            hiding_date_from = isoparse(_hiding_date_from)




        _hiding_date_to = d.pop("hidingDateTo", UNSET)
        hiding_date_to: Union[Unset, datetime.datetime]
        if isinstance(_hiding_date_to,  Unset):
            hiding_date_to = UNSET
        else:
            hiding_date_to = isoparse(_hiding_date_to)




        is_hidden = d.pop("isHidden", UNSET)

        amount_from = d.pop("amountFrom", UNSET)

        amount_to = d.pop("amountTo", UNSET)

        _amount_type = d.pop("amountType", UNSET)
        amount_type: Union[Unset, QueryCriteriaInvoiceDetailTypeAmountType]
        if isinstance(_amount_type,  Unset):
            amount_type = UNSET
        else:
            amount_type = QueryCriteriaInvoiceDetailTypeAmountType(_amount_type)




        currency_codes = []
        _currency_codes = d.pop("currencyCodes", UNSET)
        for currency_codes_item_data in (_currency_codes or []):
            currency_codes_item = QueryCriteriaInvoiceDetailTypeCurrencyCodesItem(currency_codes_item_data)



            currency_codes.append(currency_codes_item)


        fa_p17_annotation = d.pop("faP17Annotation", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        invoice_types = []
        _invoice_types = d.pop("invoiceTypes", UNSET)
        for invoice_types_item_data in (_invoice_types or []):
            invoice_types_item = QueryCriteriaInvoiceDetailTypeInvoiceTypesItem(invoice_types_item_data)



            invoice_types.append(invoice_types_item)


        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        _schema_type = d.pop("schemaType", UNSET)
        schema_type: Union[Unset, QueryCriteriaInvoiceDetailTypeSchemaType]
        if isinstance(_schema_type,  Unset):
            schema_type = UNSET
        else:
            schema_type = QueryCriteriaInvoiceDetailTypeSchemaType(_schema_type)




        _subject_by = d.pop("subjectBy", UNSET)
        subject_by: Union[Unset, SubjectByType]
        if isinstance(_subject_by,  Unset):
            subject_by = UNSET
        else:
            subject_by = SubjectByType.from_dict(_subject_by)




        _subject_to = d.pop("subjectTo", UNSET)
        subject_to: Union[Unset, SubjectToType]
        if isinstance(_subject_to,  Unset):
            subject_to = UNSET
        else:
            subject_to = SubjectToType.from_dict(_subject_to)




        query_criteria_invoice_detail_type = cls(
            subject_type=subject_type,
            type=type,
            invoicing_date_from=invoicing_date_from,
            invoicing_date_to=invoicing_date_to,
            hiding_date_from=hiding_date_from,
            hiding_date_to=hiding_date_to,
            is_hidden=is_hidden,
            amount_from=amount_from,
            amount_to=amount_to,
            amount_type=amount_type,
            currency_codes=currency_codes,
            fa_p17_annotation=fa_p17_annotation,
            invoice_number=invoice_number,
            invoice_types=invoice_types,
            ksef_reference_number=ksef_reference_number,
            schema_type=schema_type,
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
