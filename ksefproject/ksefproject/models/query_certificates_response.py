from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.certificate_list_item import CertificateListItem





T = TypeVar("T", bound="QueryCertificatesResponse")



@_attrs_define
class QueryCertificatesResponse:
    """ 
        Attributes:
            certificates (list['CertificateListItem']): Lista certyfikatów spełniających kryteria wyszukiwania.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    certificates: list['CertificateListItem']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_list_item import CertificateListItem
        certificates = []
        for certificates_item_data in self.certificates:
            certificates_item = certificates_item_data.to_dict()
            certificates.append(certificates_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificates": certificates,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_list_item import CertificateListItem
        d = dict(src_dict)
        certificates = []
        _certificates = d.pop("certificates")
        for certificates_item_data in (_certificates):
            certificates_item = CertificateListItem.from_dict(certificates_item_data)



            certificates.append(certificates_item)


        has_more = d.pop("hasMore")

        query_certificates_response = cls(
            certificates=certificates,
            has_more=has_more,
        )

        return query_certificates_response

