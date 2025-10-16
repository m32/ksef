from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.invoice_query_filters import InvoiceQueryFilters
from ...models.query_invoices_metadata_response import QueryInvoicesMetadataResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: InvoiceQueryFilters,
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
        "url": "/api/v2/invoices/query/metadata",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]:
    if response.status_code == 200:
        response_200 = QueryInvoicesMetadataResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InvoiceQueryFilters,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]:
    """ Pobranie listy metadanych faktur

     Zwraca listę metadanych faktur spełniające podane kryteria wyszukiwania. Wyniki sortowane są rosnąco
    według typu daty przekazanej w `DateRange`. Do realizacji pobierania przyrostowego należy stosować
    typ `PermanentStorage`. Maksymalnie można pobrać faktury w zakresie do 10 000 rekordów

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (InvoiceQueryFilters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]
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
    body: InvoiceQueryFilters,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]:
    """ Pobranie listy metadanych faktur

     Zwraca listę metadanych faktur spełniające podane kryteria wyszukiwania. Wyniki sortowane są rosnąco
    według typu daty przekazanej w `DateRange`. Do realizacji pobierania przyrostowego należy stosować
    typ `PermanentStorage`. Maksymalnie można pobrać faktury w zakresie do 10 000 rekordów

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (InvoiceQueryFilters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]
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
    body: InvoiceQueryFilters,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Response[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]:
    """ Pobranie listy metadanych faktur

     Zwraca listę metadanych faktur spełniające podane kryteria wyszukiwania. Wyniki sortowane są rosnąco
    według typu daty przekazanej w `DateRange`. Do realizacji pobierania przyrostowego należy stosować
    typ `PermanentStorage`. Maksymalnie można pobrać faktury w zakresie do 10 000 rekordów

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (InvoiceQueryFilters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]
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
    body: InvoiceQueryFilters,
    page_offset: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 10,

) -> Optional[Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]]:
    """ Pobranie listy metadanych faktur

     Zwraca listę metadanych faktur spełniające podane kryteria wyszukiwania. Wyniki sortowane są rosnąco
    według typu daty przekazanej w `DateRange`. Do realizacji pobierania przyrostowego należy stosować
    typ `PermanentStorage`. Maksymalnie można pobrać faktury w zakresie do 10 000 rekordów

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        page_offset (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 10.
        body (InvoiceQueryFilters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryInvoicesMetadataResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_offset=page_offset,
page_size=page_size,

    )).parsed
