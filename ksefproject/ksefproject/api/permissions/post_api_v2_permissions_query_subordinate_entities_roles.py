from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.query_subordinate_entity_roles_response import QuerySubordinateEntityRolesResponse
from ...models.subordinate_entity_roles_query_request import SubordinateEntityRolesQueryRequest
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: SubordinateEntityRolesQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["pageOffset"] = page_offset

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/permissions/query/subordinate-entities/roles",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]:
    if response.status_code == 200:
        response_200 = QuerySubordinateEntityRolesResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubordinateEntityRolesQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]:
    """ Pobranie listy podmiotów podrzędnych

      Metoda pozwala na odczytanie listy podmiotów podrzędnych,
     jeżeli podmiot bieżącego kontekstu ma rolę podmiotu nadrzędnego:
     - **nadrzędna JST** – odczytywane są podrzędne JST,
     - **grupa VAT** – odczytywane są podmioty będące członkami grupy VAT.

     Role podmiotów zwracane przez operację obejmują:
     - **LocalGovernmentSubUnit** – podrzędne JST,
     - **VatGroupSubUnit** – członek grupy VAT.

     Odpowiedź może być filtrowana według parametru:
     - **subordinateEntityIdentifier** – identyfikator podmiotu podrzędnego.

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy podmiotów podrzędnych](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-podmiot%C3%B3w-podrz%C4%99dnych)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`, `SubunitManage`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (SubordinateEntityRolesQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]
     """


    kwargs = _get_kwargs(
        body=body,
page_offset=page_offset,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: SubordinateEntityRolesQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]:
    """ Pobranie listy podmiotów podrzędnych

      Metoda pozwala na odczytanie listy podmiotów podrzędnych,
     jeżeli podmiot bieżącego kontekstu ma rolę podmiotu nadrzędnego:
     - **nadrzędna JST** – odczytywane są podrzędne JST,
     - **grupa VAT** – odczytywane są podmioty będące członkami grupy VAT.

     Role podmiotów zwracane przez operację obejmują:
     - **LocalGovernmentSubUnit** – podrzędne JST,
     - **VatGroupSubUnit** – członek grupy VAT.

     Odpowiedź może być filtrowana według parametru:
     - **subordinateEntityIdentifier** – identyfikator podmiotu podrzędnego.

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy podmiotów podrzędnych](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-podmiot%C3%B3w-podrz%C4%99dnych)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`, `SubunitManage`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (SubordinateEntityRolesQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]
     """


    return sync_detailed(
        client=client,
body=body,
page_offset=page_offset,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubordinateEntityRolesQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]:
    """ Pobranie listy podmiotów podrzędnych

      Metoda pozwala na odczytanie listy podmiotów podrzędnych,
     jeżeli podmiot bieżącego kontekstu ma rolę podmiotu nadrzędnego:
     - **nadrzędna JST** – odczytywane są podrzędne JST,
     - **grupa VAT** – odczytywane są podmioty będące członkami grupy VAT.

     Role podmiotów zwracane przez operację obejmują:
     - **LocalGovernmentSubUnit** – podrzędne JST,
     - **VatGroupSubUnit** – członek grupy VAT.

     Odpowiedź może być filtrowana według parametru:
     - **subordinateEntityIdentifier** – identyfikator podmiotu podrzędnego.

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy podmiotów podrzędnych](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-podmiot%C3%B3w-podrz%C4%99dnych)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`, `SubunitManage`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (SubordinateEntityRolesQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]
     """


    kwargs = _get_kwargs(
        body=body,
page_offset=page_offset,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubordinateEntityRolesQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]]:
    """ Pobranie listy podmiotów podrzędnych

      Metoda pozwala na odczytanie listy podmiotów podrzędnych,
     jeżeli podmiot bieżącego kontekstu ma rolę podmiotu nadrzędnego:
     - **nadrzędna JST** – odczytywane są podrzędne JST,
     - **grupa VAT** – odczytywane są podmioty będące członkami grupy VAT.

     Role podmiotów zwracane przez operację obejmują:
     - **LocalGovernmentSubUnit** – podrzędne JST,
     - **VatGroupSubUnit** – członek grupy VAT.

     Odpowiedź może być filtrowana według parametru:
     - **subordinateEntityIdentifier** – identyfikator podmiotu podrzędnego.

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy podmiotów podrzędnych](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-podmiot%C3%B3w-podrz%C4%99dnych)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`, `SubunitManage`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (SubordinateEntityRolesQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QuerySubordinateEntityRolesResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_offset=page_offset,
page_size=page_size,

    )).parsed
