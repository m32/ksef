from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.third_subject_identifier_type import ThirdSubjectIdentifierType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="InvoiceMetadataThirdSubjectIdentifier")



@_attrs_define
class InvoiceMetadataThirdSubjectIdentifier:
    """ 
        Attributes:
            type_ (ThirdSubjectIdentifierType): | Wartość | Opis |
                | --- | --- |
                | Nip | Nip |
                | InternalId | Identyfikator wewnętrzny |
                | VatUe | VAT UE |
                | Other | Inny identyfikator |
                | None | Brak identyfikatora podmiotu trzeciego |
            value (Union[None, Unset, str]): Wartość identyfikatora podmiotu trzeciego.
     """

    type_: ThirdSubjectIdentifierType
    value: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ThirdSubjectIdentifierType(d.pop("type"))




        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))


        invoice_metadata_third_subject_identifier = cls(
            type_=type_,
            value=value,
        )

        return invoice_metadata_third_subject_identifier

