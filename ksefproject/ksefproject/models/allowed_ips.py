from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="AllowedIps")



@_attrs_define
class AllowedIps:
    """ 
        Attributes:
            ip_4_addresses (Union[None, Unset, list[str]]): Lista adresów IPv4 w notacji dziesiętnej kropkowanej, np.
                `192.168.0.10`.
            ip_4_ranges (Union[None, Unset, list[str]]): Lista adresów IPv4 podana w formie zakresu początek–koniec,
                oddzielonego pojedynczym myślnikiem, np. `10.0.0.1–10.0.0.254`.
            ip_4_masks (Union[None, Unset, list[str]]): Lista adresów IPv4 w notacji CIDR, np. `172.16.0.0/16`.
     """

    ip_4_addresses: Union[None, Unset, list[str]] = UNSET
    ip_4_ranges: Union[None, Unset, list[str]] = UNSET
    ip_4_masks: Union[None, Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ip_4_addresses: Union[None, Unset, list[str]]
        if isinstance(self.ip_4_addresses, Unset):
            ip_4_addresses = UNSET
        elif isinstance(self.ip_4_addresses, list):
            ip_4_addresses = self.ip_4_addresses


        else:
            ip_4_addresses = self.ip_4_addresses

        ip_4_ranges: Union[None, Unset, list[str]]
        if isinstance(self.ip_4_ranges, Unset):
            ip_4_ranges = UNSET
        elif isinstance(self.ip_4_ranges, list):
            ip_4_ranges = self.ip_4_ranges


        else:
            ip_4_ranges = self.ip_4_ranges

        ip_4_masks: Union[None, Unset, list[str]]
        if isinstance(self.ip_4_masks, Unset):
            ip_4_masks = UNSET
        elif isinstance(self.ip_4_masks, list):
            ip_4_masks = self.ip_4_masks


        else:
            ip_4_masks = self.ip_4_masks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ip_4_addresses is not UNSET:
            field_dict["ip4Addresses"] = ip_4_addresses
        if ip_4_ranges is not UNSET:
            field_dict["ip4Ranges"] = ip_4_ranges
        if ip_4_masks is not UNSET:
            field_dict["ip4Masks"] = ip_4_masks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ip_4_addresses(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_4_addresses_type_0 = cast(list[str], data)

                return ip_4_addresses_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_4_addresses = _parse_ip_4_addresses(d.pop("ip4Addresses", UNSET))


        def _parse_ip_4_ranges(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_4_ranges_type_0 = cast(list[str], data)

                return ip_4_ranges_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_4_ranges = _parse_ip_4_ranges(d.pop("ip4Ranges", UNSET))


        def _parse_ip_4_masks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_4_masks_type_0 = cast(list[str], data)

                return ip_4_masks_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_4_masks = _parse_ip_4_masks(d.pop("ip4Masks", UNSET))


        allowed_ips = cls(
            ip_4_addresses=ip_4_addresses,
            ip_4_ranges=ip_4_ranges,
            ip_4_masks=ip_4_masks,
        )

        return allowed_ips

