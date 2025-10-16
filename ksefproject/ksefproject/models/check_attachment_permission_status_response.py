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






T = TypeVar("T", bound="CheckAttachmentPermissionStatusResponse")



@_attrs_define
class CheckAttachmentPermissionStatusResponse:
    """ 
        Attributes:
            is_attachment_allowed (Union[Unset, bool]): Informacja czy Podmiot ma obecnie możliwość dodawania Załączników do
                Faktur
            revoked_date (Union[None, Unset, datetime.datetime]): Data i czas zakończenia możliwość dodawania przez Podmiot
                Załączników do Faktur.
                Brak podanej daty oznacza bezterminową możliwość dodawania Załączników do Faktur
     """

    is_attachment_allowed: Union[Unset, bool] = UNSET
    revoked_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_attachment_allowed = self.is_attachment_allowed

        revoked_date: Union[None, Unset, str]
        if isinstance(self.revoked_date, Unset):
            revoked_date = UNSET
        elif isinstance(self.revoked_date, datetime.datetime):
            revoked_date = self.revoked_date.isoformat()
        else:
            revoked_date = self.revoked_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_attachment_allowed is not UNSET:
            field_dict["isAttachmentAllowed"] = is_attachment_allowed
        if revoked_date is not UNSET:
            field_dict["revokedDate"] = revoked_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_attachment_allowed = d.pop("isAttachmentAllowed", UNSET)

        def _parse_revoked_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_date_type_0 = isoparse(data)



                return revoked_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        revoked_date = _parse_revoked_date(d.pop("revokedDate", UNSET))


        check_attachment_permission_status_response = cls(
            is_attachment_allowed=is_attachment_allowed,
            revoked_date=revoked_date,
        )

        return check_attachment_permission_status_response

