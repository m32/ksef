from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.query_payment_criteria_type import QueryPaymentCriteriaType





T = TypeVar("T", bound="QueryPaymentRequest")


@_attrs_define
class QueryPaymentRequest:
    """ 
        Attributes:
            query_criteria (Union[Unset, QueryPaymentCriteriaType]):
     """

    query_criteria: Union[Unset, 'QueryPaymentCriteriaType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.query_payment_criteria_type import QueryPaymentCriteriaType
        query_criteria: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_criteria, Unset):
            query_criteria = self.query_criteria.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if query_criteria is not UNSET:
            field_dict["queryCriteria"] = query_criteria

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_payment_criteria_type import QueryPaymentCriteriaType
        d = src_dict.copy()
        _query_criteria = d.pop("queryCriteria", UNSET)
        query_criteria: Union[Unset, QueryPaymentCriteriaType]
        if isinstance(_query_criteria,  Unset):
            query_criteria = UNSET
        else:
            query_criteria = QueryPaymentCriteriaType.from_dict(_query_criteria)




        query_payment_request = cls(
            query_criteria=query_criteria,
        )

        query_payment_request.additional_properties = d
        return query_payment_request

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
