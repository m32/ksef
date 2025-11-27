from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CertificateEffectiveSubjectLimits")



@_attrs_define
class CertificateEffectiveSubjectLimits:
    """ 
        Attributes:
            max_certificates (Union[Unset, int]):
     """

    max_certificates: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        max_certificates = self.max_certificates


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_certificates is not UNSET:
            field_dict["maxCertificates"] = max_certificates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_certificates = d.pop("maxCertificates", UNSET)

        certificate_effective_subject_limits = cls(
            max_certificates=max_certificates,
        )

        return certificate_effective_subject_limits

