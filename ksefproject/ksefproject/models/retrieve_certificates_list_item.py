from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ksef_certificate_type import KsefCertificateType






T = TypeVar("T", bound="RetrieveCertificatesListItem")



@_attrs_define
class RetrieveCertificatesListItem:
    """ 
        Attributes:
            certificate (str): Certyfikat w formacie DER zakodowany w Base64.
            certificate_name (str): Nazwa własna certyfikatu.
            certificate_serial_number (str): Numer seryjny certyfikatu.
            certificate_type (KsefCertificateType): | Wartość | Opis |
                | --- | --- |
                | Authentication | Certyfikat używany do uwierzytelnienia w systemie. |
                | Offline | Certyfikat używany wyłącznie do potwierdzania autentyczności wystawcy i integralności faktury w
                trybie offline |
     """

    certificate: str
    certificate_name: str
    certificate_serial_number: str
    certificate_type: KsefCertificateType





    def to_dict(self) -> dict[str, Any]:
        certificate = self.certificate

        certificate_name = self.certificate_name

        certificate_serial_number = self.certificate_serial_number

        certificate_type = self.certificate_type.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificate": certificate,
            "certificateName": certificate_name,
            "certificateSerialNumber": certificate_serial_number,
            "certificateType": certificate_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate = d.pop("certificate")

        certificate_name = d.pop("certificateName")

        certificate_serial_number = d.pop("certificateSerialNumber")

        certificate_type = KsefCertificateType(d.pop("certificateType"))




        retrieve_certificates_list_item = cls(
            certificate=certificate,
            certificate_name=certificate_name,
            certificate_serial_number=certificate_serial_number,
            certificate_type=certificate_type,
        )

        return retrieve_certificates_list_item

