from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.retrieve_certificates_list_item import RetrieveCertificatesListItem





T = TypeVar("T", bound="RetrieveCertificatesResponse")



@_attrs_define
class RetrieveCertificatesResponse:
    """ 
        Attributes:
            certificates (list['RetrieveCertificatesListItem']): Pobrane certyfikaty.
     """

    certificates: list['RetrieveCertificatesListItem']





    def to_dict(self) -> dict[str, Any]:
        from ..models.retrieve_certificates_list_item import RetrieveCertificatesListItem
        certificates = []
        for certificates_item_data in self.certificates:
            certificates_item = certificates_item_data.to_dict()
            certificates.append(certificates_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificates": certificates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retrieve_certificates_list_item import RetrieveCertificatesListItem
        d = dict(src_dict)
        certificates = []
        _certificates = d.pop("certificates")
        for certificates_item_data in (_certificates):
            certificates_item = RetrieveCertificatesListItem.from_dict(certificates_item_data)



            certificates.append(certificates_item)


        retrieve_certificates_response = cls(
            certificates=certificates,
        )

        return retrieve_certificates_response

