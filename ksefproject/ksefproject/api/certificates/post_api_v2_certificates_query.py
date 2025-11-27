from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.query_certificates_request import QueryCertificatesRequest
from ...models.query_certificates_response import QueryCertificatesResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: QueryCertificatesRequest,
    page_size: Union[Unset, int] = 10,
    page_offset: Union[Unset, int] = 0,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageOffset"] = page_offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/certificates/query",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryCertificatesResponse]]:
    if response.status_code == 200:
        response_200 = QueryCertificatesResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryCertificatesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryCertificatesRequest,
    page_size: Union[Unset, int] = 10,
    page_offset: Union[Unset, int] = 0,

) -> Response[Union[Any, ExceptionResponse, QueryCertificatesResponse]]:
    """ Pobranie listy metadanych certyfikatów

     Zwraca listę certyfikatów spełniających podane kryteria wyszukiwania.
    W przypadku braku podania kryteriów wyszukiwania zwrócona zostanie nieprzefiltrowana lista.

    **Sortowanie:**

    - requestDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        page_offset (Union[Unset, int]):  Default: 0.
        body (QueryCertificatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryCertificatesResponse]]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
page_offset=page_offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: QueryCertificatesRequest,
    page_size: Union[Unset, int] = 10,
    page_offset: Union[Unset, int] = 0,

) -> Optional[Union[Any, ExceptionResponse, QueryCertificatesResponse]]:
    """ Pobranie listy metadanych certyfikatów

     Zwraca listę certyfikatów spełniających podane kryteria wyszukiwania.
    W przypadku braku podania kryteriów wyszukiwania zwrócona zostanie nieprzefiltrowana lista.

    **Sortowanie:**

    - requestDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        page_offset (Union[Unset, int]):  Default: 0.
        body (QueryCertificatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryCertificatesResponse]
     """


    return sync_detailed(
        client=client,
body=body,
page_size=page_size,
page_offset=page_offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryCertificatesRequest,
    page_size: Union[Unset, int] = 10,
    page_offset: Union[Unset, int] = 0,

) -> Response[Union[Any, ExceptionResponse, QueryCertificatesResponse]]:
    """ Pobranie listy metadanych certyfikatów

     Zwraca listę certyfikatów spełniających podane kryteria wyszukiwania.
    W przypadku braku podania kryteriów wyszukiwania zwrócona zostanie nieprzefiltrowana lista.

    **Sortowanie:**

    - requestDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        page_offset (Union[Unset, int]):  Default: 0.
        body (QueryCertificatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryCertificatesResponse]]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
page_offset=page_offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: QueryCertificatesRequest,
    page_size: Union[Unset, int] = 10,
    page_offset: Union[Unset, int] = 0,

) -> Optional[Union[Any, ExceptionResponse, QueryCertificatesResponse]]:
    """ Pobranie listy metadanych certyfikatów

     Zwraca listę certyfikatów spełniających podane kryteria wyszukiwania.
    W przypadku braku podania kryteriów wyszukiwania zwrócona zostanie nieprzefiltrowana lista.

    **Sortowanie:**

    - requestDate (Desc)


    Args:
        page_size (Union[Unset, int]):  Default: 10.
        page_offset (Union[Unset, int]):  Default: 0.
        body (QueryCertificatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryCertificatesResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_offset=page_offset,

    )).parsed
