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
  from ..models.session_invoice_status_response import SessionInvoiceStatusResponse





T = TypeVar("T", bound="SessionInvoicesResponse")



@_attrs_define
class SessionInvoicesResponse:
    """ 
        Attributes:
            invoices (list['SessionInvoiceStatusResponse']): Lista pobranych faktur.
            continuation_token (Union[None, Unset, str]): Token służący do pobrania kolejnej strony wyników. Jeśli jest
                pusty, to nie ma kolejnych stron.
     """

    invoices: list['SessionInvoiceStatusResponse']
    continuation_token: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_invoice_status_response import SessionInvoiceStatusResponse
        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)



        continuation_token: Union[None, Unset, str]
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "invoices": invoices,
        })
        if continuation_token is not UNSET:
            field_dict["continuationToken"] = continuation_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_invoice_status_response import SessionInvoiceStatusResponse
        d = dict(src_dict)
        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in (_invoices):
            invoices_item = SessionInvoiceStatusResponse.from_dict(invoices_item_data)



            invoices.append(invoices_item)


        def _parse_continuation_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        continuation_token = _parse_continuation_token(d.pop("continuationToken", UNSET))


        session_invoices_response = cls(
            invoices=invoices,
            continuation_token=continuation_token,
        )

        return session_invoices_response

