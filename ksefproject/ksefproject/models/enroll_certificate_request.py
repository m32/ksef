from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ksef_certificate_type import KsefCertificateType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="EnrollCertificateRequest")



@_attrs_define
class EnrollCertificateRequest:
    """ 
        Attributes:
            certificate_name (str): Nazwa własna certyfikatu.
            certificate_type (KsefCertificateType): | Wartość | Opis |
                | --- | --- |
                | Authentication | Certyfikat używany do uwierzytelnienia w systemie. |
                | Offline | Certyfikat używany wyłącznie do potwierdzania autentyczności wystawcy i integralności faktury w
                trybie offline |
            csr (str): Wniosek certyfikacyjny PKCS#10 (CSR) w formacie DER zakodowany w Base64.
            valid_from (Union[None, Unset, datetime.datetime]): Data rozpoczęcia ważności certyfikatu.
                Jeśli nie zostanie podana, certyfikat będzie ważny od momentu jego wystawienia.
     """

    certificate_name: str
    certificate_type: KsefCertificateType
    csr: str
    valid_from: Union[None, Unset, datetime.datetime] = UNSET





    def to_dict(self) -> dict[str, Any]:
        certificate_name = self.certificate_name

        certificate_type = self.certificate_type.value

        csr = self.csr

        valid_from: Union[None, Unset, str]
        if isinstance(self.valid_from, Unset):
            valid_from = UNSET
        elif isinstance(self.valid_from, datetime.datetime):
            valid_from = self.valid_from.isoformat()
        else:
            valid_from = self.valid_from


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificateName": certificate_name,
            "certificateType": certificate_type,
            "csr": csr,
        })
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_name = d.pop("certificateName")

        certificate_type = KsefCertificateType(d.pop("certificateType"))




        csr = d.pop("csr")

        def _parse_valid_from(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_type_0 = isoparse(data)



                return valid_from_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        valid_from = _parse_valid_from(d.pop("validFrom", UNSET))


        enroll_certificate_request = cls(
            certificate_name=certificate_name,
            certificate_type=certificate_type,
            csr=csr,
            valid_from=valid_from,
        )

        return enroll_certificate_request

