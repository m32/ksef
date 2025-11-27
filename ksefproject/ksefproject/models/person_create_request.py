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
            nip (str): 10 cyfrowy numer NIP.
            pesel (str): 11 cyfrowy numer PESEL.
            is_bailiff (bool):
            description (str):
            is_deceased (Union[Unset, bool]):
            created_date (Union[None, Unset, datetime.datetime]): W przypadku wielokrotnego tworzenia danych testowych z tym
                samym identyfikatorem nie można podawać daty wcześniejszej ani takiej samej jak poprzednia.
     """

    nip: str
    pesel: str
    is_bailiff: bool
    description: str
    is_deceased: Union[Unset, bool] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        nip = self.nip

        pesel = self.pesel

        is_bailiff = self.is_bailiff

        description = self.description

        is_deceased = self.is_deceased

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "nip": nip,
            "pesel": pesel,
            "isBailiff": is_bailiff,
            "description": description,
        })
        if is_deceased is not UNSET:
            field_dict["isDeceased"] = is_deceased
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nip = d.pop("nip")

        pesel = d.pop("pesel")

        is_bailiff = d.pop("isBailiff")

        description = d.pop("description")

        is_deceased = d.pop("isDeceased", UNSET)

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
            is_deceased=is_deceased,
            created_date=created_date,
        )

        return person_create_request

