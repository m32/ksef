from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="BatchFilePartInfo")



@_attrs_define
class BatchFilePartInfo:
    """ 
        Attributes:
            ordinal_number (int): Numer sekwencyjny części pliku paczki.
            file_size (int): Rozmiar zaszyfrowanej części pliku paczki w bajtach.
            file_hash (str): SHA-256 w Base64.
            file_name (Union[None, Unset, str]): Nazwa części pliku paczki.
     """

    ordinal_number: int
    file_size: int
    file_hash: str
    file_name: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ordinal_number = self.ordinal_number

        file_size = self.file_size

        file_hash = self.file_hash

        file_name: Union[None, Unset, str]
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ordinalNumber": ordinal_number,
            "fileSize": file_size,
            "fileHash": file_hash,
        })
        if file_name is not UNSET:
            field_dict["fileName"] = file_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber")

        file_size = d.pop("fileSize")

        file_hash = d.pop("fileHash")

        def _parse_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        batch_file_part_info = cls(
            ordinal_number=ordinal_number,
            file_size=file_size,
            file_hash=file_hash,
            file_name=file_name,
        )

        return batch_file_part_info

