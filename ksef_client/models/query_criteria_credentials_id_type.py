from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
from ..models.query_criteria_credentials_id_type_query_credentials_scope_result_type import (
    QueryCriteriaCredentialsIdTypeQueryCredentialsScopeResultType,
)
from ..models.query_criteria_credentials_id_type_query_credentials_type_result_type import (
    QueryCriteriaCredentialsIdTypeQueryCredentialsTypeResultType,
)

T = TypeVar("T", bound="QueryCriteriaCredentialsIdType")


@attr.s(auto_attribs=True)
class QueryCriteriaCredentialsIdType:
    """
    Attributes:
        type (str):
        query_credentials_type_result_type (QueryCriteriaCredentialsIdTypeQueryCredentialsTypeResultType):
        query_credentials_scope_result_type (QueryCriteriaCredentialsIdTypeQueryCredentialsScopeResultType):
        credentials_identifier (CredentialsIdentifierRequestType):
    """

    type: str
    query_credentials_type_result_type: QueryCriteriaCredentialsIdTypeQueryCredentialsTypeResultType
    query_credentials_scope_result_type: QueryCriteriaCredentialsIdTypeQueryCredentialsScopeResultType
    credentials_identifier: CredentialsIdentifierRequestType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        query_credentials_type_result_type = self.query_credentials_type_result_type.value

        query_credentials_scope_result_type = self.query_credentials_scope_result_type.value

        credentials_identifier = self.credentials_identifier.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "queryCredentialsTypeResultType": query_credentials_type_result_type,
                "queryCredentialsScopeResultType": query_credentials_scope_result_type,
                "credentialsIdentifier": credentials_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        query_credentials_type_result_type = QueryCriteriaCredentialsIdTypeQueryCredentialsTypeResultType(
            d.pop("queryCredentialsTypeResultType")
        )

        query_credentials_scope_result_type = QueryCriteriaCredentialsIdTypeQueryCredentialsScopeResultType(
            d.pop("queryCredentialsScopeResultType")
        )

        credentials_identifier = CredentialsIdentifierRequestType.from_dict(d.pop("credentialsIdentifier"))

        query_criteria_credentials_id_type = cls(
            type=type,
            query_credentials_type_result_type=query_credentials_type_result_type,
            query_credentials_scope_result_type=query_credentials_scope_result_type,
            credentials_identifier=credentials_identifier,
        )

        query_criteria_credentials_id_type.additional_properties = d
        return query_criteria_credentials_id_type

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
