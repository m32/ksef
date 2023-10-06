import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.subject_authorized_type import SubjectAuthorizedType
from ..models.subject_by_type import SubjectByType
from ..models.subject_other_type import SubjectOtherType
from ..models.subject_to_type import SubjectToType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceHeaderType")


@attr.s(auto_attribs=True)
class InvoiceHeaderType:
    """
    Attributes:
        invoice_reference_number (str):
        ksef_reference_number (str):
        invoicing_date (datetime.datetime):
        acquisition_timestamp (datetime.datetime):
        subject_by (SubjectByType):
        subject_to (SubjectToType):
        net (str):
        vat (str):
        gross (str):
        subject_by_k (Union[Unset, SubjectByType]):
        subject_to_k_list (Union[Unset, List[SubjectToType]]):
        subjects_other_list (Union[Unset, List[SubjectOtherType]]):
        subjects_authorized_list (Union[Unset, List[SubjectAuthorizedType]]):
    """

    invoice_reference_number: str
    ksef_reference_number: str
    invoicing_date: datetime.datetime
    acquisition_timestamp: datetime.datetime
    subject_by: SubjectByType
    subject_to: SubjectToType
    net: str
    vat: str
    gross: str
    subject_by_k: Union[Unset, SubjectByType] = UNSET
    subject_to_k_list: Union[Unset, List[SubjectToType]] = UNSET
    subjects_other_list: Union[Unset, List[SubjectOtherType]] = UNSET
    subjects_authorized_list: Union[Unset, List[SubjectAuthorizedType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_reference_number = self.invoice_reference_number
        ksef_reference_number = self.ksef_reference_number
        invoicing_date = self.invoicing_date.isoformat()

        acquisition_timestamp = self.acquisition_timestamp.isoformat()

        subject_by = self.subject_by.to_dict()

        subject_to = self.subject_to.to_dict()

        net = self.net
        vat = self.vat
        gross = self.gross
        subject_by_k: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject_by_k, Unset):
            subject_by_k = self.subject_by_k.to_dict()

        subject_to_k_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subject_to_k_list, Unset):
            subject_to_k_list = []
            for subject_to_k_list_item_data in self.subject_to_k_list:
                subject_to_k_list_item = subject_to_k_list_item_data.to_dict()

                subject_to_k_list.append(subject_to_k_list_item)

        subjects_other_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subjects_other_list, Unset):
            subjects_other_list = []
            for subjects_other_list_item_data in self.subjects_other_list:
                subjects_other_list_item = subjects_other_list_item_data.to_dict()

                subjects_other_list.append(subjects_other_list_item)

        subjects_authorized_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subjects_authorized_list, Unset):
            subjects_authorized_list = []
            for subjects_authorized_list_item_data in self.subjects_authorized_list:
                subjects_authorized_list_item = subjects_authorized_list_item_data.to_dict()

                subjects_authorized_list.append(subjects_authorized_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceReferenceNumber": invoice_reference_number,
                "ksefReferenceNumber": ksef_reference_number,
                "invoicingDate": invoicing_date,
                "acquisitionTimestamp": acquisition_timestamp,
                "subjectBy": subject_by,
                "subjectTo": subject_to,
                "net": net,
                "vat": vat,
                "gross": gross,
            }
        )
        if subject_by_k is not UNSET:
            field_dict["subjectByK"] = subject_by_k
        if subject_to_k_list is not UNSET:
            field_dict["subjectToKList"] = subject_to_k_list
        if subjects_other_list is not UNSET:
            field_dict["subjectsOtherList"] = subjects_other_list
        if subjects_authorized_list is not UNSET:
            field_dict["subjectsAuthorizedList"] = subjects_authorized_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_reference_number = d.pop("invoiceReferenceNumber")

        ksef_reference_number = d.pop("ksefReferenceNumber")

        invoicing_date = isoparse(d.pop("invoicingDate"))

        acquisition_timestamp = isoparse(d.pop("acquisitionTimestamp"))

        subject_by = SubjectByType.from_dict(d.pop("subjectBy"))

        subject_to = SubjectToType.from_dict(d.pop("subjectTo"))

        net = d.pop("net")

        vat = d.pop("vat")

        gross = d.pop("gross")

        _subject_by_k = d.pop("subjectByK", UNSET)
        subject_by_k: Union[Unset, SubjectByType]
        if isinstance(_subject_by_k, Unset):
            subject_by_k = UNSET
        else:
            subject_by_k = SubjectByType.from_dict(_subject_by_k)

        subject_to_k_list = []
        _subject_to_k_list = d.pop("subjectToKList", UNSET)
        for subject_to_k_list_item_data in _subject_to_k_list or []:
            subject_to_k_list_item = SubjectToType.from_dict(subject_to_k_list_item_data)

            subject_to_k_list.append(subject_to_k_list_item)

        subjects_other_list = []
        _subjects_other_list = d.pop("subjectsOtherList", UNSET)
        for subjects_other_list_item_data in _subjects_other_list or []:
            subjects_other_list_item = SubjectOtherType.from_dict(subjects_other_list_item_data)

            subjects_other_list.append(subjects_other_list_item)

        subjects_authorized_list = []
        _subjects_authorized_list = d.pop("subjectsAuthorizedList", UNSET)
        for subjects_authorized_list_item_data in _subjects_authorized_list or []:
            subjects_authorized_list_item = SubjectAuthorizedType.from_dict(subjects_authorized_list_item_data)

            subjects_authorized_list.append(subjects_authorized_list_item)

        invoice_header_type = cls(
            invoice_reference_number=invoice_reference_number,
            ksef_reference_number=ksef_reference_number,
            invoicing_date=invoicing_date,
            acquisition_timestamp=acquisition_timestamp,
            subject_by=subject_by,
            subject_to=subject_to,
            net=net,
            vat=vat,
            gross=gross,
            subject_by_k=subject_by_k,
            subject_to_k_list=subject_to_k_list,
            subjects_other_list=subjects_other_list,
            subjects_authorized_list=subjects_authorized_list,
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
