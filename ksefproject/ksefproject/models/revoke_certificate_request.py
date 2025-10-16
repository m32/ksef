from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.certificate_revocation_reason import CertificateRevocationReason
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="RevokeCertificateRequest")



@_attrs_define
class RevokeCertificateRequest:
    """ 
        Attributes:
            revocation_reason (Union[CertificateRevocationReason, None, Unset]): Powód unieważnienia certyfikatu.
                | Wartość | Opis |
                | --- | --- |
                | Unspecified | Nieokreślony. |
                | Superseded | Certyfikat został zastąpiony przez inny. |
                | KeyCompromise | Klucz prywatny powiązany z certyfikatem został skompromitowany. |
     """

    revocation_reason: Union[CertificateRevocationReason, None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        revocation_reason: Union[None, Unset, str]
        if isinstance(self.revocation_reason, Unset):
            revocation_reason = UNSET
        elif isinstance(self.revocation_reason, CertificateRevocationReason):
            revocation_reason = self.revocation_reason.value
        else:
            revocation_reason = self.revocation_reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_revocation_reason(data: object) -> Union[CertificateRevocationReason, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revocation_reason_type_1 = CertificateRevocationReason(data)



                return revocation_reason_type_1
            except: # noqa: E722
                pass
            return cast(Union[CertificateRevocationReason, None, Unset], data)

        revocation_reason = _parse_revocation_reason(d.pop("revocationReason", UNSET))


        revoke_certificate_request = cls(
            revocation_reason=revocation_reason,
        )

        return revoke_certificate_request

