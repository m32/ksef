from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subject_identifier_type import SubjectIdentifierType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.certificate_subject_limits_override import CertificateSubjectLimitsOverride
  from ..models.enrollment_subject_limits_override import EnrollmentSubjectLimitsOverride





T = TypeVar("T", bound="SetSubjectLimitsRequest")



@_attrs_define
class SetSubjectLimitsRequest:
    """ 
        Attributes:
            subject_identifier_type (Union[Unset, SubjectIdentifierType]):
            enrollment (Union['EnrollmentSubjectLimitsOverride', None, Unset]):
            certificate (Union['CertificateSubjectLimitsOverride', None, Unset]):
     """

    subject_identifier_type: Union[Unset, SubjectIdentifierType] = UNSET
    enrollment: Union['EnrollmentSubjectLimitsOverride', None, Unset] = UNSET
    certificate: Union['CertificateSubjectLimitsOverride', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_subject_limits_override import CertificateSubjectLimitsOverride
        from ..models.enrollment_subject_limits_override import EnrollmentSubjectLimitsOverride
        subject_identifier_type: Union[Unset, str] = UNSET
        if not isinstance(self.subject_identifier_type, Unset):
            subject_identifier_type = self.subject_identifier_type.value


        enrollment: Union[None, Unset, dict[str, Any]]
        if isinstance(self.enrollment, Unset):
            enrollment = UNSET
        elif isinstance(self.enrollment, EnrollmentSubjectLimitsOverride):
            enrollment = self.enrollment.to_dict()
        else:
            enrollment = self.enrollment

        certificate: Union[None, Unset, dict[str, Any]]
        if isinstance(self.certificate, Unset):
            certificate = UNSET
        elif isinstance(self.certificate, CertificateSubjectLimitsOverride):
            certificate = self.certificate.to_dict()
        else:
            certificate = self.certificate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subject_identifier_type is not UNSET:
            field_dict["subjectIdentifierType"] = subject_identifier_type
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if certificate is not UNSET:
            field_dict["certificate"] = certificate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_subject_limits_override import CertificateSubjectLimitsOverride
        from ..models.enrollment_subject_limits_override import EnrollmentSubjectLimitsOverride
        d = dict(src_dict)
        _subject_identifier_type = d.pop("subjectIdentifierType", UNSET)
        subject_identifier_type: Union[Unset, SubjectIdentifierType]
        if isinstance(_subject_identifier_type,  Unset):
            subject_identifier_type = UNSET
        else:
            subject_identifier_type = SubjectIdentifierType(_subject_identifier_type)




        def _parse_enrollment(data: object) -> Union['EnrollmentSubjectLimitsOverride', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                enrollment_type_1 = EnrollmentSubjectLimitsOverride.from_dict(data)



                return enrollment_type_1
            except: # noqa: E722
                pass
            return cast(Union['EnrollmentSubjectLimitsOverride', None, Unset], data)

        enrollment = _parse_enrollment(d.pop("enrollment", UNSET))


        def _parse_certificate(data: object) -> Union['CertificateSubjectLimitsOverride', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                certificate_type_1 = CertificateSubjectLimitsOverride.from_dict(data)



                return certificate_type_1
            except: # noqa: E722
                pass
            return cast(Union['CertificateSubjectLimitsOverride', None, Unset], data)

        certificate = _parse_certificate(d.pop("certificate", UNSET))


        set_subject_limits_request = cls(
            subject_identifier_type=subject_identifier_type,
            enrollment=enrollment,
            certificate=certificate,
        )

        return set_subject_limits_request

