from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.entity_authorization_permissions_query_request import EntityAuthorizationPermissionsQueryRequest
from ...models.exception_response import ExceptionResponse
from ...models.query_entity_authorization_permissions_response import QueryEntityAuthorizationPermissionsResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: EntityAuthorizationPermissionsQueryRequest,
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
        "url": "/api/v2/permissions/query/authorizations/grants",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]:
    if response.status_code == 200:
        response_200 = QueryEntityAuthorizationPermissionsResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EntityAuthorizationPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]:
    """ Pobranie listy uprawnień podmiotowych do obsługi faktur

      Metoda pozwala na odczytanie uprawnień podmiotowych:
     - otrzymanych przez podmiot bieżącego kontekstu
     - nadanych przez podmiot bieżącego kontekstu

     Wybór listy nadanych lub otrzymanych uprawnień odbywa się przy użyciu parametru **queryType**.

     Uprawnienia zwracane przez operację obejmują:
     - **SelfInvoicing** – wystawianie faktur w trybie samofakturowania
     - **TaxRepresentative** – wykonywanie operacji przedstawiciela podatkowego
     - **RRInvoicing** – wystawianie faktur VAT RR
     - **PefInvoicing** – wystawianie faktur PEF

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **authorizingIdentifier** – identyfikator podmiotu uprawniającego (stosowane przy queryType =
    Received)
     - **authorizedIdentifier** – identyfikator podmiotu uprawnionego (stosowane przy queryType =
    Granted)
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-podmiotowych-do-obs%C5%82ugi-faktur)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (EntityAuthorizationPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]
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
    body: EntityAuthorizationPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]:
    """ Pobranie listy uprawnień podmiotowych do obsługi faktur

      Metoda pozwala na odczytanie uprawnień podmiotowych:
     - otrzymanych przez podmiot bieżącego kontekstu
     - nadanych przez podmiot bieżącego kontekstu

     Wybór listy nadanych lub otrzymanych uprawnień odbywa się przy użyciu parametru **queryType**.

     Uprawnienia zwracane przez operację obejmują:
     - **SelfInvoicing** – wystawianie faktur w trybie samofakturowania
     - **TaxRepresentative** – wykonywanie operacji przedstawiciela podatkowego
     - **RRInvoicing** – wystawianie faktur VAT RR
     - **PefInvoicing** – wystawianie faktur PEF

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **authorizingIdentifier** – identyfikator podmiotu uprawniającego (stosowane przy queryType =
    Received)
     - **authorizedIdentifier** – identyfikator podmiotu uprawnionego (stosowane przy queryType =
    Granted)
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-podmiotowych-do-obs%C5%82ugi-faktur)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (EntityAuthorizationPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]
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
    body: EntityAuthorizationPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]:
    """ Pobranie listy uprawnień podmiotowych do obsługi faktur

      Metoda pozwala na odczytanie uprawnień podmiotowych:
     - otrzymanych przez podmiot bieżącego kontekstu
     - nadanych przez podmiot bieżącego kontekstu

     Wybór listy nadanych lub otrzymanych uprawnień odbywa się przy użyciu parametru **queryType**.

     Uprawnienia zwracane przez operację obejmują:
     - **SelfInvoicing** – wystawianie faktur w trybie samofakturowania
     - **TaxRepresentative** – wykonywanie operacji przedstawiciela podatkowego
     - **RRInvoicing** – wystawianie faktur VAT RR
     - **PefInvoicing** – wystawianie faktur PEF

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **authorizingIdentifier** – identyfikator podmiotu uprawniającego (stosowane przy queryType =
    Received)
     - **authorizedIdentifier** – identyfikator podmiotu uprawnionego (stosowane przy queryType =
    Granted)
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-podmiotowych-do-obs%C5%82ugi-faktur)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (EntityAuthorizationPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]
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
    body: EntityAuthorizationPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]]:
    """ Pobranie listy uprawnień podmiotowych do obsługi faktur

      Metoda pozwala na odczytanie uprawnień podmiotowych:
     - otrzymanych przez podmiot bieżącego kontekstu
     - nadanych przez podmiot bieżącego kontekstu

     Wybór listy nadanych lub otrzymanych uprawnień odbywa się przy użyciu parametru **queryType**.

     Uprawnienia zwracane przez operację obejmują:
     - **SelfInvoicing** – wystawianie faktur w trybie samofakturowania
     - **TaxRepresentative** – wykonywanie operacji przedstawiciela podatkowego
     - **RRInvoicing** – wystawianie faktur VAT RR
     - **PefInvoicing** – wystawianie faktur PEF

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **authorizingIdentifier** – identyfikator podmiotu uprawniającego (stosowane przy queryType =
    Received)
     - **authorizedIdentifier** – identyfikator podmiotu uprawnionego (stosowane przy queryType =
    Granted)
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-podmiotowych-do-obs%C5%82ugi-faktur)

    **Sortowanie:**

    - startDate (Desc)



    **Wymagane uprawnienia**: `CredentialsManage`, `CredentialsRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (EntityAuthorizationPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryEntityAuthorizationPermissionsResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_offset=page_offset,
page_size=page_size,

    )).parsed
