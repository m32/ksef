from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from ..models.invoice_verification_response_invoice_type import InvoiceVerificationResponseInvoiceType
from typing import Union
from dateutil.parser import isoparse
import datetime
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.subject_identifier_by_type import SubjectIdentifierByType





T = TypeVar("T", bound="InvoiceVerificationResponse")


@_attrs_define
class InvoiceVerificationResponse:
    """ 
        Attributes:
            acquisition_timestamp (Union[Unset, datetime.datetime]):
            hash_ (Union[Unset, str]):
            invoice_type (Union[Unset, InvoiceVerificationResponseInvoiceType]):
            ksef_reference_number (Union[Unset, str]):
            schema_version (Union[Unset, str]):
            subject_by (Union[Unset, SubjectIdentifierByType]):
     """

    acquisition_timestamp: Union[Unset, datetime.datetime] = UNSET
    hash_: Union[Unset, str] = UNSET
    invoice_type: Union[Unset, InvoiceVerificationResponseInvoiceType] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    schema_version: Union[Unset, str] = UNSET
    subject_by: Union[Unset, 'SubjectIdentifierByType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        acquisition_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.acquisition_timestamp, Unset):
            acquisition_timestamp = self.acquisition_timestamp.isoformat()

        hash_ = self.hash_
        invoice_type: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_type, Unset):
            invoice_type = self.invoice_type.value

        ksef_reference_number = self.ksef_reference_number
        schema_version = self.schema_version
        subject_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_by, Unset):
            subject_by = self.subject_by.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if acquisition_timestamp is not UNSET:
            field_dict["acquisitionTimestamp"] = acquisition_timestamp
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if invoice_type is not UNSET:
            field_dict["invoiceType"] = invoice_type
        if ksef_reference_number is not UNSET:
            field_dict["ksefReferenceNumber"] = ksef_reference_number
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version
        if subject_by is not UNSET:
            field_dict["subjectBy"] = subject_by

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        d = src_dict.copy()
        _acquisition_timestamp = d.pop("acquisitionTimestamp", UNSET)
        acquisition_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_acquisition_timestamp,  Unset):
            acquisition_timestamp = UNSET
        else:
            acquisition_timestamp = isoparse(_acquisition_timestamp)




        hash_ = d.pop("hash", UNSET)

        _invoice_type = d.pop("invoiceType", UNSET)
        invoice_type: Union[Unset, InvoiceVerificationResponseInvoiceType]
        if isinstance(_invoice_type,  Unset):
            invoice_type = UNSET
        else:
            invoice_type = InvoiceVerificationResponseInvoiceType(_invoice_type)




        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        schema_version = d.pop("schemaVersion", UNSET)

        _subject_by = d.pop("subjectBy", UNSET)
        subject_by: Union[Unset, SubjectIdentifierByType]
        if isinstance(_subject_by,  Unset):
            subject_by = UNSET
        else:
            subject_by = SubjectIdentifierByType.from_dict(_subject_by)




        invoice_verification_response = cls(
            acquisition_timestamp=acquisition_timestamp,
            hash_=hash_,
            invoice_type=invoice_type,
            ksef_reference_number=ksef_reference_number,
            schema_version=schema_version,
            subject_by=subject_by,
        )

        invoice_verification_response.additional_properties = d
        return invoice_verification_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
