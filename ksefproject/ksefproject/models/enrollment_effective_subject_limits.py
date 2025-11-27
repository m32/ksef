from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="EnrollmentEffectiveSubjectLimits")



@_attrs_define
class EnrollmentEffectiveSubjectLimits:
    """ 
        Attributes:
            max_enrollments (Union[Unset, int]):
     """

    max_enrollments: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        max_enrollments = self.max_enrollments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_enrollments is not UNSET:
            field_dict["maxEnrollments"] = max_enrollments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_enrollments = d.pop("maxEnrollments", UNSET)

        enrollment_effective_subject_limits = cls(
            max_enrollments=max_enrollments,
        )

        return enrollment_effective_subject_limits

