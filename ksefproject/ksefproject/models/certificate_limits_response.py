from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.certificate_limit import CertificateLimit





T = TypeVar("T", bound="CertificateLimitsResponse")



@_attrs_define
class CertificateLimitsResponse:
    """ Informacje o limitach wniosków oraz certyfikatów dla uwierzytelnionego podmiotu.

        Attributes:
            can_request (bool): Flaga informująca czy uwierzytelniony podmiot może złożyć nowy wniosek o certyfikat.
            enrollment (CertificateLimit):
            certificate (CertificateLimit):
     """

    can_request: bool
    enrollment: 'CertificateLimit'
    certificate: 'CertificateLimit'





    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_limit import CertificateLimit
        can_request = self.can_request

        enrollment = self.enrollment.to_dict()

        certificate = self.certificate.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "canRequest": can_request,
            "enrollment": enrollment,
            "certificate": certificate,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_limit import CertificateLimit
        d = dict(src_dict)
        can_request = d.pop("canRequest")

        enrollment = CertificateLimit.from_dict(d.pop("enrollment"))




        certificate = CertificateLimit.from_dict(d.pop("certificate"))




        certificate_limits_response = cls(
            can_request=can_request,
            enrollment=enrollment,
            certificate=certificate,
        )

        return certificate_limits_response

