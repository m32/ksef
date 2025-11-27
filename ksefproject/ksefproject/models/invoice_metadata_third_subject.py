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
                | Wartość | Opis |
                | ---- | --- |
                | 0 | Inna rola |
                | 1 | Faktor - w przypadku gdy na fakturze występują dane faktora |
                | 2 | Odbiorca - w przypadku gdy na fakturze występują dane jednostek wewnętrznych, oddziałów, wyodrębnionych w
                ramach nabywcy, które same nie stanowią nabywcy w rozumieniu ustawy |
                | 3 | Podmiot pierwotny - w przypadku gdy na fakturze występują dane podmiotu będącego w stosunku do podatnika
                podmiotem przejętym lub przekształconym, który dokonywał dostawy lub świadczył usługę. Z wyłączeniem przypadków,
                o których mowa w art. 106j ust.2 pkt 3 ustawy, gdy dane te wykazywane są w części Podmiot1K |
                | 4 | Dodatkowy nabywca - w przypadku gdy na fakturze występują dane kolejnych (innych niż wymieniony w części
                Podmiot2) nabywców |
                | 5 | Wystawca faktury - w przypadku gdy na fakturze występują dane podmiotu wystawiającego fakturę w imieniu
                podatnika. Nie dotyczy przypadku, gdy wystawcą faktury jest nabywca |
                | 6 | Dokonujący płatności - w przypadku gdy na fakturze występują dane podmiotu regulującego zobowiązanie w
                miejsce nabywcy |
                | 7 | Jednostka samorządu terytorialnego - wystawca |
                | 8 | Jednostka samorządu terytorialnego - odbiorca |
                | 9 | Członek grupy VAT - wystawca |
                | 10 | Członek grupy VAT - odbiorca |
                | 11 | Pracownik |
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

