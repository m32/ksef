from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.authentication_context_identifier import AuthenticationContextIdentifier
  from ..models.authorization_policy import AuthorizationPolicy





T = TypeVar("T", bound="InitTokenAuthenticationRequest")



@_attrs_define
class InitTokenAuthenticationRequest:
    """ 
        Attributes:
            challenge (str): Unikalny challenge.
            context_identifier (AuthenticationContextIdentifier):
            encrypted_token (str): Zaszyfrowany token wraz z timestampem z challenge'a, w formacie `token|timestamp`.
            authorization_policy (Union['AuthorizationPolicy', None, Unset]): Polityka autoryzacji żądań przy każdym użyciu
                tokena dostępu.
     """

    challenge: str
    context_identifier: 'AuthenticationContextIdentifier'
    encrypted_token: str
    authorization_policy: Union['AuthorizationPolicy', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.authentication_context_identifier import AuthenticationContextIdentifier
        from ..models.authorization_policy import AuthorizationPolicy
        challenge = self.challenge

        context_identifier = self.context_identifier.to_dict()

        encrypted_token = self.encrypted_token

        authorization_policy: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorization_policy, Unset):
            authorization_policy = UNSET
        elif isinstance(self.authorization_policy, AuthorizationPolicy):
            authorization_policy = self.authorization_policy.to_dict()
        else:
            authorization_policy = self.authorization_policy


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "challenge": challenge,
            "contextIdentifier": context_identifier,
            "encryptedToken": encrypted_token,
        })
        if authorization_policy is not UNSET:
            field_dict["authorizationPolicy"] = authorization_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication_context_identifier import AuthenticationContextIdentifier
        from ..models.authorization_policy import AuthorizationPolicy
        d = dict(src_dict)
        challenge = d.pop("challenge")

        context_identifier = AuthenticationContextIdentifier.from_dict(d.pop("contextIdentifier"))




        encrypted_token = d.pop("encryptedToken")

        def _parse_authorization_policy(data: object) -> Union['AuthorizationPolicy', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorization_policy_type_1 = AuthorizationPolicy.from_dict(data)



                return authorization_policy_type_1
            except: # noqa: E722
                pass
            return cast(Union['AuthorizationPolicy', None, Unset], data)

        authorization_policy = _parse_authorization_policy(d.pop("authorizationPolicy", UNSET))


        init_token_authentication_request = cls(
            challenge=challenge,
            context_identifier=context_identifier,
            encrypted_token=encrypted_token,
            authorization_policy=authorization_policy,
        )

        return init_token_authentication_request

