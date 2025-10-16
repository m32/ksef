from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.part_upload_request_headers_type_0 import PartUploadRequestHeadersType0





T = TypeVar("T", bound="PartUploadRequest")



@_attrs_define
class PartUploadRequest:
    """ 
        Attributes:
            ordinal_number (Union[Unset, int]): Numer sekwencyjny części pliku paczki.
            method (Union[None, Unset, str]): Metoda HTTP, której należy użyć przy wysyłce części pliku paczki.
            url (Union[None, Unset, str]): Adres pod który należy wysłać część pliku paczki.
            headers (Union['PartUploadRequestHeadersType0', None, Unset]): Nagłówki, których należy użyć przy wysyłce części
                pliku paczki.
     """

    ordinal_number: Union[Unset, int] = UNSET
    method: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    headers: Union['PartUploadRequestHeadersType0', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.part_upload_request_headers_type_0 import PartUploadRequestHeadersType0
        ordinal_number = self.ordinal_number

        method: Union[None, Unset, str]
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        headers: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, PartUploadRequestHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ordinal_number is not UNSET:
            field_dict["ordinalNumber"] = ordinal_number
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.part_upload_request_headers_type_0 import PartUploadRequestHeadersType0
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber", UNSET)

        def _parse_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        method = _parse_method(d.pop("method", UNSET))


        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_headers(data: object) -> Union['PartUploadRequestHeadersType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = PartUploadRequestHeadersType0.from_dict(data)



                return headers_type_0
            except: # noqa: E722
                pass
            return cast(Union['PartUploadRequestHeadersType0', None, Unset], data)

        headers = _parse_headers(d.pop("headers", UNSET))


        part_upload_request = cls(
            ordinal_number=ordinal_number,
            method=method,
            url=url,
            headers=headers,
        )

        return part_upload_request

