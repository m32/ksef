from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_rate_limit_values_override import ApiRateLimitValuesOverride





T = TypeVar("T", bound="ApiRateLimitsOverride")



@_attrs_define
class ApiRateLimitsOverride:
    """ 
        Attributes:
            online_session (ApiRateLimitValuesOverride):
            batch_session (ApiRateLimitValuesOverride):
            invoice_send (ApiRateLimitValuesOverride):
            invoice_status (ApiRateLimitValuesOverride):
            session_list (ApiRateLimitValuesOverride):
            session_invoice_list (ApiRateLimitValuesOverride):
            session_misc (ApiRateLimitValuesOverride):
            invoice_metadata (ApiRateLimitValuesOverride):
            invoice_export (ApiRateLimitValuesOverride):
            invoice_download (ApiRateLimitValuesOverride):
            other (ApiRateLimitValuesOverride):
     """

    online_session: 'ApiRateLimitValuesOverride'
    batch_session: 'ApiRateLimitValuesOverride'
    invoice_send: 'ApiRateLimitValuesOverride'
    invoice_status: 'ApiRateLimitValuesOverride'
    session_list: 'ApiRateLimitValuesOverride'
    session_invoice_list: 'ApiRateLimitValuesOverride'
    session_misc: 'ApiRateLimitValuesOverride'
    invoice_metadata: 'ApiRateLimitValuesOverride'
    invoice_export: 'ApiRateLimitValuesOverride'
    invoice_download: 'ApiRateLimitValuesOverride'
    other: 'ApiRateLimitValuesOverride'





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_rate_limit_values_override import ApiRateLimitValuesOverride
        online_session = self.online_session.to_dict()

        batch_session = self.batch_session.to_dict()

        invoice_send = self.invoice_send.to_dict()

        invoice_status = self.invoice_status.to_dict()

        session_list = self.session_list.to_dict()

        session_invoice_list = self.session_invoice_list.to_dict()

        session_misc = self.session_misc.to_dict()

        invoice_metadata = self.invoice_metadata.to_dict()

        invoice_export = self.invoice_export.to_dict()

        invoice_download = self.invoice_download.to_dict()

        other = self.other.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "onlineSession": online_session,
            "batchSession": batch_session,
            "invoiceSend": invoice_send,
            "invoiceStatus": invoice_status,
            "sessionList": session_list,
            "sessionInvoiceList": session_invoice_list,
            "sessionMisc": session_misc,
            "invoiceMetadata": invoice_metadata,
            "invoiceExport": invoice_export,
            "invoiceDownload": invoice_download,
            "other": other,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_rate_limit_values_override import ApiRateLimitValuesOverride
        d = dict(src_dict)
        online_session = ApiRateLimitValuesOverride.from_dict(d.pop("onlineSession"))




        batch_session = ApiRateLimitValuesOverride.from_dict(d.pop("batchSession"))




        invoice_send = ApiRateLimitValuesOverride.from_dict(d.pop("invoiceSend"))




        invoice_status = ApiRateLimitValuesOverride.from_dict(d.pop("invoiceStatus"))




        session_list = ApiRateLimitValuesOverride.from_dict(d.pop("sessionList"))




        session_invoice_list = ApiRateLimitValuesOverride.from_dict(d.pop("sessionInvoiceList"))




        session_misc = ApiRateLimitValuesOverride.from_dict(d.pop("sessionMisc"))




        invoice_metadata = ApiRateLimitValuesOverride.from_dict(d.pop("invoiceMetadata"))




        invoice_export = ApiRateLimitValuesOverride.from_dict(d.pop("invoiceExport"))




        invoice_download = ApiRateLimitValuesOverride.from_dict(d.pop("invoiceDownload"))




        other = ApiRateLimitValuesOverride.from_dict(d.pop("other"))




        api_rate_limits_override = cls(
            online_session=online_session,
            batch_session=batch_session,
            invoice_send=invoice_send,
            invoice_status=invoice_status,
            session_list=session_list,
            session_invoice_list=session_invoice_list,
            session_misc=session_misc,
            invoice_metadata=invoice_metadata,
            invoice_export=invoice_export,
            invoice_download=invoice_download,
            other=other,
        )

        return api_rate_limits_override

