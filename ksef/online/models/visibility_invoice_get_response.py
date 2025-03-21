from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.visibility_invoice_get_response_type import VisibilityInvoiceGetResponseType





T = TypeVar("T", bound="VisibilityInvoiceGetResponse")


@_attrs_define
class VisibilityInvoiceGetResponse:
    """ 
        Attributes:
            visibility_invoice_get_response_type (VisibilityInvoiceGetResponseType):
     """

    visibility_invoice_get_response_type: 'VisibilityInvoiceGetResponseType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.visibility_invoice_get_response_type import VisibilityInvoiceGetResponseType
        visibility_invoice_get_response_type = self.visibility_invoice_get_response_type.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "visibilityInvoiceGetResponseType": visibility_invoice_get_response_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.visibility_invoice_get_response_type import VisibilityInvoiceGetResponseType
        d = src_dict.copy()
        visibility_invoice_get_response_type = VisibilityInvoiceGetResponseType.from_dict(d.pop("visibilityInvoiceGetResponseType"))




        visibility_invoice_get_response = cls(
            visibility_invoice_get_response_type=visibility_invoice_get_response_type,
        )

        visibility_invoice_get_response.additional_properties = d
        return visibility_invoice_get_response

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
