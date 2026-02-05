from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.query_peppol_providers_response import QueryPeppolProvidersResponse
from ...models.too_many_requests_response import TooManyRequestsResponse
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
        "url": "/peppol/query",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]:
    if response.status_code == 200:
        response_200 = QueryPeppolProvidersResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 429:
        response_429 = TooManyRequestsResponse.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]:
    """ Pobranie listy dostawców usług Peppol

     Zwraca listę dostawców usług Peppol zarejestrowanych w systemie.

    **Sortowanie:**

    - dateCreated (Desc)
    - id (Asc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]
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
    client: Union[AuthenticatedClient, Client],
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]:
    """ Pobranie listy dostawców usług Peppol

     Zwraca listę dostawców usług Peppol zarejestrowanych w systemie.

    **Sortowanie:**

    - dateCreated (Desc)
    - id (Asc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]
     """


    return sync_detailed(
        client=client,
page_offset=page_offset,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]:
    """ Pobranie listy dostawców usług Peppol

     Zwraca listę dostawców usług Peppol zarejestrowanych w systemie.

    **Sortowanie:**

    - dateCreated (Desc)
    - id (Asc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]
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
    client: Union[AuthenticatedClient, Client],
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]]:
    """ Pobranie listy dostawców usług Peppol

     Zwraca listę dostawców usług Peppol zarejestrowanych w systemie.

    **Sortowanie:**

    - dateCreated (Desc)
    - id (Asc)


    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryPeppolProvidersResponse, TooManyRequestsResponse]
     """


    return (await asyncio_detailed(
        client=client,
page_offset=page_offset,
page_size=page_size,

    )).parsed
