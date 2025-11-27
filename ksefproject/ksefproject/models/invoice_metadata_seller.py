from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="InvoiceMetadataSeller")



@_attrs_define
class InvoiceMetadataSeller:
    """ 
        Attributes:
            nip (str): 10 cyfrowy numer NIP.
            name (Union[None, Unset, str]): Nazwa sprzedawcy.
     """

    nip: str
    name: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        nip = self.nip

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "nip": nip,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nip = d.pop("nip")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        invoice_metadata_seller = cls(
            nip=nip,
            name=name,
        )

        return invoice_metadata_seller

