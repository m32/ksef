from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.amount_type import AmountType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="InvoiceQueryAmount")



@_attrs_define
class InvoiceQueryAmount:
    """ 
        Attributes:
            type_ (AmountType):
            from_ (Union[None, Unset, float]):
            to (Union[None, Unset, float]):
     """

    type_: AmountType
    from_: Union[None, Unset, float] = UNSET
    to: Union[None, Unset, float] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        from_: Union[None, Unset, float]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: Union[None, Unset, float]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AmountType(d.pop("type"))




        def _parse_from_(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_to(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        to = _parse_to(d.pop("to", UNSET))


        invoice_query_amount = cls(
            type_=type_,
            from_=from_,
            to=to,
        )

        return invoice_query_amount

