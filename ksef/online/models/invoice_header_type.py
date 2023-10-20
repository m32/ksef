from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_header_type_invoice_type import InvoiceHeaderTypeInvoiceType
from typing import Union
from typing import cast, List
import datetime
from typing import Dict
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast

if TYPE_CHECKING:
  from ..models.subject_other_type import SubjectOtherType
  from ..models.subject_authorized_type import SubjectAuthorizedType
  from ..models.file_unlimited_hash_type import FileUnlimitedHashType
  from ..models.subject_to_type import SubjectToType
  from ..models.subject_by_type import SubjectByType





T = TypeVar("T", bound="InvoiceHeaderType")


@_attrs_define
class InvoiceHeaderType:
    """ 
        Attributes:
            acquisition_timestamp (datetime.datetime):
            currency (str):
            fa_p17_annotation (bool):
            gross (str):
            invoice_hash (FileUnlimitedHashType):
            invoice_reference_number (str):
            invoice_type (InvoiceHeaderTypeInvoiceType):
            invoicing_date (datetime.date):
            ksef_reference_number (str):
            net (str):
            subject_by (SubjectByType):
            subject_to (SubjectToType):
            vat (str):
            schema_version (Union[Unset, str]):
            subject_by_k (Union[Unset, SubjectByType]):
            subject_to_k_list (Union[Unset, List['SubjectToType']]):
            subjects_authorized_list (Union[Unset, List['SubjectAuthorizedType']]):
            subjects_other_list (Union[Unset, List['SubjectOtherType']]):
     """

    acquisition_timestamp: datetime.datetime
    currency: str
    fa_p17_annotation: bool
    gross: str
    invoice_hash: 'FileUnlimitedHashType'
    invoice_reference_number: str
    invoice_type: InvoiceHeaderTypeInvoiceType
    invoicing_date: datetime.date
    ksef_reference_number: str
    net: str
    subject_by: 'SubjectByType'
    subject_to: 'SubjectToType'
    vat: str
    schema_version: Union[Unset, str] = UNSET
    subject_by_k: Union[Unset, 'SubjectByType'] = UNSET
    subject_to_k_list: Union[Unset, List['SubjectToType']] = UNSET
    subjects_authorized_list: Union[Unset, List['SubjectAuthorizedType']] = UNSET
    subjects_other_list: Union[Unset, List['SubjectOtherType']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_other_type import SubjectOtherType
        from ..models.subject_authorized_type import SubjectAuthorizedType
        from ..models.file_unlimited_hash_type import FileUnlimitedHashType
        from ..models.subject_to_type import SubjectToType
        from ..models.subject_by_type import SubjectByType
        acquisition_timestamp = self.acquisition_timestamp.isoformat()

        currency = self.currency
        fa_p17_annotation = self.fa_p17_annotation
        gross = self.gross
        invoice_hash = self.invoice_hash.to_dict()

        invoice_reference_number = self.invoice_reference_number
        invoice_type = self.invoice_type.value

        invoicing_date = self.invoicing_date.isoformat() 
        ksef_reference_number = self.ksef_reference_number
        net = self.net
        subject_by = self.subject_by.to_dict()

        subject_to = self.subject_to.to_dict()

        vat = self.vat
        schema_version = self.schema_version
        subject_by_k: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_by_k, Unset):
            subject_by_k = self.subject_by_k.to_dict()

        subject_to_k_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subject_to_k_list, Unset):
            subject_to_k_list = []
            for subject_to_k_list_item_data in self.subject_to_k_list:
                subject_to_k_list_item = subject_to_k_list_item_data.to_dict()

                subject_to_k_list.append(subject_to_k_list_item)




        subjects_authorized_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subjects_authorized_list, Unset):
            subjects_authorized_list = []
            for subjects_authorized_list_item_data in self.subjects_authorized_list:
                subjects_authorized_list_item = subjects_authorized_list_item_data.to_dict()

                subjects_authorized_list.append(subjects_authorized_list_item)




        subjects_other_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subjects_other_list, Unset):
            subjects_other_list = []
            for subjects_other_list_item_data in self.subjects_other_list:
                subjects_other_list_item = subjects_other_list_item_data.to_dict()

                subjects_other_list.append(subjects_other_list_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "acquisitionTimestamp": acquisition_timestamp,
            "currency": currency,
            "faP17Annotation": fa_p17_annotation,
            "gross": gross,
            "invoiceHash": invoice_hash,
            "invoiceReferenceNumber": invoice_reference_number,
            "invoiceType": invoice_type,
            "invoicingDate": invoicing_date,
            "ksefReferenceNumber": ksef_reference_number,
            "net": net,
            "subjectBy": subject_by,
            "subjectTo": subject_to,
            "vat": vat,
        })
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version
        if subject_by_k is not UNSET:
            field_dict["subjectByK"] = subject_by_k
        if subject_to_k_list is not UNSET:
            field_dict["subjectToKList"] = subject_to_k_list
        if subjects_authorized_list is not UNSET:
            field_dict["subjectsAuthorizedList"] = subjects_authorized_list
        if subjects_other_list is not UNSET:
            field_dict["subjectsOtherList"] = subjects_other_list

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_other_type import SubjectOtherType
        from ..models.subject_authorized_type import SubjectAuthorizedType
        from ..models.file_unlimited_hash_type import FileUnlimitedHashType
        from ..models.subject_to_type import SubjectToType
        from ..models.subject_by_type import SubjectByType
        d = src_dict.copy()
        acquisition_timestamp = isoparse(d.pop("acquisitionTimestamp"))




        currency = d.pop("currency")

        fa_p17_annotation = d.pop("faP17Annotation")

        gross = d.pop("gross")

        invoice_hash = FileUnlimitedHashType.from_dict(d.pop("invoiceHash"))




        invoice_reference_number = d.pop("invoiceReferenceNumber")

        invoice_type = InvoiceHeaderTypeInvoiceType(d.pop("invoiceType"))




        invoicing_date = isoparse(d.pop("invoicingDate")).date()




        ksef_reference_number = d.pop("ksefReferenceNumber")

        net = d.pop("net")

        subject_by = SubjectByType.from_dict(d.pop("subjectBy"))




        subject_to = SubjectToType.from_dict(d.pop("subjectTo"))




        vat = d.pop("vat")

        schema_version = d.pop("schemaVersion", UNSET)

        _subject_by_k = d.pop("subjectByK", UNSET)
        subject_by_k: Union[Unset, SubjectByType]
        if isinstance(_subject_by_k,  Unset):
            subject_by_k = UNSET
        else:
            subject_by_k = SubjectByType.from_dict(_subject_by_k)




        subject_to_k_list = []
        _subject_to_k_list = d.pop("subjectToKList", UNSET)
        for subject_to_k_list_item_data in (_subject_to_k_list or []):
            subject_to_k_list_item = SubjectToType.from_dict(subject_to_k_list_item_data)



            subject_to_k_list.append(subject_to_k_list_item)


        subjects_authorized_list = []
        _subjects_authorized_list = d.pop("subjectsAuthorizedList", UNSET)
        for subjects_authorized_list_item_data in (_subjects_authorized_list or []):
            subjects_authorized_list_item = SubjectAuthorizedType.from_dict(subjects_authorized_list_item_data)



            subjects_authorized_list.append(subjects_authorized_list_item)


        subjects_other_list = []
        _subjects_other_list = d.pop("subjectsOtherList", UNSET)
        for subjects_other_list_item_data in (_subjects_other_list or []):
            subjects_other_list_item = SubjectOtherType.from_dict(subjects_other_list_item_data)



            subjects_other_list.append(subjects_other_list_item)


        invoice_header_type = cls(
            acquisition_timestamp=acquisition_timestamp,
            currency=currency,
            fa_p17_annotation=fa_p17_annotation,
            gross=gross,
            invoice_hash=invoice_hash,
            invoice_reference_number=invoice_reference_number,
            invoice_type=invoice_type,
            invoicing_date=invoicing_date,
            ksef_reference_number=ksef_reference_number,
            net=net,
            subject_by=subject_by,
            subject_to=subject_to,
            vat=vat,
            schema_version=schema_version,
            subject_by_k=subject_by_k,
            subject_to_k_list=subject_to_k_list,
            subjects_authorized_list=subjects_authorized_list,
            subjects_other_list=subjects_other_list,
        )

        invoice_header_type.additional_properties = d
        return invoice_header_type

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
