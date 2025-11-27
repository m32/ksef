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
  from ..models.certificate_effective_subject_limits import CertificateEffectiveSubjectLimits
  from ..models.enrollment_effective_subject_limits import EnrollmentEffectiveSubjectLimits





T = TypeVar("T", bound="EffectiveSubjectLimits")



@_attrs_define
class EffectiveSubjectLimits:
    """ 
        Attributes:
            enrollment (Union['EnrollmentEffectiveSubjectLimits', None, Unset]):
            certificate (Union['CertificateEffectiveSubjectLimits', None, Unset]):
     """

    enrollment: Union['EnrollmentEffectiveSubjectLimits', None, Unset] = UNSET
    certificate: Union['CertificateEffectiveSubjectLimits', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_effective_subject_limits import CertificateEffectiveSubjectLimits
        from ..models.enrollment_effective_subject_limits import EnrollmentEffectiveSubjectLimits
        enrollment: Union[None, Unset, dict[str, Any]]
        if isinstance(self.enrollment, Unset):
            enrollment = UNSET
        elif isinstance(self.enrollment, EnrollmentEffectiveSubjectLimits):
            enrollment = self.enrollment.to_dict()
        else:
            enrollment = self.enrollment

        certificate: Union[None, Unset, dict[str, Any]]
        if isinstance(self.certificate, Unset):
            certificate = UNSET
        elif isinstance(self.certificate, CertificateEffectiveSubjectLimits):
            certificate = self.certificate.to_dict()
        else:
            certificate = self.certificate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if certificate is not UNSET:
            field_dict["certificate"] = certificate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_effective_subject_limits import CertificateEffectiveSubjectLimits
        from ..models.enrollment_effective_subject_limits import EnrollmentEffectiveSubjectLimits
        d = dict(src_dict)
        def _parse_enrollment(data: object) -> Union['EnrollmentEffectiveSubjectLimits', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                enrollment_type_1 = EnrollmentEffectiveSubjectLimits.from_dict(data)



                return enrollment_type_1
            except: # noqa: E722
                pass
            return cast(Union['EnrollmentEffectiveSubjectLimits', None, Unset], data)

        enrollment = _parse_enrollment(d.pop("enrollment", UNSET))


        def _parse_certificate(data: object) -> Union['CertificateEffectiveSubjectLimits', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                certificate_type_1 = CertificateEffectiveSubjectLimits.from_dict(data)



                return certificate_type_1
            except: # noqa: E722
                pass
            return cast(Union['CertificateEffectiveSubjectLimits', None, Unset], data)

        certificate = _parse_certificate(d.pop("certificate", UNSET))


        effective_subject_limits = cls(
            enrollment=enrollment,
            certificate=certificate,
        )

        return effective_subject_limits

