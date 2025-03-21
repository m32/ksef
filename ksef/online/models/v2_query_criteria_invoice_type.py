from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from dateutil.parser import isoparse
from ..models.v2_query_criteria_invoice_type_subject_type import V2QueryCriteriaInvoiceTypeSubjectType
from typing import cast
import datetime
from ..types import UNSET, Unset






T = TypeVar("T", bound="V2QueryCriteriaInvoiceType")


@_attrs_define
class V2QueryCriteriaInvoiceType:
    """ 
        Attributes:
            subject_type (V2QueryCriteriaInvoiceTypeSubjectType):
            type (str):
            hiding_date_from (Union[Unset, datetime.datetime]): yyyy-MM-dd'T'HH:mm:ss
            hiding_date_to (Union[Unset, datetime.datetime]): yyyy-MM-dd'T'HH:mm:ss
            is_hidden (Union[Unset, bool]):
     """

    subject_type: V2QueryCriteriaInvoiceTypeSubjectType
    type: str
    hiding_date_from: Union[Unset, datetime.datetime] = UNSET
    hiding_date_to: Union[Unset, datetime.datetime] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        subject_type = self.subject_type.value

        type = self.type
        hiding_date_from: Union[Unset, str] = UNSET
        if not isinstance(self.hiding_date_from, Unset):
            hiding_date_from = self.hiding_date_from.isoformat()

        hiding_date_to: Union[Unset, str] = UNSET
        if not isinstance(self.hiding_date_to, Unset):
            hiding_date_to = self.hiding_date_to.isoformat()

        is_hidden = self.is_hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subjectType": subject_type,
            "type": type,
        })
        if hiding_date_from is not UNSET:
            field_dict["hidingDateFrom"] = hiding_date_from
        if hiding_date_to is not UNSET:
            field_dict["hidingDateTo"] = hiding_date_to
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_type = V2QueryCriteriaInvoiceTypeSubjectType(d.pop("subjectType"))




        type = d.pop("type")

        _hiding_date_from = d.pop("hidingDateFrom", UNSET)
        hiding_date_from: Union[Unset, datetime.datetime]
        if isinstance(_hiding_date_from,  Unset):
            hiding_date_from = UNSET
        else:
            hiding_date_from = isoparse(_hiding_date_from)




        _hiding_date_to = d.pop("hidingDateTo", UNSET)
        hiding_date_to: Union[Unset, datetime.datetime]
        if isinstance(_hiding_date_to,  Unset):
            hiding_date_to = UNSET
        else:
            hiding_date_to = isoparse(_hiding_date_to)




        is_hidden = d.pop("isHidden", UNSET)

        v2_query_criteria_invoice_type = cls(
            subject_type=subject_type,
            type=type,
            hiding_date_from=hiding_date_from,
            hiding_date_to=hiding_date_to,
            is_hidden=is_hidden,
        )

        v2_query_criteria_invoice_type.additional_properties = d
        return v2_query_criteria_invoice_type

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
