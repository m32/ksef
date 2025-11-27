from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_query_date_type import InvoiceQueryDateType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="InvoiceQueryDateRange")



@_attrs_define
class InvoiceQueryDateRange:
    """ 
        Attributes:
            date_type (InvoiceQueryDateType): | Wartość | Opis |
                | --- | --- |
                | Issue | Data wystawienia faktury. |
                | Invoicing | Data przyjęcia faktury w systemie KSeF (do dalszego przetwarzania). |
                | PermanentStorage | Data trwałego zapisu faktury w repozytorium systemu KSeF. |
            from_ (datetime.datetime): Data początkowa zakresu(UTC).
            to (Union[None, Unset, datetime.datetime]): Data końcowa zakresu(UTC). Jeśli nie zostanie podana, przyjmowana
                jest bieżąca data i czas w UTC.
     """

    date_type: InvoiceQueryDateType
    from_: datetime.datetime
    to: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        date_type = self.date_type.value

        from_ = self.from_.isoformat()

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "dateType": date_type,
            "from": from_,
        })
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_type = InvoiceQueryDateType(d.pop("dateType"))




        from_ = isoparse(d.pop("from"))




        def _parse_to(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = isoparse(data)



                return to_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        to = _parse_to(d.pop("to", UNSET))


        invoice_query_date_range = cls(
            date_type=date_type,
            from_=from_,
            to=to,
        )

        return invoice_query_date_range

