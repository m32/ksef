from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.batch_file_part_info import BatchFilePartInfo





T = TypeVar("T", bound="BatchFileInfo")



@_attrs_define
class BatchFileInfo:
    """ 
        Attributes:
            file_size (int): Rozmiar pliku paczki w bajtach. Maksymalny rozmiar paczki to 5GB.
            file_hash (str): SHA-256 w Base64.
            file_parts (list['BatchFilePartInfo']): Informacje o częściach pliku paczki. Maksymalna liczba części to 50.
                Maksymalny dozwolony rozmiar części przed zaszyfrowaniem to 100MB.
     """

    file_size: int
    file_hash: str
    file_parts: list['BatchFilePartInfo']





    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_file_part_info import BatchFilePartInfo
        file_size = self.file_size

        file_hash = self.file_hash

        file_parts = []
        for file_parts_item_data in self.file_parts:
            file_parts_item = file_parts_item_data.to_dict()
            file_parts.append(file_parts_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fileSize": file_size,
            "fileHash": file_hash,
            "fileParts": file_parts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_file_part_info import BatchFilePartInfo
        d = dict(src_dict)
        file_size = d.pop("fileSize")

        file_hash = d.pop("fileHash")

        file_parts = []
        _file_parts = d.pop("fileParts")
        for file_parts_item_data in (_file_parts):
            file_parts_item = BatchFilePartInfo.from_dict(file_parts_item_data)



            file_parts.append(file_parts_item)


        batch_file_info = cls(
            file_size=file_size,
            file_hash=file_hash,
            file_parts=file_parts,
        )

        return batch_file_info

