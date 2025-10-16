from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.eu_entity_permissions_query_request import EuEntityPermissionsQueryRequest
from ...models.exception_response import ExceptionResponse
from ...models.query_eu_entity_permissions_response import QueryEuEntityPermissionsResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: EuEntityPermissionsQueryRequest,
    page_offset: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["pageOffset"] = page_offset

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/permissions/query/eu-entities/grants",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]:
    if response.status_code == 200:
        response_200 = QueryEuEntityPermissionsResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EuEntityPermissionsQueryRequest,
    page_offset: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,

) -> Response[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]:
    """ Pobranie listy uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania

     Zwraca listę uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania.

    > Więcej informacji:
    > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-administrator%C3%B3w-lub-
    reprezentant%C3%B3w-podmiot%C3%B3w-unijnych-uprawnionych-do-samofakturowania)

    Wymagane uprawnienia: `CredentialsManage`, `CredentialsRead`, `VatUeManage`.

    Args:
        page_offset (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (EuEntityPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]
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
    body: EuEntityPermissionsQueryRequest,
    page_offset: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]:
    """ Pobranie listy uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania

     Zwraca listę uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania.

    > Więcej informacji:
    > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-administrator%C3%B3w-lub-
    reprezentant%C3%B3w-podmiot%C3%B3w-unijnych-uprawnionych-do-samofakturowania)

    Wymagane uprawnienia: `CredentialsManage`, `CredentialsRead`, `VatUeManage`.

    Args:
        page_offset (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (EuEntityPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]
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
    body: EuEntityPermissionsQueryRequest,
    page_offset: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,

) -> Response[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]:
    """ Pobranie listy uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania

     Zwraca listę uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania.

    > Więcej informacji:
    > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-administrator%C3%B3w-lub-
    reprezentant%C3%B3w-podmiot%C3%B3w-unijnych-uprawnionych-do-samofakturowania)

    Wymagane uprawnienia: `CredentialsManage`, `CredentialsRead`, `VatUeManage`.

    Args:
        page_offset (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (EuEntityPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]
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
    body: EuEntityPermissionsQueryRequest,
    page_offset: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]]:
    """ Pobranie listy uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania

     Zwraca listę uprawnień administratorów lub reprezentantów podmiotów unijnych uprawnionych do
    samofakturowania.

    > Więcej informacji:
    > - [Pobieranie listy uprawnień](https://github.com/CIRFMF/ksef-
    docs/blob/main/uprawnienia.md#pobranie-listy-uprawnie%C5%84-administrator%C3%B3w-lub-
    reprezentant%C3%B3w-podmiot%C3%B3w-unijnych-uprawnionych-do-samofakturowania)

    Wymagane uprawnienia: `CredentialsManage`, `CredentialsRead`, `VatUeManage`.

    Args:
        page_offset (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (EuEntityPermissionsQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryEuEntityPermissionsResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_offset=page_offset,
page_size=page_size,

    )).parsed
