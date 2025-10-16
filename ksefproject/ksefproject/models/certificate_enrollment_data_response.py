from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CertificateEnrollmentDataResponse")



@_attrs_define
class CertificateEnrollmentDataResponse:
    """ 
        Attributes:
            common_name (str): Nazwa powszechna.
            country_name (str): Kraj, kod ISO 3166.
            given_name (Union[None, Unset, str]): Imię.
            surname (Union[None, Unset, str]): Nazwisko.
            serial_number (Union[None, Unset, str]): Numer seryjny podmiotu.
            unique_identifier (Union[None, Unset, str]): Unikalny identyfikator.
            organization_name (Union[None, Unset, str]): Nazwa organizacji.
            organization_identifier (Union[None, Unset, str]): Identyfikator organizacji.
     """

    common_name: str
    country_name: str
    given_name: Union[None, Unset, str] = UNSET
    surname: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    unique_identifier: Union[None, Unset, str] = UNSET
    organization_name: Union[None, Unset, str] = UNSET
    organization_identifier: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        common_name = self.common_name

        country_name = self.country_name

        given_name: Union[None, Unset, str]
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        surname: Union[None, Unset, str]
        if isinstance(self.surname, Unset):
            surname = UNSET
        else:
            surname = self.surname

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        unique_identifier: Union[None, Unset, str]
        if isinstance(self.unique_identifier, Unset):
            unique_identifier = UNSET
        else:
            unique_identifier = self.unique_identifier

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        organization_identifier: Union[None, Unset, str]
        if isinstance(self.organization_identifier, Unset):
            organization_identifier = UNSET
        else:
            organization_identifier = self.organization_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "commonName": common_name,
            "countryName": country_name,
        })
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if unique_identifier is not UNSET:
            field_dict["uniqueIdentifier"] = unique_identifier
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if organization_identifier is not UNSET:
            field_dict["organizationIdentifier"] = organization_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        common_name = d.pop("commonName")

        country_name = d.pop("countryName")

        def _parse_given_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))


        def _parse_surname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        surname = _parse_surname(d.pop("surname", UNSET))


        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))


        def _parse_unique_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unique_identifier = _parse_unique_identifier(d.pop("uniqueIdentifier", UNSET))


        def _parse_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))


        def _parse_organization_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_identifier = _parse_organization_identifier(d.pop("organizationIdentifier", UNSET))


        certificate_enrollment_data_response = cls(
            common_name=common_name,
            country_name=country_name,
            given_name=given_name,
            surname=surname,
            serial_number=serial_number,
            unique_identifier=unique_identifier,
            organization_name=organization_name,
            organization_identifier=organization_identifier,
        )

        return certificate_enrollment_data_response

