from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="AttachmentPermissionRevokeRequest")



@_attrs_define
class AttachmentPermissionRevokeRequest:
    """ 
        Attributes:
            nip (str): 10 cyfrowy numer NIP.
            expected_end_date (Union[None, Unset, datetime.date]): Data wycofania zgody na przesyłanie faktur z
                załącznikiem.
     """

    nip: str
    expected_end_date: Union[None, Unset, datetime.date] = UNSET





    def to_dict(self) -> dict[str, Any]:
        nip = self.nip

        expected_end_date: Union[None, Unset, str]
        if isinstance(self.expected_end_date, Unset):
            expected_end_date = UNSET
        elif isinstance(self.expected_end_date, datetime.date):
            expected_end_date = self.expected_end_date.isoformat()
        else:
            expected_end_date = self.expected_end_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "nip": nip,
        })
        if expected_end_date is not UNSET:
            field_dict["expectedEndDate"] = expected_end_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nip = d.pop("nip")

        def _parse_expected_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_end_date_type_0 = isoparse(data).date()



                return expected_end_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        expected_end_date = _parse_expected_end_date(d.pop("expectedEndDate", UNSET))


        attachment_permission_revoke_request = cls(
            nip=nip,
            expected_end_date=expected_end_date,
        )

        return attachment_permission_revoke_request

