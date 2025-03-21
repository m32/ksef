from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from dateutil.parser import isoparse
from typing import Dict
from typing import cast, List
from typing import cast
import datetime
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.authentication_identifier_type import AuthenticationIdentifierType
  from ..models.v2_initialised_session_type import V2InitialisedSessionType





T = TypeVar("T", bound="V2InitSessionResponse")


@_attrs_define
class V2InitSessionResponse:
    """ 
        Attributes:
            reference_number (str):
            session_token (V2InitialisedSessionType):
            timestamp (datetime.datetime):
            authentication_identifiers (Union[Unset, List['AuthenticationIdentifierType']]):
     """

    reference_number: str
    session_token: 'V2InitialisedSessionType'
    timestamp: datetime.datetime
    authentication_identifiers: Union[Unset, List['AuthenticationIdentifierType']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.authentication_identifier_type import AuthenticationIdentifierType
        from ..models.v2_initialised_session_type import V2InitialisedSessionType
        reference_number = self.reference_number
        session_token = self.session_token.to_dict()

        timestamp = self.timestamp.isoformat()

        authentication_identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authentication_identifiers, Unset):
            authentication_identifiers = []
            for authentication_identifiers_item_data in self.authentication_identifiers:
                authentication_identifiers_item = authentication_identifiers_item_data.to_dict()

                authentication_identifiers.append(authentication_identifiers_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "referenceNumber": reference_number,
            "sessionToken": session_token,
            "timestamp": timestamp,
        })
        if authentication_identifiers is not UNSET:
            field_dict["authenticationIdentifiers"] = authentication_identifiers

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authentication_identifier_type import AuthenticationIdentifierType
        from ..models.v2_initialised_session_type import V2InitialisedSessionType
        d = src_dict.copy()
        reference_number = d.pop("referenceNumber")

        session_token = V2InitialisedSessionType.from_dict(d.pop("sessionToken"))




        timestamp = isoparse(d.pop("timestamp"))




        authentication_identifiers = []
        _authentication_identifiers = d.pop("authenticationIdentifiers", UNSET)
        for authentication_identifiers_item_data in (_authentication_identifiers or []):
            authentication_identifiers_item = AuthenticationIdentifierType.from_dict(authentication_identifiers_item_data)



            authentication_identifiers.append(authentication_identifiers_item)


        v2_init_session_response = cls(
            reference_number=reference_number,
            session_token=session_token,
            timestamp=timestamp,
            authentication_identifiers=authentication_identifiers,
        )

        v2_init_session_response.additional_properties = d
        return v2_init_session_response

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
