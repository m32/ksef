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






T = TypeVar("T", bound="PersonCreateRequest")



@_attrs_define
class PersonCreateRequest:
    """ 
        Attributes:
            nip (Union[None, Unset, str]):
            pesel (Union[None, Unset, str]):
            is_bailiff (Union[Unset, bool]):
            description (Union[None, Unset, str]):
            created_date (Union[None, Unset, datetime.datetime]):
     """

    nip: Union[None, Unset, str] = UNSET
    pesel: Union[None, Unset, str] = UNSET
    is_bailiff: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        nip: Union[None, Unset, str]
        if isinstance(self.nip, Unset):
            nip = UNSET
        else:
            nip = self.nip

        pesel: Union[None, Unset, str]
        if isinstance(self.pesel, Unset):
            pesel = UNSET
        else:
            pesel = self.pesel

        is_bailiff = self.is_bailiff

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if nip is not UNSET:
            field_dict["nip"] = nip
        if pesel is not UNSET:
            field_dict["pesel"] = pesel
        if is_bailiff is not UNSET:
            field_dict["isBailiff"] = is_bailiff
        if description is not UNSET:
            field_dict["description"] = description
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_nip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nip = _parse_nip(d.pop("nip", UNSET))


        def _parse_pesel(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pesel = _parse_pesel(d.pop("pesel", UNSET))


        is_bailiff = d.pop("isBailiff", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)



                return created_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))


        person_create_request = cls(
            nip=nip,
            pesel=pesel,
            is_bailiff=is_bailiff,
            description=description,
            created_date=created_date,
        )

        return person_create_request

