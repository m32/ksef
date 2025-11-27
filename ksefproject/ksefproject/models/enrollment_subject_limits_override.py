from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="EnrollmentSubjectLimitsOverride")



@_attrs_define
class EnrollmentSubjectLimitsOverride:
    """ 
        Attributes:
            max_enrollments (Union[None, Unset, int]):
     """

    max_enrollments: Union[None, Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        max_enrollments: Union[None, Unset, int]
        if isinstance(self.max_enrollments, Unset):
            max_enrollments = UNSET
        else:
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
        def _parse_max_enrollments(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_enrollments = _parse_max_enrollments(d.pop("maxEnrollments", UNSET))


        enrollment_subject_limits_override = cls(
            max_enrollments=max_enrollments,
        )

        return enrollment_subject_limits_override

