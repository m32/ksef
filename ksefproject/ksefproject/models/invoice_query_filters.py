from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.currency_code import CurrencyCode
from ..models.invoice_query_form_type import InvoiceQueryFormType
from ..models.invoice_query_subject_type import InvoiceQuerySubjectType
from ..models.invoice_type import InvoiceType
from ..models.invoicing_mode import InvoicingMode
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.invoice_query_buyer_identifier import InvoiceQueryBuyerIdentifier
  from ..models.invoice_query_amount import InvoiceQueryAmount
  from ..models.invoice_query_date_range import InvoiceQueryDateRange





T = TypeVar("T", bound="InvoiceQueryFilters")



@_attrs_define
class InvoiceQueryFilters:
    """ 
        Attributes:
            subject_type (InvoiceQuerySubjectType): | Wartość | Opis |
                | --- | --- |
                | Subject1 | Podmiot 1 - sprzedawca |
                | Subject2 | Podmiot 2 - nabywca |
                | Subject3 | Podmiot 3 |
                | SubjectAuthorized | Podmiot upoważniony |
            date_range (InvoiceQueryDateRange):
            ksef_number (Union[None, Unset, str]): Numer KSeF faktury (exact match).
            invoice_number (Union[None, Unset, str]): Numer faktury nadany przez wystawcę (exact match).
            amount (Union['InvoiceQueryAmount', None, Unset]): Filtr kwotowy – brutto, netto lub VAT (z wartością).
            seller_nip (Union[None, Unset, str]): Nip sprzedawcy (exact match).
            buyer_identifier (Union['InvoiceQueryBuyerIdentifier', None, Unset]): Identyfikator nabywcy.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | VatUe | Identyfikator VAT UE podmiotu unijnego. |
                | Other | Inny identyfikator|
                | None  | Brak identyfikatora nabywcy |
            currency_codes (Union[None, Unset, list[CurrencyCode]]): Kody walut.
            invoicing_mode (Union[InvoicingMode, None, Unset]): Tryb wystawienia faktury: online lub offline.
            is_self_invoicing (Union[None, Unset, bool]): Czy faktura została wystawiona w trybie samofakturowania.
            form_type (Union[InvoiceQueryFormType, None, Unset]): Typ dokumentu.
                | Wartość | Opis |
                | --- | --- |
                | FA | Faktura VAT |
                | PEF | Faktura PEF |
                | RR | Faktura RR |
            invoice_types (Union[None, Unset, list[InvoiceType]]): Rodzaje faktur.
                | Wartość | Opis |
                | --- | --- |
                | Vat | (FA) Podstawowa |
                | Zal | (FA) Zaliczkowa |
                | Kor | (FA) Korygująca |
                | Roz | (FA) Rozliczeniowa |
                | Upr | (FA) Uproszczona |
                | KorZal | (FA) Korygująca fakturę zaliczkową |
                | KorRoz | (FA) Korygująca fakturę rozliczeniową |
                | VatPef | (PEF) Podstawowowa |
                | VatPefSp | (PEF) Specjalizowana |
                | KorPef | (PEF) Korygująca |
                | VatRr | (RR) Podstawowa |
                | KorVatRr | (RR) Korygująca |
            has_attachment (Union[None, Unset, bool]): Czy faktura ma załącznik.
     """

    subject_type: InvoiceQuerySubjectType
    date_range: 'InvoiceQueryDateRange'
    ksef_number: Union[None, Unset, str] = UNSET
    invoice_number: Union[None, Unset, str] = UNSET
    amount: Union['InvoiceQueryAmount', None, Unset] = UNSET
    seller_nip: Union[None, Unset, str] = UNSET
    buyer_identifier: Union['InvoiceQueryBuyerIdentifier', None, Unset] = UNSET
    currency_codes: Union[None, Unset, list[CurrencyCode]] = UNSET
    invoicing_mode: Union[InvoicingMode, None, Unset] = UNSET
    is_self_invoicing: Union[None, Unset, bool] = UNSET
    form_type: Union[InvoiceQueryFormType, None, Unset] = UNSET
    invoice_types: Union[None, Unset, list[InvoiceType]] = UNSET
    has_attachment: Union[None, Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_query_buyer_identifier import InvoiceQueryBuyerIdentifier
        from ..models.invoice_query_amount import InvoiceQueryAmount
        from ..models.invoice_query_date_range import InvoiceQueryDateRange
        subject_type = self.subject_type.value

        date_range = self.date_range.to_dict()

        ksef_number: Union[None, Unset, str]
        if isinstance(self.ksef_number, Unset):
            ksef_number = UNSET
        else:
            ksef_number = self.ksef_number

        invoice_number: Union[None, Unset, str]
        if isinstance(self.invoice_number, Unset):
            invoice_number = UNSET
        else:
            invoice_number = self.invoice_number

        amount: Union[None, Unset, dict[str, Any]]
        if isinstance(self.amount, Unset):
            amount = UNSET
        elif isinstance(self.amount, InvoiceQueryAmount):
            amount = self.amount.to_dict()
        else:
            amount = self.amount

        seller_nip: Union[None, Unset, str]
        if isinstance(self.seller_nip, Unset):
            seller_nip = UNSET
        else:
            seller_nip = self.seller_nip

        buyer_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.buyer_identifier, Unset):
            buyer_identifier = UNSET
        elif isinstance(self.buyer_identifier, InvoiceQueryBuyerIdentifier):
            buyer_identifier = self.buyer_identifier.to_dict()
        else:
            buyer_identifier = self.buyer_identifier

        currency_codes: Union[None, Unset, list[str]]
        if isinstance(self.currency_codes, Unset):
            currency_codes = UNSET
        elif isinstance(self.currency_codes, list):
            currency_codes = []
            for currency_codes_type_0_item_data in self.currency_codes:
                currency_codes_type_0_item = currency_codes_type_0_item_data.value
                currency_codes.append(currency_codes_type_0_item)


        else:
            currency_codes = self.currency_codes

        invoicing_mode: Union[None, Unset, str]
        if isinstance(self.invoicing_mode, Unset):
            invoicing_mode = UNSET
        elif isinstance(self.invoicing_mode, InvoicingMode):
            invoicing_mode = self.invoicing_mode.value
        else:
            invoicing_mode = self.invoicing_mode

        is_self_invoicing: Union[None, Unset, bool]
        if isinstance(self.is_self_invoicing, Unset):
            is_self_invoicing = UNSET
        else:
            is_self_invoicing = self.is_self_invoicing

        form_type: Union[None, Unset, str]
        if isinstance(self.form_type, Unset):
            form_type = UNSET
        elif isinstance(self.form_type, InvoiceQueryFormType):
            form_type = self.form_type.value
        else:
            form_type = self.form_type

        invoice_types: Union[None, Unset, list[str]]
        if isinstance(self.invoice_types, Unset):
            invoice_types = UNSET
        elif isinstance(self.invoice_types, list):
            invoice_types = []
            for invoice_types_type_0_item_data in self.invoice_types:
                invoice_types_type_0_item = invoice_types_type_0_item_data.value
                invoice_types.append(invoice_types_type_0_item)


        else:
            invoice_types = self.invoice_types

        has_attachment: Union[None, Unset, bool]
        if isinstance(self.has_attachment, Unset):
            has_attachment = UNSET
        else:
            has_attachment = self.has_attachment


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectType": subject_type,
            "dateRange": date_range,
        })
        if ksef_number is not UNSET:
            field_dict["ksefNumber"] = ksef_number
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if amount is not UNSET:
            field_dict["amount"] = amount
        if seller_nip is not UNSET:
            field_dict["sellerNip"] = seller_nip
        if buyer_identifier is not UNSET:
            field_dict["buyerIdentifier"] = buyer_identifier
        if currency_codes is not UNSET:
            field_dict["currencyCodes"] = currency_codes
        if invoicing_mode is not UNSET:
            field_dict["invoicingMode"] = invoicing_mode
        if is_self_invoicing is not UNSET:
            field_dict["isSelfInvoicing"] = is_self_invoicing
        if form_type is not UNSET:
            field_dict["formType"] = form_type
        if invoice_types is not UNSET:
            field_dict["invoiceTypes"] = invoice_types
        if has_attachment is not UNSET:
            field_dict["hasAttachment"] = has_attachment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_query_buyer_identifier import InvoiceQueryBuyerIdentifier
        from ..models.invoice_query_amount import InvoiceQueryAmount
        from ..models.invoice_query_date_range import InvoiceQueryDateRange
        d = dict(src_dict)
        subject_type = InvoiceQuerySubjectType(d.pop("subjectType"))




        date_range = InvoiceQueryDateRange.from_dict(d.pop("dateRange"))




        def _parse_ksef_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ksef_number = _parse_ksef_number(d.pop("ksefNumber", UNSET))


        def _parse_invoice_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_number = _parse_invoice_number(d.pop("invoiceNumber", UNSET))


        def _parse_amount(data: object) -> Union['InvoiceQueryAmount', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amount_type_1 = InvoiceQueryAmount.from_dict(data)



                return amount_type_1
            except: # noqa: E722
                pass
            return cast(Union['InvoiceQueryAmount', None, Unset], data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_seller_nip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        seller_nip = _parse_seller_nip(d.pop("sellerNip", UNSET))


        def _parse_buyer_identifier(data: object) -> Union['InvoiceQueryBuyerIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                buyer_identifier_type_1 = InvoiceQueryBuyerIdentifier.from_dict(data)



                return buyer_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['InvoiceQueryBuyerIdentifier', None, Unset], data)

        buyer_identifier = _parse_buyer_identifier(d.pop("buyerIdentifier", UNSET))


        def _parse_currency_codes(data: object) -> Union[None, Unset, list[CurrencyCode]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                currency_codes_type_0 = []
                _currency_codes_type_0 = data
                for currency_codes_type_0_item_data in (_currency_codes_type_0):
                    currency_codes_type_0_item = CurrencyCode(currency_codes_type_0_item_data)



                    currency_codes_type_0.append(currency_codes_type_0_item)

                return currency_codes_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[CurrencyCode]], data)

        currency_codes = _parse_currency_codes(d.pop("currencyCodes", UNSET))


        def _parse_invoicing_mode(data: object) -> Union[InvoicingMode, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoicing_mode_type_1 = InvoicingMode(data)



                return invoicing_mode_type_1
            except: # noqa: E722
                pass
            return cast(Union[InvoicingMode, None, Unset], data)

        invoicing_mode = _parse_invoicing_mode(d.pop("invoicingMode", UNSET))


        def _parse_is_self_invoicing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_self_invoicing = _parse_is_self_invoicing(d.pop("isSelfInvoicing", UNSET))


        def _parse_form_type(data: object) -> Union[InvoiceQueryFormType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_type_type_1 = InvoiceQueryFormType(data)



                return form_type_type_1
            except: # noqa: E722
                pass
            return cast(Union[InvoiceQueryFormType, None, Unset], data)

        form_type = _parse_form_type(d.pop("formType", UNSET))


        def _parse_invoice_types(data: object) -> Union[None, Unset, list[InvoiceType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                invoice_types_type_0 = []
                _invoice_types_type_0 = data
                for invoice_types_type_0_item_data in (_invoice_types_type_0):
                    invoice_types_type_0_item = InvoiceType(invoice_types_type_0_item_data)



                    invoice_types_type_0.append(invoice_types_type_0_item)

                return invoice_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[InvoiceType]], data)

        invoice_types = _parse_invoice_types(d.pop("invoiceTypes", UNSET))


        def _parse_has_attachment(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_attachment = _parse_has_attachment(d.pop("hasAttachment", UNSET))


        invoice_query_filters = cls(
            subject_type=subject_type,
            date_range=date_range,
            ksef_number=ksef_number,
            invoice_number=invoice_number,
            amount=amount,
            seller_nip=seller_nip,
            buyer_identifier=buyer_identifier,
            currency_codes=currency_codes,
            invoicing_mode=invoicing_mode,
            is_self_invoicing=is_self_invoicing,
            form_type=form_type,
            invoice_types=invoice_types,
            has_attachment=has_attachment,
        )

        return invoice_query_filters

