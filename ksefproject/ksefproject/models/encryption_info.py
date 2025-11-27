from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="EncryptionInfo")



@_attrs_define
class EncryptionInfo:
    """ 
        Attributes:
            encrypted_symmetric_key (str): Klucz symetryczny o długości 32 bajtów, zaszyfrowany algorytmem RSA (Padding:
                OAEP z SHA-256), zakodowany w formacie Base64.

                [Klucz publiczny Ministersta Finansów](/docs/v2/index.html#tag/Certyfikaty-klucza-publicznego)
            initialization_vector (str): Wektor inicjalizujący (IV) o długości 16 bajtów, używany do szyfrowania
                symetrycznego, zakodowany w formacie Base64.
     """

    encrypted_symmetric_key: str
    initialization_vector: str





    def to_dict(self) -> dict[str, Any]:
        encrypted_symmetric_key = self.encrypted_symmetric_key

        initialization_vector = self.initialization_vector


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "encryptedSymmetricKey": encrypted_symmetric_key,
            "initializationVector": initialization_vector,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encrypted_symmetric_key = d.pop("encryptedSymmetricKey")

        initialization_vector = d.pop("initializationVector")

        encryption_info = cls(
            encrypted_symmetric_key=encrypted_symmetric_key,
            initialization_vector=initialization_vector,
        )

        return encryption_info

