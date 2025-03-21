from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.anonymous_subject_to_type import AnonymousSubjectToType





T = TypeVar("T", bound="InvoiceQueryDetailsType")


@_attrs_define
class InvoiceQueryDetailsType:
    """ 
        Attributes:
            due_value (str):
            invoice_oryginal_number (str):
            subject_to (AnonymousSubjectToType):
     """

    due_value: str
    invoice_oryginal_number: str
    subject_to: 'AnonymousSubjectToType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.anonymous_subject_to_type import AnonymousSubjectToType
        due_value = self.due_value
        invoice_oryginal_number = self.invoice_oryginal_number
        subject_to = self.subject_to.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dueValue": due_value,
            "invoiceOryginalNumber": invoice_oryginal_number,
            "subjectTo": subject_to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.anonymous_subject_to_type import AnonymousSubjectToType
        d = src_dict.copy()
        due_value = d.pop("dueValue")

        invoice_oryginal_number = d.pop("invoiceOryginalNumber")

        subject_to = AnonymousSubjectToType.from_dict(d.pop("subjectTo"))




        invoice_query_details_type = cls(
            due_value=due_value,
            invoice_oryginal_number=invoice_oryginal_number,
            subject_to=subject_to,
        )

        invoice_query_details_type.additional_properties = d
        return invoice_query_details_type

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
