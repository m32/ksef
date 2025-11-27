from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="InvoicePackagePart")



@_attrs_define
class InvoicePackagePart:
    """ 
        Attributes:
            ordinal_number (int): Numer sekwencyjny pliku części paczki.
            part_name (str): Nazwa pliku części paczki.
            method (str): Metoda HTTP, której należy użyć przy pobieraniu pliku.
            url (str): Adres URL, pod który należy wysłać żądanie pobrania części paczki.
                Link jest generowany dynamicznie w momencie odpytania o status operacji eksportu.
                Nie podlega limitom API i nie wymaga przesyłania tokenu dostępowego przy pobraniu.
            part_size (int): Rozmiar części paczki w bajtach.
            part_hash (str): SHA-256 w Base64.
            encrypted_part_size (int): Rozmiar zaszyfrowanej części paczki w bajtach.
            encrypted_part_hash (str): SHA-256 w Base64.
            expiration_date (datetime.datetime): Data i godzina wygaśnięcia linku umożliwiającego pobranie części paczki.
                Po upływie tego momentu link przestaje być aktywny.
     """

    ordinal_number: int
    part_name: str
    method: str
    url: str
    part_size: int
    part_hash: str
    encrypted_part_size: int
    encrypted_part_hash: str
    expiration_date: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        ordinal_number = self.ordinal_number

        part_name = self.part_name

        method = self.method

        url = self.url

        part_size = self.part_size

        part_hash = self.part_hash

        encrypted_part_size = self.encrypted_part_size

        encrypted_part_hash = self.encrypted_part_hash

        expiration_date = self.expiration_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ordinalNumber": ordinal_number,
            "partName": part_name,
            "method": method,
            "url": url,
            "partSize": part_size,
            "partHash": part_hash,
            "encryptedPartSize": encrypted_part_size,
            "encryptedPartHash": encrypted_part_hash,
            "expirationDate": expiration_date,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber")

        part_name = d.pop("partName")

        method = d.pop("method")

        url = d.pop("url")

        part_size = d.pop("partSize")

        part_hash = d.pop("partHash")

        encrypted_part_size = d.pop("encryptedPartSize")

        encrypted_part_hash = d.pop("encryptedPartHash")

        expiration_date = isoparse(d.pop("expirationDate"))




        invoice_package_part = cls(
            ordinal_number=ordinal_number,
            part_name=part_name,
            method=method,
            url=url,
            part_size=part_size,
            part_hash=part_hash,
            encrypted_part_size=encrypted_part_size,
            encrypted_part_hash=encrypted_part_hash,
            expiration_date=expiration_date,
        )

        return invoice_package_part

