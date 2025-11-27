from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eu_entity_permissions_query_permission_type import EuEntityPermissionsQueryPermissionType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="EuEntityPermissionsQueryRequest")



@_attrs_define
class EuEntityPermissionsQueryRequest:
    """ 
        Attributes:
            vat_ue_identifier (Union[None, Unset, str]): Wartość identyfikatora (numeru identyfikacyjnego VAT) podmiotu
                unijnego.
            authorized_fingerprint_identifier (Union[None, Unset, str]): Odcisk palca certyfikatu kwalifikowanego
                uprawnionego.
            permission_types (Union[None, Unset, list[EuEntityPermissionsQueryPermissionType]]): Lista rodzajów
                wyszukiwanych uprawnień.
     """

    vat_ue_identifier: Union[None, Unset, str] = UNSET
    authorized_fingerprint_identifier: Union[None, Unset, str] = UNSET
    permission_types: Union[None, Unset, list[EuEntityPermissionsQueryPermissionType]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        vat_ue_identifier: Union[None, Unset, str]
        if isinstance(self.vat_ue_identifier, Unset):
            vat_ue_identifier = UNSET
        else:
            vat_ue_identifier = self.vat_ue_identifier

        authorized_fingerprint_identifier: Union[None, Unset, str]
        if isinstance(self.authorized_fingerprint_identifier, Unset):
            authorized_fingerprint_identifier = UNSET
        else:
            authorized_fingerprint_identifier = self.authorized_fingerprint_identifier

        permission_types: Union[None, Unset, list[str]]
        if isinstance(self.permission_types, Unset):
            permission_types = UNSET
        elif isinstance(self.permission_types, list):
            permission_types = []
            for permission_types_type_0_item_data in self.permission_types:
                permission_types_type_0_item = permission_types_type_0_item_data.value
                permission_types.append(permission_types_type_0_item)


        else:
            permission_types = self.permission_types


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if vat_ue_identifier is not UNSET:
            field_dict["vatUeIdentifier"] = vat_ue_identifier
        if authorized_fingerprint_identifier is not UNSET:
            field_dict["authorizedFingerprintIdentifier"] = authorized_fingerprint_identifier
        if permission_types is not UNSET:
            field_dict["permissionTypes"] = permission_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_vat_ue_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vat_ue_identifier = _parse_vat_ue_identifier(d.pop("vatUeIdentifier", UNSET))


        def _parse_authorized_fingerprint_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        authorized_fingerprint_identifier = _parse_authorized_fingerprint_identifier(d.pop("authorizedFingerprintIdentifier", UNSET))


        def _parse_permission_types(data: object) -> Union[None, Unset, list[EuEntityPermissionsQueryPermissionType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permission_types_type_0 = []
                _permission_types_type_0 = data
                for permission_types_type_0_item_data in (_permission_types_type_0):
                    permission_types_type_0_item = EuEntityPermissionsQueryPermissionType(permission_types_type_0_item_data)



                    permission_types_type_0.append(permission_types_type_0_item)

                return permission_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[EuEntityPermissionsQueryPermissionType]], data)

        permission_types = _parse_permission_types(d.pop("permissionTypes", UNSET))


        eu_entity_permissions_query_request = cls(
            vat_ue_identifier=vat_ue_identifier,
            authorized_fingerprint_identifier=authorized_fingerprint_identifier,
            permission_types=permission_types,
        )

        return eu_entity_permissions_query_request

