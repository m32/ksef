from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.part_upload_request import PartUploadRequest





T = TypeVar("T", bound="OpenBatchSessionResponse")



@_attrs_define
class OpenBatchSessionResponse:
    """ 
        Attributes:
            reference_number (str): Numer referencyjny.
            part_upload_requests (list['PartUploadRequest']): Dane wymagane do poprawnego przesłania poszczególnych części
                pliku paczki faktur.

                Każdą część pliku paczki zadeklarowaną w <b>fileParts</b> należy przesłać zgodnie z odpowiadającym jej obiektem
                w <b>partUploadRequests</b>.
                Łącznikiem pomiędzy deklaracją a instrukcją wysyłki jest pole <b>ordinalNumber</b>.

                Dla każdej części należy:
                * zastosować metodę HTTP wskazaną w <b>method</b>,
                * ustawić adres z <b>url</b>,
                * dołączyć nagłówki z <b>headers</b>,
                * dołączyć treść części pliku w korpusie żądania.

                `Uwaga: nie należy dodawać do nagłówków token dostępu (accessToken).`

                Każdą część przesyła się oddzielnym żądaniem HTTP.Zwracane kody odpowiedzi:
                 * <b>201</b> – poprawne przyjęcie pliku,
                 * <b>400</b> – błędne dane,
                 * <b>401</b> – nieprawidłowe uwierzytelnienie,
                 * <b>403</b> – brak uprawnień do zapisu (np.upłynął czas na zapis).
     """

    reference_number: str
    part_upload_requests: list['PartUploadRequest']





    def to_dict(self) -> dict[str, Any]:
        from ..models.part_upload_request import PartUploadRequest
        reference_number = self.reference_number

        part_upload_requests = []
        for part_upload_requests_item_data in self.part_upload_requests:
            part_upload_requests_item = part_upload_requests_item_data.to_dict()
            part_upload_requests.append(part_upload_requests_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "referenceNumber": reference_number,
            "partUploadRequests": part_upload_requests,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.part_upload_request import PartUploadRequest
        d = dict(src_dict)
        reference_number = d.pop("referenceNumber")

        part_upload_requests = []
        _part_upload_requests = d.pop("partUploadRequests")
        for part_upload_requests_item_data in (_part_upload_requests):
            part_upload_requests_item = PartUploadRequest.from_dict(part_upload_requests_item_data)



            part_upload_requests.append(part_upload_requests_item)


        open_batch_session_response = cls(
            reference_number=reference_number,
            part_upload_requests=part_upload_requests,
        )

        return open_batch_session_response

