from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_type import InvoiceType
from ..models.invoicing_mode import InvoicingMode
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.invoice_metadata_third_subject import InvoiceMetadataThirdSubject
  from ..models.form_code import FormCode
  from ..models.invoice_metadata_seller import InvoiceMetadataSeller
  from ..models.invoice_metadata_buyer import InvoiceMetadataBuyer
  from ..models.invoice_metadata_authorized_subject import InvoiceMetadataAuthorizedSubject





T = TypeVar("T", bound="InvoiceMetadata")



@_attrs_define
class InvoiceMetadata:
    """ 
        Attributes:
            ksef_number (str): Numer KSeF o długości 35 znaków jest akceptowany, by zachować kompatybilność wsteczna z KSeF
                1.0. W KSeF 2.0 numery są generowane wyłącznie w formacie 36-znakowym.
            invoice_number (str): Numer faktury nadany przez wystawcę.
            issue_date (datetime.date): Data wystawienia faktury.
            invoicing_date (datetime.datetime): Data przyjęcia faktury w systemie KSeF (do dalszego przetwarzania).
            acquisition_date (datetime.datetime): Data nadania numeru KSeF.
            permanent_storage_date (datetime.datetime): Data trwałego zapisu faktury w repozytorium systemu KSeF.
            seller (InvoiceMetadataSeller):
            buyer (InvoiceMetadataBuyer):
            net_amount (float): Łączna kwota netto.
            gross_amount (float): Łączna kwota brutto.
            vat_amount (float): Łączna kwota VAT.
            currency (str): Kod waluty.
            invoicing_mode (InvoicingMode):
            invoice_type (InvoiceType): | Wartość | Opis |
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
            form_code (FormCode):
            is_self_invoicing (bool): Czy faktura została wystawiona w trybie samofakturowania.
            has_attachment (bool): Określa, czy faktura posiada załącznik.
            invoice_hash (str): SHA-256 w Base64.
            hash_of_corrected_invoice (Union[None, Unset, str]): Skrót SHA256 korygowanej faktury.
            third_subjects (Union[None, Unset, list['InvoiceMetadataThirdSubject']]): Lista podmiotów trzecich.
            authorized_subject (Union['InvoiceMetadataAuthorizedSubject', None, Unset]): Podmiot upoważniony.
     """

    ksef_number: str
    invoice_number: str
    issue_date: datetime.date
    invoicing_date: datetime.datetime
    acquisition_date: datetime.datetime
    permanent_storage_date: datetime.datetime
    seller: 'InvoiceMetadataSeller'
    buyer: 'InvoiceMetadataBuyer'
    net_amount: float
    gross_amount: float
    vat_amount: float
    currency: str
    invoicing_mode: InvoicingMode
    invoice_type: InvoiceType
    form_code: 'FormCode'
    is_self_invoicing: bool
    has_attachment: bool
    invoice_hash: str
    hash_of_corrected_invoice: Union[None, Unset, str] = UNSET
    third_subjects: Union[None, Unset, list['InvoiceMetadataThirdSubject']] = UNSET
    authorized_subject: Union['InvoiceMetadataAuthorizedSubject', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_metadata_third_subject import InvoiceMetadataThirdSubject
        from ..models.form_code import FormCode
        from ..models.invoice_metadata_seller import InvoiceMetadataSeller
        from ..models.invoice_metadata_buyer import InvoiceMetadataBuyer
        from ..models.invoice_metadata_authorized_subject import InvoiceMetadataAuthorizedSubject
        ksef_number = self.ksef_number

        invoice_number = self.invoice_number

        issue_date = self.issue_date.isoformat()

        invoicing_date = self.invoicing_date.isoformat()

        acquisition_date = self.acquisition_date.isoformat()

        permanent_storage_date = self.permanent_storage_date.isoformat()

        seller = self.seller.to_dict()

        buyer = self.buyer.to_dict()

        net_amount = self.net_amount

        gross_amount = self.gross_amount

        vat_amount = self.vat_amount

        currency = self.currency

        invoicing_mode = self.invoicing_mode.value

        invoice_type = self.invoice_type.value

        form_code = self.form_code.to_dict()

        is_self_invoicing = self.is_self_invoicing

        has_attachment = self.has_attachment

        invoice_hash = self.invoice_hash

        hash_of_corrected_invoice: Union[None, Unset, str]
        if isinstance(self.hash_of_corrected_invoice, Unset):
            hash_of_corrected_invoice = UNSET
        else:
            hash_of_corrected_invoice = self.hash_of_corrected_invoice

        third_subjects: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.third_subjects, Unset):
            third_subjects = UNSET
        elif isinstance(self.third_subjects, list):
            third_subjects = []
            for third_subjects_type_0_item_data in self.third_subjects:
                third_subjects_type_0_item = third_subjects_type_0_item_data.to_dict()
                third_subjects.append(third_subjects_type_0_item)


        else:
            third_subjects = self.third_subjects

        authorized_subject: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorized_subject, Unset):
            authorized_subject = UNSET
        elif isinstance(self.authorized_subject, InvoiceMetadataAuthorizedSubject):
            authorized_subject = self.authorized_subject.to_dict()
        else:
            authorized_subject = self.authorized_subject


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ksefNumber": ksef_number,
            "invoiceNumber": invoice_number,
            "issueDate": issue_date,
            "invoicingDate": invoicing_date,
            "acquisitionDate": acquisition_date,
            "permanentStorageDate": permanent_storage_date,
            "seller": seller,
            "buyer": buyer,
            "netAmount": net_amount,
            "grossAmount": gross_amount,
            "vatAmount": vat_amount,
            "currency": currency,
            "invoicingMode": invoicing_mode,
            "invoiceType": invoice_type,
            "formCode": form_code,
            "isSelfInvoicing": is_self_invoicing,
            "hasAttachment": has_attachment,
            "invoiceHash": invoice_hash,
        })
        if hash_of_corrected_invoice is not UNSET:
            field_dict["hashOfCorrectedInvoice"] = hash_of_corrected_invoice
        if third_subjects is not UNSET:
            field_dict["thirdSubjects"] = third_subjects
        if authorized_subject is not UNSET:
            field_dict["authorizedSubject"] = authorized_subject

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_metadata_third_subject import InvoiceMetadataThirdSubject
        from ..models.form_code import FormCode
        from ..models.invoice_metadata_seller import InvoiceMetadataSeller
        from ..models.invoice_metadata_buyer import InvoiceMetadataBuyer
        from ..models.invoice_metadata_authorized_subject import InvoiceMetadataAuthorizedSubject
        d = dict(src_dict)
        ksef_number = d.pop("ksefNumber")

        invoice_number = d.pop("invoiceNumber")

        issue_date = isoparse(d.pop("issueDate")).date()




        invoicing_date = isoparse(d.pop("invoicingDate"))




        acquisition_date = isoparse(d.pop("acquisitionDate"))




        permanent_storage_date = isoparse(d.pop("permanentStorageDate"))




        seller = InvoiceMetadataSeller.from_dict(d.pop("seller"))




        buyer = InvoiceMetadataBuyer.from_dict(d.pop("buyer"))




        net_amount = d.pop("netAmount")

        gross_amount = d.pop("grossAmount")

        vat_amount = d.pop("vatAmount")

        currency = d.pop("currency")

        invoicing_mode = InvoicingMode(d.pop("invoicingMode"))




        invoice_type = InvoiceType(d.pop("invoiceType"))




        form_code = FormCode.from_dict(d.pop("formCode"))




        is_self_invoicing = d.pop("isSelfInvoicing")

        has_attachment = d.pop("hasAttachment")

        invoice_hash = d.pop("invoiceHash")

        def _parse_hash_of_corrected_invoice(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_of_corrected_invoice = _parse_hash_of_corrected_invoice(d.pop("hashOfCorrectedInvoice", UNSET))


        def _parse_third_subjects(data: object) -> Union[None, Unset, list['InvoiceMetadataThirdSubject']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                third_subjects_type_0 = []
                _third_subjects_type_0 = data
                for third_subjects_type_0_item_data in (_third_subjects_type_0):
                    third_subjects_type_0_item = InvoiceMetadataThirdSubject.from_dict(third_subjects_type_0_item_data)



                    third_subjects_type_0.append(third_subjects_type_0_item)

                return third_subjects_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['InvoiceMetadataThirdSubject']], data)

        third_subjects = _parse_third_subjects(d.pop("thirdSubjects", UNSET))


        def _parse_authorized_subject(data: object) -> Union['InvoiceMetadataAuthorizedSubject', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorized_subject_type_1 = InvoiceMetadataAuthorizedSubject.from_dict(data)



                return authorized_subject_type_1
            except: # noqa: E722
                pass
            return cast(Union['InvoiceMetadataAuthorizedSubject', None, Unset], data)

        authorized_subject = _parse_authorized_subject(d.pop("authorizedSubject", UNSET))


        invoice_metadata = cls(
            ksef_number=ksef_number,
            invoice_number=invoice_number,
            issue_date=issue_date,
            invoicing_date=invoicing_date,
            acquisition_date=acquisition_date,
            permanent_storage_date=permanent_storage_date,
            seller=seller,
            buyer=buyer,
            net_amount=net_amount,
            gross_amount=gross_amount,
            vat_amount=vat_amount,
            currency=currency,
            invoicing_mode=invoicing_mode,
            invoice_type=invoice_type,
            form_code=form_code,
            is_self_invoicing=is_self_invoicing,
            has_attachment=has_attachment,
            invoice_hash=invoice_hash,
            hash_of_corrected_invoice=hash_of_corrected_invoice,
            third_subjects=third_subjects,
            authorized_subject=authorized_subject,
        )

        return invoice_metadata

