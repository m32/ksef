from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CertificateSubjectLimitsOverride")



@_attrs_define
class CertificateSubjectLimitsOverride:
    """ 
        Attributes:
            max_certificates (Union[None, Unset, int]):
     """

    max_certificates: Union[None, Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        max_certificates: Union[None, Unset, int]
        if isinstance(self.max_certificates, Unset):
            max_certificates = UNSET
        else:
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
        def _parse_max_certificates(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_certificates = _parse_max_certificates(d.pop("maxCertificates", UNSET))


        certificate_subject_limits_override = cls(
            max_certificates=max_certificates,
        )

        return certificate_subject_limits_override

