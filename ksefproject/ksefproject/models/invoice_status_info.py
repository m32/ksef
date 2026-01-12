from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.invoice_status_info_extensions_type_0 import InvoiceStatusInfoExtensionsType0





T = TypeVar("T", bound="InvoiceStatusInfo")



@_attrs_define
class InvoiceStatusInfo:
    """ 
        Attributes:
            code (int): Kod statusu faktury
            description (str): Opis statusu
            details (Union[None, Unset, list[str]]): Dodatkowe szczegóły statusu
            extensions (Union['InvoiceStatusInfoExtensionsType0', None, Unset]): Zbiór dodatkowych informacji związanych ze
                statusem faktury, zapisanych jako pary klucz–wartość.
                Umożliwia rozszerzenie modelu o dane specyficzne dla danego przypadku.
     """

    code: int
    description: str
    details: Union[None, Unset, list[str]] = UNSET
    extensions: Union['InvoiceStatusInfoExtensionsType0', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_status_info_extensions_type_0 import InvoiceStatusInfoExtensionsType0
        code = self.code

        description = self.description

        details: Union[None, Unset, list[str]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details


        else:
            details = self.details

        extensions: Union[None, Unset, dict[str, Any]]
        if isinstance(self.extensions, Unset):
            extensions = UNSET
        elif isinstance(self.extensions, InvoiceStatusInfoExtensionsType0):
            extensions = self.extensions.to_dict()
        else:
            extensions = self.extensions


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "description": description,
        })
        if details is not UNSET:
            field_dict["details"] = details
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_status_info_extensions_type_0 import InvoiceStatusInfoExtensionsType0
        d = dict(src_dict)
        code = d.pop("code")

        description = d.pop("description")

        def _parse_details(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        details = _parse_details(d.pop("details", UNSET))


        def _parse_extensions(data: object) -> Union['InvoiceStatusInfoExtensionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extensions_type_0 = InvoiceStatusInfoExtensionsType0.from_dict(data)



                return extensions_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvoiceStatusInfoExtensionsType0', None, Unset], data)

        extensions = _parse_extensions(d.pop("extensions", UNSET))


        invoice_status_info = cls(
            code=code,
            description=description,
            details=details,
            extensions=extensions,
        )

        return invoice_status_info

