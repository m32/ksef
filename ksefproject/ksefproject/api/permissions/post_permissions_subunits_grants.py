from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.permissions_operation_response import PermissionsOperationResponse
from ...models.subunit_permissions_grant_request import SubunitPermissionsGrantRequest
from ...models.too_many_requests_response import TooManyRequestsResponse
from typing import cast



def _get_kwargs(
    *,
    body: SubunitPermissionsGrantRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/permissions/subunits/grants",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]:
    if response.status_code == 202:
        response_202 = PermissionsOperationResponse.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = TooManyRequestsResponse.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubunitPermissionsGrantRequest,

) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]:
    r""" Nadanie uprawnień administratora podmiotu podrzędnego

     Metoda pozwala na nadanie wskazanemu w żądaniu podmiotowi lub osobie fizycznej uprawnień
    administratora w kontekście:
    - wskazanego NIP podmiotu podrzędnego – wyłącznie jeżeli podmiot bieżącego kontekstu logowania ma
    rolę podmiotu nadrzędnego:
      - **LocalGovernmentUnit**
      - **VatGroupUnit**
    - wskazanego lub utworzonego identyfikatora wewnętrznego

    Wraz z utworzeniem administratora jednostki podrzędnej tworzony jest identyfikator wewnętrzny
    składający się z numeru NIP podmiotu kontekstu logowania oraz 5 cyfr unikalnie identyfikujących
    jednostkę wewnętrzną.
    Ostatnia cyfra musi być poprawną sumą kontrolną, która jest obliczana według poniższego algorytmu.

    Algorytm używa naprzemiennych wag (1×, 3×, 1×, 3×, ...), sumuje wyniki i zwraca resztę z dzielenia
    przez 10.

    Przykład:
    - Wejście: \"6824515772-1234\" (bez cyfry kontrolnej)
    - Pozycja 0 (1. cyfra): 6 × 1 = 6
    - Pozycja 1 (2. cyfra): 8 × 3 = 24
    - Pozycja 2 (3. cyfra): 2 × 1 = 2
    - Pozycja 3 (4. cyfra): 4 × 3 = 12
    - Pozycja 4 (5. cyfra): 5 × 1 = 5
    - Pozycja 5 (6. cyfra): 1 × 3 = 3
    - Pozycja 6 (7. cyfra): 5 × 1 = 5
    - Pozycja 7 (8. cyfra): 7 × 3 = 21
    - Pozycja 8 (9. cyfra): 7 × 1 = 7
    - Pozycja 9 (10. cyfra): 2 × 3 = 6
    - Pozycja 10 (11. cyfra): 1 × 1 = 1
    - Pozycja 11 (12. cyfra): 2 × 3 = 6
    - Pozycja 12 (13. cyfra): 3 × 1 = 3
    - Pozycja 13 (14. cyfra): 4 × 3 = 12
    - Suma: 6 + 24 + 2 + 12 + 5 + 3 + 5 + 21 + 7 + 6 + 1 + 6 + 3 + 12 = 113
    - Cyfra kontrolna (15. cyfra): 113 % 10 = 3

    W żądaniu podaje się również nazwę tej jednostki.

    Uprawnienia administratora jednostki podrzędnej obejmują:
    - **CredentialsManage** – zarządzanie uprawnieniami

    Metoda automatycznie nadaje powyższe uprawnienie, bez konieczności podawania go w żądaniu.

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadanie-
    uprawnie%C5%84-administratora-podmiotu-podrz%C4%99dnego)

    **Wymagane uprawnienia**: `SubunitManage`.

    Args:
        body (SubunitPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: SubunitPermissionsGrantRequest,

) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]:
    r""" Nadanie uprawnień administratora podmiotu podrzędnego

     Metoda pozwala na nadanie wskazanemu w żądaniu podmiotowi lub osobie fizycznej uprawnień
    administratora w kontekście:
    - wskazanego NIP podmiotu podrzędnego – wyłącznie jeżeli podmiot bieżącego kontekstu logowania ma
    rolę podmiotu nadrzędnego:
      - **LocalGovernmentUnit**
      - **VatGroupUnit**
    - wskazanego lub utworzonego identyfikatora wewnętrznego

    Wraz z utworzeniem administratora jednostki podrzędnej tworzony jest identyfikator wewnętrzny
    składający się z numeru NIP podmiotu kontekstu logowania oraz 5 cyfr unikalnie identyfikujących
    jednostkę wewnętrzną.
    Ostatnia cyfra musi być poprawną sumą kontrolną, która jest obliczana według poniższego algorytmu.

    Algorytm używa naprzemiennych wag (1×, 3×, 1×, 3×, ...), sumuje wyniki i zwraca resztę z dzielenia
    przez 10.

    Przykład:
    - Wejście: \"6824515772-1234\" (bez cyfry kontrolnej)
    - Pozycja 0 (1. cyfra): 6 × 1 = 6
    - Pozycja 1 (2. cyfra): 8 × 3 = 24
    - Pozycja 2 (3. cyfra): 2 × 1 = 2
    - Pozycja 3 (4. cyfra): 4 × 3 = 12
    - Pozycja 4 (5. cyfra): 5 × 1 = 5
    - Pozycja 5 (6. cyfra): 1 × 3 = 3
    - Pozycja 6 (7. cyfra): 5 × 1 = 5
    - Pozycja 7 (8. cyfra): 7 × 3 = 21
    - Pozycja 8 (9. cyfra): 7 × 1 = 7
    - Pozycja 9 (10. cyfra): 2 × 3 = 6
    - Pozycja 10 (11. cyfra): 1 × 1 = 1
    - Pozycja 11 (12. cyfra): 2 × 3 = 6
    - Pozycja 12 (13. cyfra): 3 × 1 = 3
    - Pozycja 13 (14. cyfra): 4 × 3 = 12
    - Suma: 6 + 24 + 2 + 12 + 5 + 3 + 5 + 21 + 7 + 6 + 1 + 6 + 3 + 12 = 113
    - Cyfra kontrolna (15. cyfra): 113 % 10 = 3

    W żądaniu podaje się również nazwę tej jednostki.

    Uprawnienia administratora jednostki podrzędnej obejmują:
    - **CredentialsManage** – zarządzanie uprawnieniami

    Metoda automatycznie nadaje powyższe uprawnienie, bez konieczności podawania go w żądaniu.

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadanie-
    uprawnie%C5%84-administratora-podmiotu-podrz%C4%99dnego)

    **Wymagane uprawnienia**: `SubunitManage`.

    Args:
        body (SubunitPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubunitPermissionsGrantRequest,

) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]:
    r""" Nadanie uprawnień administratora podmiotu podrzędnego

     Metoda pozwala na nadanie wskazanemu w żądaniu podmiotowi lub osobie fizycznej uprawnień
    administratora w kontekście:
    - wskazanego NIP podmiotu podrzędnego – wyłącznie jeżeli podmiot bieżącego kontekstu logowania ma
    rolę podmiotu nadrzędnego:
      - **LocalGovernmentUnit**
      - **VatGroupUnit**
    - wskazanego lub utworzonego identyfikatora wewnętrznego

    Wraz z utworzeniem administratora jednostki podrzędnej tworzony jest identyfikator wewnętrzny
    składający się z numeru NIP podmiotu kontekstu logowania oraz 5 cyfr unikalnie identyfikujących
    jednostkę wewnętrzną.
    Ostatnia cyfra musi być poprawną sumą kontrolną, która jest obliczana według poniższego algorytmu.

    Algorytm używa naprzemiennych wag (1×, 3×, 1×, 3×, ...), sumuje wyniki i zwraca resztę z dzielenia
    przez 10.

    Przykład:
    - Wejście: \"6824515772-1234\" (bez cyfry kontrolnej)
    - Pozycja 0 (1. cyfra): 6 × 1 = 6
    - Pozycja 1 (2. cyfra): 8 × 3 = 24
    - Pozycja 2 (3. cyfra): 2 × 1 = 2
    - Pozycja 3 (4. cyfra): 4 × 3 = 12
    - Pozycja 4 (5. cyfra): 5 × 1 = 5
    - Pozycja 5 (6. cyfra): 1 × 3 = 3
    - Pozycja 6 (7. cyfra): 5 × 1 = 5
    - Pozycja 7 (8. cyfra): 7 × 3 = 21
    - Pozycja 8 (9. cyfra): 7 × 1 = 7
    - Pozycja 9 (10. cyfra): 2 × 3 = 6
    - Pozycja 10 (11. cyfra): 1 × 1 = 1
    - Pozycja 11 (12. cyfra): 2 × 3 = 6
    - Pozycja 12 (13. cyfra): 3 × 1 = 3
    - Pozycja 13 (14. cyfra): 4 × 3 = 12
    - Suma: 6 + 24 + 2 + 12 + 5 + 3 + 5 + 21 + 7 + 6 + 1 + 6 + 3 + 12 = 113
    - Cyfra kontrolna (15. cyfra): 113 % 10 = 3

    W żądaniu podaje się również nazwę tej jednostki.

    Uprawnienia administratora jednostki podrzędnej obejmują:
    - **CredentialsManage** – zarządzanie uprawnieniami

    Metoda automatycznie nadaje powyższe uprawnienie, bez konieczności podawania go w żądaniu.

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadanie-
    uprawnie%C5%84-administratora-podmiotu-podrz%C4%99dnego)

    **Wymagane uprawnienia**: `SubunitManage`.

    Args:
        body (SubunitPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubunitPermissionsGrantRequest,

) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]]:
    r""" Nadanie uprawnień administratora podmiotu podrzędnego

     Metoda pozwala na nadanie wskazanemu w żądaniu podmiotowi lub osobie fizycznej uprawnień
    administratora w kontekście:
    - wskazanego NIP podmiotu podrzędnego – wyłącznie jeżeli podmiot bieżącego kontekstu logowania ma
    rolę podmiotu nadrzędnego:
      - **LocalGovernmentUnit**
      - **VatGroupUnit**
    - wskazanego lub utworzonego identyfikatora wewnętrznego

    Wraz z utworzeniem administratora jednostki podrzędnej tworzony jest identyfikator wewnętrzny
    składający się z numeru NIP podmiotu kontekstu logowania oraz 5 cyfr unikalnie identyfikujących
    jednostkę wewnętrzną.
    Ostatnia cyfra musi być poprawną sumą kontrolną, która jest obliczana według poniższego algorytmu.

    Algorytm używa naprzemiennych wag (1×, 3×, 1×, 3×, ...), sumuje wyniki i zwraca resztę z dzielenia
    przez 10.

    Przykład:
    - Wejście: \"6824515772-1234\" (bez cyfry kontrolnej)
    - Pozycja 0 (1. cyfra): 6 × 1 = 6
    - Pozycja 1 (2. cyfra): 8 × 3 = 24
    - Pozycja 2 (3. cyfra): 2 × 1 = 2
    - Pozycja 3 (4. cyfra): 4 × 3 = 12
    - Pozycja 4 (5. cyfra): 5 × 1 = 5
    - Pozycja 5 (6. cyfra): 1 × 3 = 3
    - Pozycja 6 (7. cyfra): 5 × 1 = 5
    - Pozycja 7 (8. cyfra): 7 × 3 = 21
    - Pozycja 8 (9. cyfra): 7 × 1 = 7
    - Pozycja 9 (10. cyfra): 2 × 3 = 6
    - Pozycja 10 (11. cyfra): 1 × 1 = 1
    - Pozycja 11 (12. cyfra): 2 × 3 = 6
    - Pozycja 12 (13. cyfra): 3 × 1 = 3
    - Pozycja 13 (14. cyfra): 4 × 3 = 12
    - Suma: 6 + 24 + 2 + 12 + 5 + 3 + 5 + 21 + 7 + 6 + 1 + 6 + 3 + 12 = 113
    - Cyfra kontrolna (15. cyfra): 113 % 10 = 3

    W żądaniu podaje się również nazwę tej jednostki.

    Uprawnienia administratora jednostki podrzędnej obejmują:
    - **CredentialsManage** – zarządzanie uprawnieniami

    Metoda automatycznie nadaje powyższe uprawnienie, bez konieczności podawania go w żądaniu.

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadanie-
    uprawnie%C5%84-administratora-podmiotu-podrz%C4%99dnego)

    **Wymagane uprawnienia**: `SubunitManage`.

    Args:
        body (SubunitPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, PermissionsOperationResponse, TooManyRequestsResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
