from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authentication_method import AuthenticationMethod
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.status_info import StatusInfo





T = TypeVar("T", bound="AuthenticationListItem")



@_attrs_define
class AuthenticationListItem:
    """ 
        Attributes:
            start_date (datetime.datetime): Data rozpoczęcia operacji uwierzytelnienia.
            authentication_method (AuthenticationMethod): Metoda uwierzytelnienia.
                | Wartość | Opis |
                | --- | --- |
                | Token | Token KSeF. |
                | TrustedProfile | Profil Zaufany. |
                | InternalCertificate | Certyfikat KSeF. |
                | QualifiedSignature | Podpis kwalifikowany. |
                | QualifiedSeal | Pieczęć kwalifikowana. |
                | PersonalSignature | Podpis osobisty. |
                | PeppolSignature | Podpis dostawcy uslug Peppol. |
            status (StatusInfo):
            reference_number (str): Numer referencyjny.
            is_token_redeemed (Union[None, Unset, bool]): Czy został już wydany refresh token powiązany z danym
                uwierzytelnieniem.
            last_token_refresh_date (Union[None, Unset, datetime.datetime]): Data ostatniego odświeżenia tokena.
            refresh_token_valid_until (Union[None, Unset, datetime.datetime]): Termin ważności refresh tokena (o ile nie
                zostanie wcześniej unieważniony).
            is_current (Union[Unset, bool]): Czy sesja jest powiązana z aktualnie używanym tokenem.
     """

    start_date: datetime.datetime
    authentication_method: AuthenticationMethod
    status: 'StatusInfo'
    reference_number: str
    is_token_redeemed: Union[None, Unset, bool] = UNSET
    last_token_refresh_date: Union[None, Unset, datetime.datetime] = UNSET
    refresh_token_valid_until: Union[None, Unset, datetime.datetime] = UNSET
    is_current: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_info import StatusInfo
        start_date = self.start_date.isoformat()

        authentication_method = self.authentication_method.value

        status = self.status.to_dict()

        reference_number = self.reference_number

        is_token_redeemed: Union[None, Unset, bool]
        if isinstance(self.is_token_redeemed, Unset):
            is_token_redeemed = UNSET
        else:
            is_token_redeemed = self.is_token_redeemed

        last_token_refresh_date: Union[None, Unset, str]
        if isinstance(self.last_token_refresh_date, Unset):
            last_token_refresh_date = UNSET
        elif isinstance(self.last_token_refresh_date, datetime.datetime):
            last_token_refresh_date = self.last_token_refresh_date.isoformat()
        else:
            last_token_refresh_date = self.last_token_refresh_date

        refresh_token_valid_until: Union[None, Unset, str]
        if isinstance(self.refresh_token_valid_until, Unset):
            refresh_token_valid_until = UNSET
        elif isinstance(self.refresh_token_valid_until, datetime.datetime):
            refresh_token_valid_until = self.refresh_token_valid_until.isoformat()
        else:
            refresh_token_valid_until = self.refresh_token_valid_until

        is_current = self.is_current


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "startDate": start_date,
            "authenticationMethod": authentication_method,
            "status": status,
            "referenceNumber": reference_number,
        })
        if is_token_redeemed is not UNSET:
            field_dict["isTokenRedeemed"] = is_token_redeemed
        if last_token_refresh_date is not UNSET:
            field_dict["lastTokenRefreshDate"] = last_token_refresh_date
        if refresh_token_valid_until is not UNSET:
            field_dict["refreshTokenValidUntil"] = refresh_token_valid_until
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        start_date = isoparse(d.pop("startDate"))




        authentication_method = AuthenticationMethod(d.pop("authenticationMethod"))




        status = StatusInfo.from_dict(d.pop("status"))




        reference_number = d.pop("referenceNumber")

        def _parse_is_token_redeemed(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_token_redeemed = _parse_is_token_redeemed(d.pop("isTokenRedeemed", UNSET))


        def _parse_last_token_refresh_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_token_refresh_date_type_0 = isoparse(data)



                return last_token_refresh_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_token_refresh_date = _parse_last_token_refresh_date(d.pop("lastTokenRefreshDate", UNSET))


        def _parse_refresh_token_valid_until(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refresh_token_valid_until_type_0 = isoparse(data)



                return refresh_token_valid_until_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        refresh_token_valid_until = _parse_refresh_token_valid_until(d.pop("refreshTokenValidUntil", UNSET))


        is_current = d.pop("isCurrent", UNSET)

        authentication_list_item = cls(
            start_date=start_date,
            authentication_method=authentication_method,
            status=status,
            reference_number=reference_number,
            is_token_redeemed=is_token_redeemed,
            last_token_refresh_date=last_token_refresh_date,
            refresh_token_valid_until=refresh_token_valid_until,
            is_current=is_current,
        )

        return authentication_list_item

