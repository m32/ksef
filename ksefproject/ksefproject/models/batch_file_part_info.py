from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BatchFilePartInfo")



@_attrs_define
class BatchFilePartInfo:
    """ 
        Attributes:
            ordinal_number (int): Numer sekwencyjny części pliku paczki.
            file_name (str): Nazwa części pliku paczki.
            file_size (int): Rozmiar części pliku paczki w bajtach. Maksymalna dozwolona wartość to 100MiB (104 857 600
                bajtów).
            file_hash (str): Skrót SHA256 części pliku paczki, zakodowany w formacie Base64.
     """

    ordinal_number: int
    file_name: str
    file_size: int
    file_hash: str





    def to_dict(self) -> dict[str, Any]:
        ordinal_number = self.ordinal_number

        file_name = self.file_name

        file_size = self.file_size

        file_hash = self.file_hash


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ordinalNumber": ordinal_number,
            "fileName": file_name,
            "fileSize": file_size,
            "fileHash": file_hash,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ordinal_number = d.pop("ordinalNumber")

        file_name = d.pop("fileName")

        file_size = d.pop("fileSize")

        file_hash = d.pop("fileHash")

        batch_file_part_info = cls(
            ordinal_number=ordinal_number,
            file_name=file_name,
            file_size=file_size,
            file_hash=file_hash,
        )

        return batch_file_part_info

