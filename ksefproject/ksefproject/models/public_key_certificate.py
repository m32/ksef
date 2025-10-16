from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.public_key_certificate_usage import PublicKeyCertificateUsage
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PublicKeyCertificate")



@_attrs_define
class PublicKeyCertificate:
    """ 
        Attributes:
            certificate (str): Certyfikat klucza publicznego w formacie DER zakodowany w Base64.
            valid_from (datetime.datetime): Data początku obowiązywania certyfikatu.
            valid_to (datetime.datetime): Data końca obowiązywania certyfikatu.
            usage (list[PublicKeyCertificateUsage]): Operacje do których może być używany certyfikat.
                | Wartość | Opis |
                | --- | --- |
                | KsefTokenEncryption | Szyfrowanie tokenów KSeF przesyłanych w trakcie procesu uwierzytelniania. |
                | SymmetricKeyEncryption | Szyfrowanie klucza symetrycznego wykorzystywanego do szyfrowania przesyłanych faktur.
                |
     """

    certificate: str
    valid_from: datetime.datetime
    valid_to: datetime.datetime
    usage: list[PublicKeyCertificateUsage]





    def to_dict(self) -> dict[str, Any]:
        certificate = self.certificate

        valid_from = self.valid_from.isoformat()

        valid_to = self.valid_to.isoformat()

        usage = []
        for usage_item_data in self.usage:
            usage_item = usage_item_data.value
            usage.append(usage_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificate": certificate,
            "validFrom": valid_from,
            "validTo": valid_to,
            "usage": usage,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate = d.pop("certificate")

        valid_from = isoparse(d.pop("validFrom"))




        valid_to = isoparse(d.pop("validTo"))




        usage = []
        _usage = d.pop("usage")
        for usage_item_data in (_usage):
            usage_item = PublicKeyCertificateUsage(usage_item_data)



            usage.append(usage_item)


        public_key_certificate = cls(
            certificate=certificate,
            valid_from=valid_from,
            valid_to=valid_to,
            usage=usage,
        )

        return public_key_certificate

