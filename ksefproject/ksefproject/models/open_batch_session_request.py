from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.form_code import FormCode
  from ..models.batch_file_info import BatchFileInfo
  from ..models.encryption_info import EncryptionInfo





T = TypeVar("T", bound="OpenBatchSessionRequest")



@_attrs_define
class OpenBatchSessionRequest:
    """ 
        Attributes:
            form_code (FormCode):
            batch_file (BatchFileInfo):
            encryption (EncryptionInfo):
            offline_mode (Union[Unset, bool]): Określa, czy podatnik deklaruje tryb fakurowania "offline" dla dokumentów
                przesyłanych w sesji wsadowej. Default: False.
     """

    form_code: 'FormCode'
    batch_file: 'BatchFileInfo'
    encryption: 'EncryptionInfo'
    offline_mode: Union[Unset, bool] = False





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_code import FormCode
        from ..models.batch_file_info import BatchFileInfo
        from ..models.encryption_info import EncryptionInfo
        form_code = self.form_code.to_dict()

        batch_file = self.batch_file.to_dict()

        encryption = self.encryption.to_dict()

        offline_mode = self.offline_mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "formCode": form_code,
            "batchFile": batch_file,
            "encryption": encryption,
        })
        if offline_mode is not UNSET:
            field_dict["offlineMode"] = offline_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_code import FormCode
        from ..models.batch_file_info import BatchFileInfo
        from ..models.encryption_info import EncryptionInfo
        d = dict(src_dict)
        form_code = FormCode.from_dict(d.pop("formCode"))




        batch_file = BatchFileInfo.from_dict(d.pop("batchFile"))




        encryption = EncryptionInfo.from_dict(d.pop("encryption"))




        offline_mode = d.pop("offlineMode", UNSET)

        open_batch_session_request = cls(
            form_code=form_code,
            batch_file=batch_file,
            encryption=encryption,
            offline_mode=offline_mode,
        )

        return open_batch_session_request

