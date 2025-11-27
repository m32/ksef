from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.part_upload_request_headers import PartUploadRequestHeaders





T = TypeVar("T", bound="PartUploadRequest")



@_attrs_define
class PartUploadRequest:
    """ 
        Attributes:
            ordinal_number (int): Numer sekwencyjny części pliku paczki.
            method (str): Metoda HTTP, której należy użyć przy wysyłce części pliku paczki.
            url (str): Adres pod który należy wysłać część pliku paczki.
            headers (PartUploadRequestHeaders): Nagłówki, których należy użyć przy wysyłce części pliku paczki.
     """

    ordinal_number: int
    method: str
    url: str
    headers: 'PartUploadRequestHeaders'





    def to_dict(self) -> dict[str, Any]:
        from ..models.part_upload_request_headers import PartUploadRequestHeaders
        ordinal_number = self.ordinal_number

        method = self.method

        url = self.url

        headers = self.headers.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ordinalNumber": ordinal_number,
            "method": method,
            "url": url,
            "headers": headers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.part_upload_request_headers import PartUploadRequestHeaders
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber")

        method = d.pop("method")

        url = d.pop("url")

        headers = PartUploadRequestHeaders.from_dict(d.pop("headers"))




        part_upload_request = cls(
            ordinal_number=ordinal_number,
            method=method,
            url=url,
            headers=headers,
        )

        return part_upload_request

