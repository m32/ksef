from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.form_code import FormCode
  from ..models.encryption_info import EncryptionInfo





T = TypeVar("T", bound="OpenOnlineSessionRequest")



@_attrs_define
class OpenOnlineSessionRequest:
    """ 
        Attributes:
            form_code (FormCode):
            encryption (EncryptionInfo):
     """

    form_code: 'FormCode'
    encryption: 'EncryptionInfo'





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_code import FormCode
        from ..models.encryption_info import EncryptionInfo
        form_code = self.form_code.to_dict()

        encryption = self.encryption.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "formCode": form_code,
            "encryption": encryption,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_code import FormCode
        from ..models.encryption_info import EncryptionInfo
        d = dict(src_dict)
        form_code = FormCode.from_dict(d.pop("formCode"))




        encryption = EncryptionInfo.from_dict(d.pop("encryption"))




        open_online_session_request = cls(
            form_code=form_code,
            encryption=encryption,
        )

        return open_online_session_request

