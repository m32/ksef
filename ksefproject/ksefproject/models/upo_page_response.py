from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="UpoPageResponse")



@_attrs_define
class UpoPageResponse:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            download_url (str): Adres do pobrania strony UPO. Link generowany jest przy każdym odpytaniu o status.
                Dostęp odbywa się metodą `HTTP GET` i <b>nie należy</b> wysyłać tokenu dostępowego.
                Link nie podlega limitom API i wygasa po określonym czasie w `DownloadUrlExpirationDate`.
            download_url_expiration_date (datetime.datetime): Data i godzina wygaśnięcia adresu. Po tej dacie link
                `DownloadUrl` nie będzie już aktywny.
     """

    reference_number: str
    download_url: str
    download_url_expiration_date: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        reference_number = self.reference_number

        download_url = self.download_url

        download_url_expiration_date = self.download_url_expiration_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "downloadUrl": download_url,
            "downloadUrlExpirationDate": download_url_expiration_date,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        download_url = d.pop("downloadUrl")

        download_url_expiration_date = isoparse(d.pop("downloadUrlExpirationDate"))




        upo_page_response = cls(
            reference_number=reference_number,
            download_url=download_url,
            download_url_expiration_date=download_url_expiration_date,
        )

        return upo_page_response

