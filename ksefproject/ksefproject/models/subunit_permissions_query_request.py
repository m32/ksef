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
  from ..models.subunit_permissions_subunit_identifier import SubunitPermissionsSubunitIdentifier





T = TypeVar("T", bound="SubunitPermissionsQueryRequest")



@_attrs_define
class SubunitPermissionsQueryRequest:
    """ 
        Attributes:
            subunit_identifier (Union['SubunitPermissionsSubunitIdentifier', None, Unset]): Identyfikator jednostki lub
                podmiotu podrzędnego.
                | Type | Value |
                | --- | --- |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
                | Nip | 10 cyfrowy numer NIP |
     """

    subunit_identifier: Union['SubunitPermissionsSubunitIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.subunit_permissions_subunit_identifier import SubunitPermissionsSubunitIdentifier
        subunit_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subunit_identifier, Unset):
            subunit_identifier = UNSET
        elif isinstance(self.subunit_identifier, SubunitPermissionsSubunitIdentifier):
            subunit_identifier = self.subunit_identifier.to_dict()
        else:
            subunit_identifier = self.subunit_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subunit_identifier is not UNSET:
            field_dict["subunitIdentifier"] = subunit_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subunit_permissions_subunit_identifier import SubunitPermissionsSubunitIdentifier
        d = dict(src_dict)
        def _parse_subunit_identifier(data: object) -> Union['SubunitPermissionsSubunitIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subunit_identifier_type_1 = SubunitPermissionsSubunitIdentifier.from_dict(data)



                return subunit_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['SubunitPermissionsSubunitIdentifier', None, Unset], data)

        subunit_identifier = _parse_subunit_identifier(d.pop("subunitIdentifier", UNSET))


        subunit_permissions_query_request = cls(
            subunit_identifier=subunit_identifier,
        )

        return subunit_permissions_query_request

