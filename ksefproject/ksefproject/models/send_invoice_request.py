from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="SendInvoiceRequest")



@_attrs_define
class SendInvoiceRequest:
    """ 
        Attributes:
            invoice_hash (str): SHA-256 w Base64.
            invoice_size (int): Rozmiar oryginalnej faktury w bajtach. Maksymalny rozmiar zależy od limitów ustawionych dla
                uwierzytelnionego kontekstu.
            encrypted_invoice_hash (str): SHA-256 w Base64.
            encrypted_invoice_size (int): Rozmiar zaszyfrowanej faktury w bajtach.
            encrypted_invoice_content (str): Faktura zaszyfrowana algorytmem AES-256-CBC z dopełnianiem PKCS#7 (kluczem
                przekazanym przy otwarciu sesji), zakodowana w formacie Base64.
            offline_mode (Union[Unset, bool]): Określa, czy podatnik deklaruje tryb fakturowania "offline" dla przesyłanego
                dokumentu. Default: False.
            hash_of_corrected_invoice (Union[None, Unset, str]): Skrót SHA256 korygowanej faktury, zakodowany w formacie
                Base64. Wymagany przy wysyłaniu korekty technicznej faktury.
     """

    invoice_hash: str
    invoice_size: int
    encrypted_invoice_hash: str
    encrypted_invoice_size: int
    encrypted_invoice_content: str
    offline_mode: Union[Unset, bool] = False
    hash_of_corrected_invoice: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        invoice_hash = self.invoice_hash

        invoice_size = self.invoice_size

        encrypted_invoice_hash = self.encrypted_invoice_hash

        encrypted_invoice_size = self.encrypted_invoice_size

        encrypted_invoice_content = self.encrypted_invoice_content

        offline_mode = self.offline_mode

        hash_of_corrected_invoice: Union[None, Unset, str]
        if isinstance(self.hash_of_corrected_invoice, Unset):
            hash_of_corrected_invoice = UNSET
        else:
            hash_of_corrected_invoice = self.hash_of_corrected_invoice


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "invoiceHash": invoice_hash,
            "invoiceSize": invoice_size,
            "encryptedInvoiceHash": encrypted_invoice_hash,
            "encryptedInvoiceSize": encrypted_invoice_size,
            "encryptedInvoiceContent": encrypted_invoice_content,
        })
        if offline_mode is not UNSET:
            field_dict["offlineMode"] = offline_mode
        if hash_of_corrected_invoice is not UNSET:
            field_dict["hashOfCorrectedInvoice"] = hash_of_corrected_invoice

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invoice_hash = d.pop("invoiceHash")

        invoice_size = d.pop("invoiceSize")

        encrypted_invoice_hash = d.pop("encryptedInvoiceHash")

        encrypted_invoice_size = d.pop("encryptedInvoiceSize")

        encrypted_invoice_content = d.pop("encryptedInvoiceContent")

        offline_mode = d.pop("offlineMode", UNSET)

        def _parse_hash_of_corrected_invoice(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_of_corrected_invoice = _parse_hash_of_corrected_invoice(d.pop("hashOfCorrectedInvoice", UNSET))


        send_invoice_request = cls(
            invoice_hash=invoice_hash,
            invoice_size=invoice_size,
            encrypted_invoice_hash=encrypted_invoice_hash,
            encrypted_invoice_size=encrypted_invoice_size,
            encrypted_invoice_content=encrypted_invoice_content,
            offline_mode=offline_mode,
            hash_of_corrected_invoice=hash_of_corrected_invoice,
        )

        return send_invoice_request

