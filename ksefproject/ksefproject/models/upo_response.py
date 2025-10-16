from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.upo_page_response import UpoPageResponse





T = TypeVar("T", bound="UpoResponse")



@_attrs_define
class UpoResponse:
    """ 
        Attributes:
            pages (list['UpoPageResponse']): Lista stron UPO.
     """

    pages: list['UpoPageResponse']





    def to_dict(self) -> dict[str, Any]:
        from ..models.upo_page_response import UpoPageResponse
        pages = []
        for pages_item_data in self.pages:
            pages_item = pages_item_data.to_dict()
            pages.append(pages_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "pages": pages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upo_page_response import UpoPageResponse
        d = dict(src_dict)
        pages = []
        _pages = d.pop("pages")
        for pages_item_data in (_pages):
            pages_item = UpoPageResponse.from_dict(pages_item_data)



            pages.append(pages_item)


        upo_response = cls(
            pages=pages,
        )

        return upo_response

