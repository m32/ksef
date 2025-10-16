from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.peppol_provider import PeppolProvider





T = TypeVar("T", bound="QueryPeppolProvidersResponse")



@_attrs_define
class QueryPeppolProvidersResponse:
    """ 
        Attributes:
            peppol_providers (list['PeppolProvider']): Lista dostawców usług Peppol.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    peppol_providers: list['PeppolProvider']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.peppol_provider import PeppolProvider
        peppol_providers = []
        for peppol_providers_item_data in self.peppol_providers:
            peppol_providers_item = peppol_providers_item_data.to_dict()
            peppol_providers.append(peppol_providers_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "peppolProviders": peppol_providers,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.peppol_provider import PeppolProvider
        d = dict(src_dict)
        peppol_providers = []
        _peppol_providers = d.pop("peppolProviders")
        for peppol_providers_item_data in (_peppol_providers):
            peppol_providers_item = PeppolProvider.from_dict(peppol_providers_item_data)



            peppol_providers.append(peppol_providers_item)


        has_more = d.pop("hasMore")

        query_peppol_providers_response = cls(
            peppol_providers=peppol_providers,
            has_more=has_more,
        )

        return query_peppol_providers_response

