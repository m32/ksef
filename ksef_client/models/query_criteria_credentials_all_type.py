from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_criteria_credentials_all_type_query_credentials_scope_result_type import (
    QueryCriteriaCredentialsAllTypeQueryCredentialsScopeResultType,
)
from ..models.query_criteria_credentials_all_type_query_credentials_type_result_type import (
    QueryCriteriaCredentialsAllTypeQueryCredentialsTypeResultType,
)

T = TypeVar("T", bound="QueryCriteriaCredentialsAllType")


@attr.s(auto_attribs=True)
class QueryCriteriaCredentialsAllType:
    """
    Attributes:
        type (str):
        query_credentials_type_result_type (QueryCriteriaCredentialsAllTypeQueryCredentialsTypeResultType):
        query_credentials_scope_result_type (QueryCriteriaCredentialsAllTypeQueryCredentialsScopeResultType):
    """

    type: str
    query_credentials_type_result_type: QueryCriteriaCredentialsAllTypeQueryCredentialsTypeResultType
    query_credentials_scope_result_type: QueryCriteriaCredentialsAllTypeQueryCredentialsScopeResultType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        query_credentials_type_result_type = self.query_credentials_type_result_type.value

        query_credentials_scope_result_type = self.query_credentials_scope_result_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "queryCredentialsTypeResultType": query_credentials_type_result_type,
                "queryCredentialsScopeResultType": query_credentials_scope_result_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        query_credentials_type_result_type = QueryCriteriaCredentialsAllTypeQueryCredentialsTypeResultType(
            d.pop("queryCredentialsTypeResultType")
        )

        query_credentials_scope_result_type = QueryCriteriaCredentialsAllTypeQueryCredentialsScopeResultType(
            d.pop("queryCredentialsScopeResultType")
        )

        query_criteria_credentials_all_type = cls(
            type=type,
            query_credentials_type_result_type=query_credentials_type_result_type,
            query_credentials_scope_result_type=query_credentials_scope_result_type,
        )

        query_criteria_credentials_all_type.additional_properties = d
        return query_criteria_credentials_all_type

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
