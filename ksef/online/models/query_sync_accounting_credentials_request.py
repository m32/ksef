from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.query_criteria_accounting_credentials_type import QueryCriteriaAccountingCredentialsType





T = TypeVar("T", bound="QuerySyncAccountingCredentialsRequest")


@_attrs_define
class QuerySyncAccountingCredentialsRequest:
    """ 
        Attributes:
            query_criteria (QueryCriteriaAccountingCredentialsType):
     """

    query_criteria: 'QueryCriteriaAccountingCredentialsType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.query_criteria_accounting_credentials_type import QueryCriteriaAccountingCredentialsType
        query_criteria = self.query_criteria.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "queryCriteria": query_criteria,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_criteria_accounting_credentials_type import QueryCriteriaAccountingCredentialsType
        d = src_dict.copy()
        query_criteria = QueryCriteriaAccountingCredentialsType.from_dict(d.pop("queryCriteria"))




        query_sync_accounting_credentials_request = cls(
            query_criteria=query_criteria,
        )

        query_sync_accounting_credentials_request.additional_properties = d
        return query_sync_accounting_credentials_request

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
