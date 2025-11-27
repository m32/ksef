from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.permissions_operation_response import PermissionsOperationResponse
from ...models.person_permissions_grant_request import PersonPermissionsGrantRequest
from typing import cast



def _get_kwargs(
    *,
    body: PersonPermissionsGrantRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/permissions/persons/grants",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PersonPermissionsGrantRequest,

) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Nadanie osobom fizycznym uprawnień do pracy w KSeF

     Metoda pozwala na nadanie osobie wskazanej w żądaniu uprawnień do pracy w KSeF
    w kontekście bieżącym.

    W żądaniu określane są nadawane uprawnienia ze zbioru:
    - **InvoiceWrite** – wystawianie faktur,
    - **InvoiceRead** – przeglądanie faktur,
    - **CredentialsManage** – zarządzanie uprawnieniami,
    - **CredentialsRead** – przeglądanie uprawnień,
    - **Introspection** – przeglądanie historii sesji i generowanie UPO,
    - **SubunitManage** – zarządzanie jednostkami podrzędnymi,
    - **EnforcementOperations** – wykonywanie operacji egzekucyjnych.

    Metoda pozwala na wybór dowolnej kombinacji powyższych uprawnień.
    Uprawnienie **EnforcementOperations** może być nadane wyłącznie wtedy,
    gdy podmiot kontekstu ma rolę **EnforcementAuthority** (organ egzekucyjny)
    lub **CourtBailiff** (komornik sądowy).

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadawanie-
    uprawnie%C5%84-osobom-fizycznym-do-pracy-w-ksef)

    **Wymagane uprawnienia**: `CredentialsManage`.

    Args:
        body (PersonPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]
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
    body: PersonPermissionsGrantRequest,

) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Nadanie osobom fizycznym uprawnień do pracy w KSeF

     Metoda pozwala na nadanie osobie wskazanej w żądaniu uprawnień do pracy w KSeF
    w kontekście bieżącym.

    W żądaniu określane są nadawane uprawnienia ze zbioru:
    - **InvoiceWrite** – wystawianie faktur,
    - **InvoiceRead** – przeglądanie faktur,
    - **CredentialsManage** – zarządzanie uprawnieniami,
    - **CredentialsRead** – przeglądanie uprawnień,
    - **Introspection** – przeglądanie historii sesji i generowanie UPO,
    - **SubunitManage** – zarządzanie jednostkami podrzędnymi,
    - **EnforcementOperations** – wykonywanie operacji egzekucyjnych.

    Metoda pozwala na wybór dowolnej kombinacji powyższych uprawnień.
    Uprawnienie **EnforcementOperations** może być nadane wyłącznie wtedy,
    gdy podmiot kontekstu ma rolę **EnforcementAuthority** (organ egzekucyjny)
    lub **CourtBailiff** (komornik sądowy).

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadawanie-
    uprawnie%C5%84-osobom-fizycznym-do-pracy-w-ksef)

    **Wymagane uprawnienia**: `CredentialsManage`.

    Args:
        body (PersonPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, PermissionsOperationResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PersonPermissionsGrantRequest,

) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Nadanie osobom fizycznym uprawnień do pracy w KSeF

     Metoda pozwala na nadanie osobie wskazanej w żądaniu uprawnień do pracy w KSeF
    w kontekście bieżącym.

    W żądaniu określane są nadawane uprawnienia ze zbioru:
    - **InvoiceWrite** – wystawianie faktur,
    - **InvoiceRead** – przeglądanie faktur,
    - **CredentialsManage** – zarządzanie uprawnieniami,
    - **CredentialsRead** – przeglądanie uprawnień,
    - **Introspection** – przeglądanie historii sesji i generowanie UPO,
    - **SubunitManage** – zarządzanie jednostkami podrzędnymi,
    - **EnforcementOperations** – wykonywanie operacji egzekucyjnych.

    Metoda pozwala na wybór dowolnej kombinacji powyższych uprawnień.
    Uprawnienie **EnforcementOperations** może być nadane wyłącznie wtedy,
    gdy podmiot kontekstu ma rolę **EnforcementAuthority** (organ egzekucyjny)
    lub **CourtBailiff** (komornik sądowy).

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadawanie-
    uprawnie%C5%84-osobom-fizycznym-do-pracy-w-ksef)

    **Wymagane uprawnienia**: `CredentialsManage`.

    Args:
        body (PersonPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]
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
    body: PersonPermissionsGrantRequest,

) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Nadanie osobom fizycznym uprawnień do pracy w KSeF

     Metoda pozwala na nadanie osobie wskazanej w żądaniu uprawnień do pracy w KSeF
    w kontekście bieżącym.

    W żądaniu określane są nadawane uprawnienia ze zbioru:
    - **InvoiceWrite** – wystawianie faktur,
    - **InvoiceRead** – przeglądanie faktur,
    - **CredentialsManage** – zarządzanie uprawnieniami,
    - **CredentialsRead** – przeglądanie uprawnień,
    - **Introspection** – przeglądanie historii sesji i generowanie UPO,
    - **SubunitManage** – zarządzanie jednostkami podrzędnymi,
    - **EnforcementOperations** – wykonywanie operacji egzekucyjnych.

    Metoda pozwala na wybór dowolnej kombinacji powyższych uprawnień.
    Uprawnienie **EnforcementOperations** może być nadane wyłącznie wtedy,
    gdy podmiot kontekstu ma rolę **EnforcementAuthority** (organ egzekucyjny)
    lub **CourtBailiff** (komornik sądowy).

    > Więcej informacji:
    > - [Nadawanie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#nadawanie-
    uprawnie%C5%84-osobom-fizycznym-do-pracy-w-ksef)

    **Wymagane uprawnienia**: `CredentialsManage`.

    Args:
        body (PersonPermissionsGrantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, PermissionsOperationResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
