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
  from ..models.exception_info import ExceptionInfo





T = TypeVar("T", bound="ExceptionResponse")



@_attrs_define
class ExceptionResponse:
    """ 
        Example:
            {'Exception': {'ExceptionDetailList': [{'ExceptionCode': 12345, 'ExceptionDescription': 'Opis błędu.',
                'Details': ['Opcjonalne dodatkowe szczegóły błędu.']}], 'ReferenceNumber':
                'a1b2c3d4-e5f6-4789-ab12-cd34ef567890', 'ServiceCode':
                '00-c02cc3747020c605be02159bf3324f0e-eee7647dc67aa74a-00', 'ServiceCtx': 'srvABCDA', 'ServiceName': 'Undefined',
                'Timestamp': '2025-10-11T12:23:56.0154302'}}

        Attributes:
            exception (Union['ExceptionInfo', None, Unset]):
     """

    exception: Union['ExceptionInfo', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.exception_info import ExceptionInfo
        exception: Union[None, Unset, dict[str, Any]]
        if isinstance(self.exception, Unset):
            exception = UNSET
        elif isinstance(self.exception, ExceptionInfo):
            exception = self.exception.to_dict()
        else:
            exception = self.exception


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exception_info import ExceptionInfo
        d = dict(src_dict)
        def _parse_exception(data: object) -> Union['ExceptionInfo', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exception_type_1 = ExceptionInfo.from_dict(data)



                return exception_type_1
            except: # noqa: E722
                pass
            return cast(Union['ExceptionInfo', None, Unset], data)

        exception = _parse_exception(d.pop("exception", UNSET))


        exception_response = cls(
            exception=exception,
        )

        return exception_response

