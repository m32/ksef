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
  from ..models.invoice_metadata_third_subject_identifier import InvoiceMetadataThirdSubjectIdentifier





T = TypeVar("T", bound="InvoiceMetadataThirdSubject")



@_attrs_define
class InvoiceMetadataThirdSubject:
    """ 
        Attributes:
            identifier (InvoiceMetadataThirdSubjectIdentifier):
            role (int): Rola podmiotu trzeciego.
            name (Union[None, Unset, str]): Nazwa podmiotu trzeciego.
     """

    identifier: 'InvoiceMetadataThirdSubjectIdentifier'
    role: int
    name: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_metadata_third_subject_identifier import InvoiceMetadataThirdSubjectIdentifier
        identifier = self.identifier.to_dict()

        role = self.role

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "identifier": identifier,
            "role": role,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_metadata_third_subject_identifier import InvoiceMetadataThirdSubjectIdentifier
        d = dict(src_dict)
        identifier = InvoiceMetadataThirdSubjectIdentifier.from_dict(d.pop("identifier"))




        role = d.pop("role")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        invoice_metadata_third_subject = cls(
            identifier=identifier,
            role=role,
            name=name,
        )

        return invoice_metadata_third_subject

