from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.query_entity_roles_response import QueryEntityRolesResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageOffset"] = page_offset

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/permissions/query/entities/roles",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]:
    if response.status_code == 200:
        response_200 = QueryEntityRolesResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]:
    """ Pobranie listy ról podmiotu

      Metoda pozwala na **odczytanie listy ról podmiotu bieżącego kontekstu logowania**.

    #### Role podmiotów zwracane przez operację:
    - **CourtBailiff** – komornik sądowy
    - **EnforcementAuthority** – organ egzekucyjny
    - **LocalGovernmentUnit** – nadrzędna JST
    - **LocalGovernmentSubUnit** – podrzędne JST
    - **VatGroupUnit** – grupa VAT
    - **VatGroupSubUnit** – członek grupy VAT

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy ról](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#pobranie-
    listy-r%C3%B3l-podmiotu)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]
     """


    kwargs = _get_kwargs(
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
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]:
    """ Pobranie listy ról podmiotu

      Metoda pozwala na **odczytanie listy ról podmiotu bieżącego kontekstu logowania**.

    #### Role podmiotów zwracane przez operację:
    - **CourtBailiff** – komornik sądowy
    - **EnforcementAuthority** – organ egzekucyjny
    - **LocalGovernmentUnit** – nadrzędna JST
    - **LocalGovernmentSubUnit** – podrzędne JST
    - **VatGroupUnit** – grupa VAT
    - **VatGroupSubUnit** – członek grupy VAT

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy ról](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#pobranie-
    listy-r%C3%B3l-podmiotu)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryEntityRolesResponse]
     """


    return sync_detailed(
        client=client,
page_offset=page_offset,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]:
    """ Pobranie listy ról podmiotu

      Metoda pozwala na **odczytanie listy ról podmiotu bieżącego kontekstu logowania**.

    #### Role podmiotów zwracane przez operację:
    - **CourtBailiff** – komornik sądowy
    - **EnforcementAuthority** – organ egzekucyjny
    - **LocalGovernmentUnit** – nadrzędna JST
    - **LocalGovernmentSubUnit** – podrzędne JST
    - **VatGroupUnit** – grupa VAT
    - **VatGroupSubUnit** – członek grupy VAT

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy ról](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#pobranie-
    listy-r%C3%B3l-podmiotu)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]
     """


    kwargs = _get_kwargs(
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
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryEntityRolesResponse]]:
    """ Pobranie listy ról podmiotu

      Metoda pozwala na **odczytanie listy ról podmiotu bieżącego kontekstu logowania**.

    #### Role podmiotów zwracane przez operację:
    - **CourtBailiff** – komornik sądowy
    - **EnforcementAuthority** – organ egzekucyjny
    - **LocalGovernmentUnit** – nadrzędna JST
    - **LocalGovernmentSubUnit** – podrzędne JST
    - **VatGroupUnit** – grupa VAT
    - **VatGroupSubUnit** – członek grupy VAT

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy ról](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#pobranie-
    listy-r%C3%B3l-podmiotu)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryEntityRolesResponse]
     """


    return (await asyncio_detailed(
        client=client,
page_offset=page_offset,
page_size=page_size,

    )).parsed
