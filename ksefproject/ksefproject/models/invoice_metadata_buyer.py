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
  from ..models.invoice_metadata_buyer_identifier import InvoiceMetadataBuyerIdentifier





T = TypeVar("T", bound="InvoiceMetadataBuyer")



@_attrs_define
class InvoiceMetadataBuyer:
    """ 
        Attributes:
            identifier (InvoiceMetadataBuyerIdentifier):
            name (Union[None, Unset, str]): Nazwa nabywcy.
     """

    identifier: 'InvoiceMetadataBuyerIdentifier'
    name: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_metadata_buyer_identifier import InvoiceMetadataBuyerIdentifier
        identifier = self.identifier.to_dict()

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "identifier": identifier,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_metadata_buyer_identifier import InvoiceMetadataBuyerIdentifier
        d = dict(src_dict)
        identifier = InvoiceMetadataBuyerIdentifier.from_dict(d.pop("identifier"))




        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        invoice_metadata_buyer = cls(
            identifier=identifier,
            name=name,
        )

        return invoice_metadata_buyer

