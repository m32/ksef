from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.personal_permissions_query_request import PersonalPermissionsQueryRequest
from ...models.query_personal_permissions_response import QueryPersonalPermissionsResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: PersonalPermissionsQueryRequest,
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
        "url": "/api/v2/permissions/query/personal/grants",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]:
    if response.status_code == 200:
        response_200 = QueryPersonalPermissionsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PersonalPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]:
    """ Pobranie listy własnych uprawnień

      Metoda pozwala na odczytanie własnych uprawnień uwierzytelnionego klienta API w bieżącym kontekście
    logowania.

     W odpowiedzi przekazywane są następujące uprawnienia:
     - nadane w sposób bezpośredni w bieżącym kontekście
     - nadane przez podmiot nadrzędny
     - nadane w sposób pośredni, jeżeli podmiot kontekstu logowania jest w uprawnieniu pośrednikiem lub
    podmiotem docelowym
     - nadane podmiotowi do obsługi faktur przez inny podmiot, jeśli podmiot uwierzytelniony ma w
    bieżącym kontekście uprawnienia właścicielskie

     Uprawnienia zwracane przez operację obejmują:
     - **CredentialsManage** – zarządzanie uprawnieniami
     - **CredentialsRead** – przeglądanie uprawnień
     - **InvoiceWrite** – wystawianie faktur
     - **InvoiceRead** – przeglądanie faktur
     - **Introspection** – przeglądanie historii sesji
     - **SubunitManage** – zarządzanie podmiotami podrzędnymi
     - **EnforcementOperations** – wykonywanie operacji egzekucyjnych
     - **VatEuManage** – zarządzanie uprawnieniami w ramach podmiotu unijnego

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **contextIdentifier** – identyfikator podmiotu, który nadał uprawnienie do obsługi faktur
     - **targetIdentifier** – identyfikator podmiotu docelowego dla uprawnień nadanych pośrednio
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień
     - **permissionState** – status uprawnienia

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-w%C5%82asnych-uprawnie%C5%84)

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (PersonalPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]
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
    body: PersonalPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]:
    """ Pobranie listy własnych uprawnień

      Metoda pozwala na odczytanie własnych uprawnień uwierzytelnionego klienta API w bieżącym kontekście
    logowania.

     W odpowiedzi przekazywane są następujące uprawnienia:
     - nadane w sposób bezpośredni w bieżącym kontekście
     - nadane przez podmiot nadrzędny
     - nadane w sposób pośredni, jeżeli podmiot kontekstu logowania jest w uprawnieniu pośrednikiem lub
    podmiotem docelowym
     - nadane podmiotowi do obsługi faktur przez inny podmiot, jeśli podmiot uwierzytelniony ma w
    bieżącym kontekście uprawnienia właścicielskie

     Uprawnienia zwracane przez operację obejmują:
     - **CredentialsManage** – zarządzanie uprawnieniami
     - **CredentialsRead** – przeglądanie uprawnień
     - **InvoiceWrite** – wystawianie faktur
     - **InvoiceRead** – przeglądanie faktur
     - **Introspection** – przeglądanie historii sesji
     - **SubunitManage** – zarządzanie podmiotami podrzędnymi
     - **EnforcementOperations** – wykonywanie operacji egzekucyjnych
     - **VatEuManage** – zarządzanie uprawnieniami w ramach podmiotu unijnego

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **contextIdentifier** – identyfikator podmiotu, który nadał uprawnienie do obsługi faktur
     - **targetIdentifier** – identyfikator podmiotu docelowego dla uprawnień nadanych pośrednio
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień
     - **permissionState** – status uprawnienia

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-w%C5%82asnych-uprawnie%C5%84)

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (PersonalPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]
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
    body: PersonalPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]:
    """ Pobranie listy własnych uprawnień

      Metoda pozwala na odczytanie własnych uprawnień uwierzytelnionego klienta API w bieżącym kontekście
    logowania.

     W odpowiedzi przekazywane są następujące uprawnienia:
     - nadane w sposób bezpośredni w bieżącym kontekście
     - nadane przez podmiot nadrzędny
     - nadane w sposób pośredni, jeżeli podmiot kontekstu logowania jest w uprawnieniu pośrednikiem lub
    podmiotem docelowym
     - nadane podmiotowi do obsługi faktur przez inny podmiot, jeśli podmiot uwierzytelniony ma w
    bieżącym kontekście uprawnienia właścicielskie

     Uprawnienia zwracane przez operację obejmują:
     - **CredentialsManage** – zarządzanie uprawnieniami
     - **CredentialsRead** – przeglądanie uprawnień
     - **InvoiceWrite** – wystawianie faktur
     - **InvoiceRead** – przeglądanie faktur
     - **Introspection** – przeglądanie historii sesji
     - **SubunitManage** – zarządzanie podmiotami podrzędnymi
     - **EnforcementOperations** – wykonywanie operacji egzekucyjnych
     - **VatEuManage** – zarządzanie uprawnieniami w ramach podmiotu unijnego

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **contextIdentifier** – identyfikator podmiotu, który nadał uprawnienie do obsługi faktur
     - **targetIdentifier** – identyfikator podmiotu docelowego dla uprawnień nadanych pośrednio
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień
     - **permissionState** – status uprawnienia

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-w%C5%82asnych-uprawnie%C5%84)

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (PersonalPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]
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
    body: PersonalPermissionsQueryRequest,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]]:
    """ Pobranie listy własnych uprawnień

      Metoda pozwala na odczytanie własnych uprawnień uwierzytelnionego klienta API w bieżącym kontekście
    logowania.

     W odpowiedzi przekazywane są następujące uprawnienia:
     - nadane w sposób bezpośredni w bieżącym kontekście
     - nadane przez podmiot nadrzędny
     - nadane w sposób pośredni, jeżeli podmiot kontekstu logowania jest w uprawnieniu pośrednikiem lub
    podmiotem docelowym
     - nadane podmiotowi do obsługi faktur przez inny podmiot, jeśli podmiot uwierzytelniony ma w
    bieżącym kontekście uprawnienia właścicielskie

     Uprawnienia zwracane przez operację obejmują:
     - **CredentialsManage** – zarządzanie uprawnieniami
     - **CredentialsRead** – przeglądanie uprawnień
     - **InvoiceWrite** – wystawianie faktur
     - **InvoiceRead** – przeglądanie faktur
     - **Introspection** – przeglądanie historii sesji
     - **SubunitManage** – zarządzanie podmiotami podrzędnymi
     - **EnforcementOperations** – wykonywanie operacji egzekucyjnych
     - **VatEuManage** – zarządzanie uprawnieniami w ramach podmiotu unijnego

     Odpowiedź może być filtrowana na podstawie następujących parametrów:
     - **contextIdentifier** – identyfikator podmiotu, który nadał uprawnienie do obsługi faktur
     - **targetIdentifier** – identyfikator podmiotu docelowego dla uprawnień nadanych pośrednio
     - **permissionTypes** – lista rodzajów wyszukiwanych uprawnień
     - **permissionState** – status uprawnienia

    #### Stronicowanie wyników
    Zapytanie zwraca **jedną stronę wyników** o numerze i rozmiarze podanym w ścieżce.
    - Przy pierwszym wywołaniu należy ustawić parametr `pageOffset = 0`.
    - Jeżeli dostępna jest kolejna strona wyników, w odpowiedzi pojawi się flaga **`hasMore`**.
    - W takim przypadku można wywołać zapytanie ponownie z kolejnym numerem strony.

     > Więcej informacji:
     > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-w%C5%82asnych-uprawnie%C5%84)

    **Sortowanie:**

    - startDate (Desc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (PersonalPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryPersonalPermissionsResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_offset=page_offset,
page_size=page_size,

    )).parsed
