from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoicing_mode import InvoicingMode
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.status_info import StatusInfo





T = TypeVar("T", bound="SessionInvoiceStatusResponse")



@_attrs_define
class SessionInvoiceStatusResponse:
    """ 
        Attributes:
            ordinal_number (int): Numer sekwencyjny faktury w ramach sesji.
            reference_number (str): Numer referencyjny.
            invoice_hash (str): SHA-256 w Base64.
            invoicing_date (datetime.datetime): Data przyjęcia faktury w systemie KSeF (do dalszego przetwarzania).
            status (StatusInfo):
            invoice_number (Union[None, Unset, str]): Numer faktury.
            ksef_number (Union[None, Unset, str]): Numer KSeF.
            invoice_file_name (Union[None, Unset, str]): Nazwa pliku faktury (zwracana dla faktur wysyłanych wsadowo).
            acquisition_date (Union[None, Unset, datetime.datetime]): Data nadania numeru KSeF.
            permanent_storage_date (Union[None, Unset, datetime.datetime]): Data trwałego zapisu faktury w repozytorium
                KSeF. Wartość uzupełniana asynchronicznie w momencie trwałego zapisu; zawsze późniejsza niż
                <b>acquisitionDate</b>. Podczas sprawdzania statusu może być jeszcze niedostępna.
            upo_download_url (Union[None, Unset, str]): Adres do pobrania UPO. Link generowany jest przy każdym odpytaniu o
                status.
                Dostęp odbywa się metodą `HTTP GET` i <b>nie należy</b> wysyłać tokenu dostępowego.
                Link nie podlega limitom API i wygasa po określonym czasie w `UpoDownloadUrlExpirationDate`.
            upo_download_url_expiration_date (Union[None, Unset, datetime.datetime]): Data i godzina wygaśnięcia adresu. Po
                tej dacie link `UpoDownloadUrl` nie będzie już aktywny.
            invoicing_mode (Union[InvoicingMode, None, Unset]): Tryb fakturowania (online/offline).
     """

    ordinal_number: int
    reference_number: str
    invoice_hash: str
    invoicing_date: datetime.datetime
    status: 'StatusInfo'
    invoice_number: Union[None, Unset, str] = UNSET
    ksef_number: Union[None, Unset, str] = UNSET
    invoice_file_name: Union[None, Unset, str] = UNSET
    acquisition_date: Union[None, Unset, datetime.datetime] = UNSET
    permanent_storage_date: Union[None, Unset, datetime.datetime] = UNSET
    upo_download_url: Union[None, Unset, str] = UNSET
    upo_download_url_expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    invoicing_mode: Union[InvoicingMode, None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_info import StatusInfo
        ordinal_number = self.ordinal_number

        reference_number = self.reference_number

        invoice_hash = self.invoice_hash

        invoicing_date = self.invoicing_date.isoformat()

        status = self.status.to_dict()

        invoice_number: Union[None, Unset, str]
        if isinstance(self.invoice_number, Unset):
            invoice_number = UNSET
        else:
            invoice_number = self.invoice_number

        ksef_number: Union[None, Unset, str]
        if isinstance(self.ksef_number, Unset):
            ksef_number = UNSET
        else:
            ksef_number = self.ksef_number

        invoice_file_name: Union[None, Unset, str]
        if isinstance(self.invoice_file_name, Unset):
            invoice_file_name = UNSET
        else:
            invoice_file_name = self.invoice_file_name

        acquisition_date: Union[None, Unset, str]
        if isinstance(self.acquisition_date, Unset):
            acquisition_date = UNSET
        elif isinstance(self.acquisition_date, datetime.datetime):
            acquisition_date = self.acquisition_date.isoformat()
        else:
            acquisition_date = self.acquisition_date

        permanent_storage_date: Union[None, Unset, str]
        if isinstance(self.permanent_storage_date, Unset):
            permanent_storage_date = UNSET
        elif isinstance(self.permanent_storage_date, datetime.datetime):
            permanent_storage_date = self.permanent_storage_date.isoformat()
        else:
            permanent_storage_date = self.permanent_storage_date

        upo_download_url: Union[None, Unset, str]
        if isinstance(self.upo_download_url, Unset):
            upo_download_url = UNSET
        else:
            upo_download_url = self.upo_download_url

        upo_download_url_expiration_date: Union[None, Unset, str]
        if isinstance(self.upo_download_url_expiration_date, Unset):
            upo_download_url_expiration_date = UNSET
        elif isinstance(self.upo_download_url_expiration_date, datetime.datetime):
            upo_download_url_expiration_date = self.upo_download_url_expiration_date.isoformat()
        else:
            upo_download_url_expiration_date = self.upo_download_url_expiration_date

        invoicing_mode: Union[None, Unset, str]
        if isinstance(self.invoicing_mode, Unset):
            invoicing_mode = UNSET
        elif isinstance(self.invoicing_mode, InvoicingMode):
            invoicing_mode = self.invoicing_mode.value
        else:
            invoicing_mode = self.invoicing_mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ordinalNumber": ordinal_number,
            "referenceNumber": reference_number,
            "invoiceHash": invoice_hash,
            "invoicingDate": invoicing_date,
            "status": status,
        })
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if ksef_number is not UNSET:
            field_dict["ksefNumber"] = ksef_number
        if invoice_file_name is not UNSET:
            field_dict["invoiceFileName"] = invoice_file_name
        if acquisition_date is not UNSET:
            field_dict["acquisitionDate"] = acquisition_date
        if permanent_storage_date is not UNSET:
            field_dict["permanentStorageDate"] = permanent_storage_date
        if upo_download_url is not UNSET:
            field_dict["upoDownloadUrl"] = upo_download_url
        if upo_download_url_expiration_date is not UNSET:
            field_dict["upoDownloadUrlExpirationDate"] = upo_download_url_expiration_date
        if invoicing_mode is not UNSET:
            field_dict["invoicingMode"] = invoicing_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber")

        reference_number = d.pop("referenceNumber")

        invoice_hash = d.pop("invoiceHash")

        invoicing_date = isoparse(d.pop("invoicingDate"))




        status = StatusInfo.from_dict(d.pop("status"))




        def _parse_invoice_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_number = _parse_invoice_number(d.pop("invoiceNumber", UNSET))


        def _parse_ksef_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ksef_number = _parse_ksef_number(d.pop("ksefNumber", UNSET))


        def _parse_invoice_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_file_name = _parse_invoice_file_name(d.pop("invoiceFileName", UNSET))


        def _parse_acquisition_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquisition_date_type_0 = isoparse(data)



                return acquisition_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        acquisition_date = _parse_acquisition_date(d.pop("acquisitionDate", UNSET))


        def _parse_permanent_storage_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                permanent_storage_date_type_0 = isoparse(data)



                return permanent_storage_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        permanent_storage_date = _parse_permanent_storage_date(d.pop("permanentStorageDate", UNSET))


        def _parse_upo_download_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        upo_download_url = _parse_upo_download_url(d.pop("upoDownloadUrl", UNSET))


        def _parse_upo_download_url_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upo_download_url_expiration_date_type_0 = isoparse(data)



                return upo_download_url_expiration_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        upo_download_url_expiration_date = _parse_upo_download_url_expiration_date(d.pop("upoDownloadUrlExpirationDate", UNSET))


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


        session_invoice_status_response = cls(
            ordinal_number=ordinal_number,
            reference_number=reference_number,
            invoice_hash=invoice_hash,
            invoicing_date=invoicing_date,
            status=status,
            invoice_number=invoice_number,
            ksef_number=ksef_number,
            invoice_file_name=invoice_file_name,
            acquisition_date=acquisition_date,
            permanent_storage_date=permanent_storage_date,
            upo_download_url=upo_download_url,
            upo_download_url_expiration_date=upo_download_url_expiration_date,
            invoicing_mode=invoicing_mode,
        )

        return session_invoice_status_response

