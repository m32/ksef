from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from dateutil.parser import isoparse
from typing import cast
import datetime
from ..types import UNSET, Unset






T = TypeVar("T", bound="QueryPaymentCriteriaType")


@_attrs_define
class QueryPaymentCriteriaType:
    """ 
        Attributes:
            created_date_from (Union[Unset, datetime.datetime]): yyyy-MM-dd'T'HH:mm:ss
            created_date_to (Union[Unset, datetime.datetime]): yyyy-MM-dd'T'HH:mm:ss
            number_of_invoice_from (Union[Unset, int]):
            number_of_invoice_to (Union[Unset, int]):
            payment_identifier (Union[Unset, str]):
     """

    created_date_from: Union[Unset, datetime.datetime] = UNSET
    created_date_to: Union[Unset, datetime.datetime] = UNSET
    number_of_invoice_from: Union[Unset, int] = UNSET
    number_of_invoice_to: Union[Unset, int] = UNSET
    payment_identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_date_from: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_from, Unset):
            created_date_from = self.created_date_from.isoformat()

        created_date_to: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_to, Unset):
            created_date_to = self.created_date_to.isoformat()

        number_of_invoice_from = self.number_of_invoice_from
        number_of_invoice_to = self.number_of_invoice_to
        payment_identifier = self.payment_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_date_from is not UNSET:
            field_dict["createdDateFrom"] = created_date_from
        if created_date_to is not UNSET:
            field_dict["createdDateTo"] = created_date_to
        if number_of_invoice_from is not UNSET:
            field_dict["numberOfInvoiceFrom"] = number_of_invoice_from
        if number_of_invoice_to is not UNSET:
            field_dict["numberOfInvoiceTo"] = number_of_invoice_to
        if payment_identifier is not UNSET:
            field_dict["paymentIdentifier"] = payment_identifier

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_date_from = d.pop("createdDateFrom", UNSET)
        created_date_from: Union[Unset, datetime.datetime]
        if isinstance(_created_date_from,  Unset):
            created_date_from = UNSET
        else:
            created_date_from = isoparse(_created_date_from)




        _created_date_to = d.pop("createdDateTo", UNSET)
        created_date_to: Union[Unset, datetime.datetime]
        if isinstance(_created_date_to,  Unset):
            created_date_to = UNSET
        else:
            created_date_to = isoparse(_created_date_to)




        number_of_invoice_from = d.pop("numberOfInvoiceFrom", UNSET)

        number_of_invoice_to = d.pop("numberOfInvoiceTo", UNSET)

        payment_identifier = d.pop("paymentIdentifier", UNSET)

        query_payment_criteria_type = cls(
            created_date_from=created_date_from,
            created_date_to=created_date_to,
            number_of_invoice_from=number_of_invoice_from,
            number_of_invoice_to=number_of_invoice_to,
            payment_identifier=payment_identifier,
        )

        query_payment_criteria_type.additional_properties = d
        return query_payment_criteria_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
