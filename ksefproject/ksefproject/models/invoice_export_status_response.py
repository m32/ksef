from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.invoice_package import InvoicePackage
  from ..models.status_info import StatusInfo





T = TypeVar("T", bound="InvoiceExportStatusResponse")



@_attrs_define
class InvoiceExportStatusResponse:
    """ 
        Attributes:
            status (StatusInfo):
            completed_date (Union[None, Unset, datetime.datetime]): Data zakończenia przetwarzania żądania eksportu faktur.
            package_expiration_date (Union[None, Unset, datetime.datetime]): Data wygaśnięcia paczki faktur przygotowanej do
                pobrania.
                Po upływie tej daty paczka nie będzie już dostępna do pobrania.
            package (Union['InvoicePackage', None, Unset]): Dane paczki faktur przygotowanej do pobrania.
     """

    status: 'StatusInfo'
    completed_date: Union[None, Unset, datetime.datetime] = UNSET
    package_expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    package: Union['InvoicePackage', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_package import InvoicePackage
        from ..models.status_info import StatusInfo
        status = self.status.to_dict()

        completed_date: Union[None, Unset, str]
        if isinstance(self.completed_date, Unset):
            completed_date = UNSET
        elif isinstance(self.completed_date, datetime.datetime):
            completed_date = self.completed_date.isoformat()
        else:
            completed_date = self.completed_date

        package_expiration_date: Union[None, Unset, str]
        if isinstance(self.package_expiration_date, Unset):
            package_expiration_date = UNSET
        elif isinstance(self.package_expiration_date, datetime.datetime):
            package_expiration_date = self.package_expiration_date.isoformat()
        else:
            package_expiration_date = self.package_expiration_date

        package: Union[None, Unset, dict[str, Any]]
        if isinstance(self.package, Unset):
            package = UNSET
        elif isinstance(self.package, InvoicePackage):
            package = self.package.to_dict()
        else:
            package = self.package


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if package_expiration_date is not UNSET:
            field_dict["packageExpirationDate"] = package_expiration_date
        if package is not UNSET:
            field_dict["package"] = package

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_package import InvoicePackage
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        status = StatusInfo.from_dict(d.pop("status"))




        def _parse_completed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_date_type_0 = isoparse(data)



                return completed_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_date = _parse_completed_date(d.pop("completedDate", UNSET))


        def _parse_package_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                package_expiration_date_type_0 = isoparse(data)



                return package_expiration_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        package_expiration_date = _parse_package_expiration_date(d.pop("packageExpirationDate", UNSET))


        def _parse_package(data: object) -> Union['InvoicePackage', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                package_type_1 = InvoicePackage.from_dict(data)



                return package_type_1
            except: # noqa: E722
                pass
            return cast(Union['InvoicePackage', None, Unset], data)

        package = _parse_package(d.pop("package", UNSET))


        invoice_export_status_response = cls(
            status=status,
            completed_date=completed_date,
            package_expiration_date=package_expiration_date,
            package=package,
        )

        return invoice_export_status_response

