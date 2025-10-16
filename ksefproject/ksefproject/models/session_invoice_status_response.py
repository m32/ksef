from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
            invoicing_date (datetime.datetime): Data przyjęcia faktury w systemie KSeF (do dalszego przetwarzania).
            status (StatusInfo):
            invoice_number (Union[None, Unset, str]): Numer faktury.
            ksef_number (Union[None, Unset, str]): Numer KSeF.
            reference_number (Union[None, Unset, str]): Numer referencyjny faktury.
            invoice_hash (Union[None, Unset, str]): Skrót SHA256 faktury, zakodowany w formacie Base64.
            invoice_file_name (Union[None, Unset, str]): Nazwa pliku faktury (zwracana dla faktur wysyłanych wsadowo).
            acquisition_date (Union[None, Unset, datetime.datetime]): Data nadania numeru KSeF.
            permanent_storage_date (Union[None, Unset, datetime.datetime]): Data trwałego zapisu faktury w repozytorium
                systemu KSeF.
            upo_download_url (Union[None, Unset, str]): Adres do pobrania UPO.
     """

    ordinal_number: int
    invoicing_date: datetime.datetime
    status: 'StatusInfo'
    invoice_number: Union[None, Unset, str] = UNSET
    ksef_number: Union[None, Unset, str] = UNSET
    reference_number: Union[None, Unset, str] = UNSET
    invoice_hash: Union[None, Unset, str] = UNSET
    invoice_file_name: Union[None, Unset, str] = UNSET
    acquisition_date: Union[None, Unset, datetime.datetime] = UNSET
    permanent_storage_date: Union[None, Unset, datetime.datetime] = UNSET
    upo_download_url: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_info import StatusInfo
        ordinal_number = self.ordinal_number

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

        reference_number: Union[None, Unset, str]
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        invoice_hash: Union[None, Unset, str]
        if isinstance(self.invoice_hash, Unset):
            invoice_hash = UNSET
        else:
            invoice_hash = self.invoice_hash

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ordinalNumber": ordinal_number,
            "invoicingDate": invoicing_date,
            "status": status,
        })
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if ksef_number is not UNSET:
            field_dict["ksefNumber"] = ksef_number
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if invoice_hash is not UNSET:
            field_dict["invoiceHash"] = invoice_hash
        if invoice_file_name is not UNSET:
            field_dict["invoiceFileName"] = invoice_file_name
        if acquisition_date is not UNSET:
            field_dict["acquisitionDate"] = acquisition_date
        if permanent_storage_date is not UNSET:
            field_dict["permanentStorageDate"] = permanent_storage_date
        if upo_download_url is not UNSET:
            field_dict["upoDownloadUrl"] = upo_download_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber")

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


        def _parse_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_number = _parse_reference_number(d.pop("referenceNumber", UNSET))


        def _parse_invoice_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_hash = _parse_invoice_hash(d.pop("invoiceHash", UNSET))


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


        session_invoice_status_response = cls(
            ordinal_number=ordinal_number,
            invoicing_date=invoicing_date,
            status=status,
            invoice_number=invoice_number,
            ksef_number=ksef_number,
            reference_number=reference_number,
            invoice_hash=invoice_hash,
            invoice_file_name=invoice_file_name,
            acquisition_date=acquisition_date,
            permanent_storage_date=permanent_storage_date,
            upo_download_url=upo_download_url,
        )

        return session_invoice_status_response

