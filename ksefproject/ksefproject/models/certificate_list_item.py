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

if TYPE_CHECKING:
  from ..models.certificate_subject_identifier import CertificateSubjectIdentifier





T = TypeVar("T", bound="CertificateListItem")



@_attrs_define
class CertificateListItem:
    """ 
        Attributes:
            certificate_serial_number (str): Numer seryjny certyfikatu (w formacie szesnastkowym).
            name (str): Nazwa własna certyfikatu.
            type_ (KsefCertificateType): | Wartość | Opis |
                | --- | --- |
                | Authentication | Certyfikat używany do uwierzytelnienia w systemie. |
                | Offline | Certyfikat używany wyłącznie do potwierdzania autentyczności wystawcy i integralności faktury w
                trybie offline |
            common_name (str): Nazwa powszechna (CN) podmiotu, dla którego wystawiono certyfikat.
            status (CertificateListItemStatus): | Wartość | Opis |
                | --- | --- |
                | Active | Certyfikat jest aktywny i może zostać użyty do uwierzytelnienia lub realizacji operacji w trybie
                offline (w zależności od typu certyfikatu). |
                | Blocked | Certyfikat został zablokowany i nie może zostać użyty do uwierzytelnienia i realizacji operacji w
                trybie offline.            Status przejściowy do czasu zakończenia procesu unieważniania. |
                | Revoked | Certyfikat został unieważniony i nie może zostać użyty do uwierzytelnienia i realizacji operacji w
                trybie offline. |
                | Expired | Certyfikat wygasł i nie może zostać użyty do uwierzytelnienia i realizacji operacji w trybie
                offline. |
            subject_identifier (CertificateSubjectIdentifier): Identyfikator podmiotu dla którego wystawiono certyfikat.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            valid_from (datetime.datetime): Data rozpoczęcia ważności certyfikatu.
            valid_to (datetime.datetime): Data wygaśnięcia certyfikatu.
            request_date (datetime.datetime): Data złożenia wniosku certyfikacyjnego.
            last_use_date (Union[None, Unset, datetime.datetime]): Data ostatniego użycia certyfikatu.
     """

    certificate_serial_number: str
    name: str
    type_: KsefCertificateType
    common_name: str
    status: CertificateListItemStatus
    subject_identifier: 'CertificateSubjectIdentifier'
    valid_from: datetime.datetime
    valid_to: datetime.datetime
    request_date: datetime.datetime
    last_use_date: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_subject_identifier import CertificateSubjectIdentifier
        certificate_serial_number = self.certificate_serial_number

        name = self.name

        type_ = self.type_.value

        common_name = self.common_name

        status = self.status.value

        subject_identifier = self.subject_identifier.to_dict()

        valid_from = self.valid_from.isoformat()

        valid_to = self.valid_to.isoformat()

        request_date = self.request_date.isoformat()

        last_use_date: Union[None, Unset, str]
        if isinstance(self.last_use_date, Unset):
            last_use_date = UNSET
        elif isinstance(self.last_use_date, datetime.datetime):
            last_use_date = self.last_use_date.isoformat()
        else:
            last_use_date = self.last_use_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificateSerialNumber": certificate_serial_number,
            "name": name,
            "type": type_,
            "commonName": common_name,
            "status": status,
            "subjectIdentifier": subject_identifier,
            "validFrom": valid_from,
            "validTo": valid_to,
            "requestDate": request_date,
        })
        if last_use_date is not UNSET:
            field_dict["lastUseDate"] = last_use_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_subject_identifier import CertificateSubjectIdentifier
        d = dict(src_dict)
        certificate_serial_number = d.pop("certificateSerialNumber")

        name = d.pop("name")

        type_ = KsefCertificateType(d.pop("type"))




        common_name = d.pop("commonName")

        status = CertificateListItemStatus(d.pop("status"))




        subject_identifier = CertificateSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        valid_from = isoparse(d.pop("validFrom"))




        valid_to = isoparse(d.pop("validTo"))




        request_date = isoparse(d.pop("requestDate"))




        def _parse_last_use_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_use_date_type_0 = isoparse(data)



                return last_use_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_use_date = _parse_last_use_date(d.pop("lastUseDate", UNSET))


        certificate_list_item = cls(
            certificate_serial_number=certificate_serial_number,
            name=name,
            type_=type_,
            common_name=common_name,
            status=status,
            subject_identifier=subject_identifier,
            valid_from=valid_from,
            valid_to=valid_to,
            request_date=request_date,
            last_use_date=last_use_date,
        )

        return certificate_list_item

