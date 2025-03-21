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
  from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
  from ..models.credentials_identifier_request_accounting_type import CredentialsIdentifierRequestAccountingType





T = TypeVar("T", bound="QueryCriteriaAccountingCredentialsType")


@_attrs_define
class QueryCriteriaAccountingCredentialsType:
    """ 
        Attributes:
            assignee_identifier (Union[Unset, CredentialsIdentifierRequestType]):
            partner_identifier (Union[Unset, CredentialsIdentifierRequestAccountingType]):
     """

    assignee_identifier: Union[Unset, 'CredentialsIdentifierRequestType'] = UNSET
    partner_identifier: Union[Unset, 'CredentialsIdentifierRequestAccountingType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
        from ..models.credentials_identifier_request_accounting_type import CredentialsIdentifierRequestAccountingType
        assignee_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee_identifier, Unset):
            assignee_identifier = self.assignee_identifier.to_dict()

        partner_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partner_identifier, Unset):
            partner_identifier = self.partner_identifier.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if assignee_identifier is not UNSET:
            field_dict["assigneeIdentifier"] = assignee_identifier
        if partner_identifier is not UNSET:
            field_dict["partnerIdentifier"] = partner_identifier

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
        from ..models.credentials_identifier_request_accounting_type import CredentialsIdentifierRequestAccountingType
        d = src_dict.copy()
        _assignee_identifier = d.pop("assigneeIdentifier", UNSET)
        assignee_identifier: Union[Unset, CredentialsIdentifierRequestType]
        if isinstance(_assignee_identifier,  Unset):
            assignee_identifier = UNSET
        else:
            assignee_identifier = CredentialsIdentifierRequestType.from_dict(_assignee_identifier)




        _partner_identifier = d.pop("partnerIdentifier", UNSET)
        partner_identifier: Union[Unset, CredentialsIdentifierRequestAccountingType]
        if isinstance(_partner_identifier,  Unset):
            partner_identifier = UNSET
        else:
            partner_identifier = CredentialsIdentifierRequestAccountingType.from_dict(_partner_identifier)




        query_criteria_accounting_credentials_type = cls(
            assignee_identifier=assignee_identifier,
            partner_identifier=partner_identifier,
        )

        query_criteria_accounting_credentials_type.additional_properties = d
        return query_criteria_accounting_credentials_type

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
