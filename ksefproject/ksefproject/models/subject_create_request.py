from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subject_type import SubjectType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.subunit import Subunit





T = TypeVar("T", bound="SubjectCreateRequest")



@_attrs_define
class SubjectCreateRequest:
    """ 
        Attributes:
            subject_nip (str): 10 cyfrowy numer NIP.
            subject_type (SubjectType):
            description (str):
            subunits (Union[None, Unset, list['Subunit']]):
            created_date (Union[None, Unset, datetime.datetime]): W przypadku wielokrotnego tworzenia danych testowych z tym
                samym identyfikatorem nie można podawać daty wcześniejszej ani takiej samej jak poprzednia.
     """

    subject_nip: str
    subject_type: SubjectType
    description: str
    subunits: Union[None, Unset, list['Subunit']] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.subunit import Subunit
        subject_nip = self.subject_nip

        subject_type = self.subject_type.value

        description = self.description

        subunits: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.subunits, Unset):
            subunits = UNSET
        elif isinstance(self.subunits, list):
            subunits = []
            for subunits_type_0_item_data in self.subunits:
                subunits_type_0_item = subunits_type_0_item_data.to_dict()
                subunits.append(subunits_type_0_item)


        else:
            subunits = self.subunits

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectNip": subject_nip,
            "subjectType": subject_type,
            "description": description,
        })
        if subunits is not UNSET:
            field_dict["subunits"] = subunits
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subunit import Subunit
        d = dict(src_dict)
        subject_nip = d.pop("subjectNip")

        subject_type = SubjectType(d.pop("subjectType"))




        description = d.pop("description")

        def _parse_subunits(data: object) -> Union[None, Unset, list['Subunit']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subunits_type_0 = []
                _subunits_type_0 = data
                for subunits_type_0_item_data in (_subunits_type_0):
                    subunits_type_0_item = Subunit.from_dict(subunits_type_0_item_data)



                    subunits_type_0.append(subunits_type_0_item)

                return subunits_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['Subunit']], data)

        subunits = _parse_subunits(d.pop("subunits", UNSET))


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


        subject_create_request = cls(
            subject_nip=subject_nip,
            subject_type=subject_type,
            description=description,
            subunits=subunits,
            created_date=created_date,
        )

        return subject_create_request

