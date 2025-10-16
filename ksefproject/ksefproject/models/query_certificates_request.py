from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.certificate_list_item_status import CertificateListItemStatus
from ..models.ksef_certificate_type import KsefCertificateType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="QueryCertificatesRequest")



@_attrs_define
class QueryCertificatesRequest:
    """ 
        Attributes:
            certificate_serial_number (Union[None, Unset, str]): Numer seryjny certyfikatu. Wyszukiwanie odbywa się na
                zasadzie dokładnego dopasowania (exact match).
            name (Union[None, Unset, str]): Nazwa własna certyfikatu. Wyszukiwanie jest częściowe, czyli zwracane są
                certyfikaty, których nazwa zawiera podany ciąg znaków (contains).
            type_ (Union[KsefCertificateType, None, Unset]): Typ certyfikatu KSeF.
                | Wartość | Opis |
                | --- | --- |
                | Authentication | Certyfikat używany do uwierzytelnienia w systemie. |
                | Offline | Certyfikat używany wyłącznie do potwierdzania autentyczności wystawcy i integralności faktury w
                trybie offline |
            status (Union[CertificateListItemStatus, None, Unset]): Status certyfikatu.
                | Wartość | Opis |
                | --- | --- |
                | Active | Certyfikat jest aktywny i może zostać użyty do uwierzytelnienia lub realizacji operacji w trybie
                offline (w zależności od typu certyfikatu). |
                | Blocked | Certyfikat został zablokowany i nie może zostać użyty do uwierzytelnienia i realizacji operacji w
                trybie offline.            Status przejściowy do czasu zakończenia procesu unieważniania. |
                | Revoked | Certyfikat został unieważniony i nie może zostać użyty do uwierzytelnienia i realizacji operacji w
                trybie offline. |
                | Expired | Certyfikat wygasł i nie może zostać użyty do uwierzytelnienia i realizacji operacji w trybie
                offline. |
            expires_after (Union[None, Unset, datetime.datetime]): Filtruje certyfikaty, które wygasają po podanej dacie.
     """

    certificate_serial_number: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[KsefCertificateType, None, Unset] = UNSET
    status: Union[CertificateListItemStatus, None, Unset] = UNSET
    expires_after: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        certificate_serial_number: Union[None, Unset, str]
        if isinstance(self.certificate_serial_number, Unset):
            certificate_serial_number = UNSET
        else:
            certificate_serial_number = self.certificate_serial_number

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, KsefCertificateType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, CertificateListItemStatus):
            status = self.status.value
        else:
            status = self.status

        expires_after: Union[None, Unset, str]
        if isinstance(self.expires_after, Unset):
            expires_after = UNSET
        elif isinstance(self.expires_after, datetime.datetime):
            expires_after = self.expires_after.isoformat()
        else:
            expires_after = self.expires_after


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if certificate_serial_number is not UNSET:
            field_dict["certificateSerialNumber"] = certificate_serial_number
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if expires_after is not UNSET:
            field_dict["expiresAfter"] = expires_after

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_certificate_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        certificate_serial_number = _parse_certificate_serial_number(d.pop("certificateSerialNumber", UNSET))


        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_type_(data: object) -> Union[KsefCertificateType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = KsefCertificateType(data)



                return type_type_1
            except: # noqa: E722
                pass
            return cast(Union[KsefCertificateType, None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_status(data: object) -> Union[CertificateListItemStatus, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = CertificateListItemStatus(data)



                return status_type_1
            except: # noqa: E722
                pass
            return cast(Union[CertificateListItemStatus, None, Unset], data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_expires_after(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_after_type_0 = isoparse(data)



                return expires_after_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_after = _parse_expires_after(d.pop("expiresAfter", UNSET))


        query_certificates_request = cls(
            certificate_serial_number=certificate_serial_number,
            name=name,
            type_=type_,
            status=status,
            expires_after=expires_after,
        )

        return query_certificates_request

