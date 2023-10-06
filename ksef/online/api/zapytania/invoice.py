from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.query_invoice_request import QueryInvoiceRequest
from ...models.query_invoice_sync_response import QueryInvoiceSyncResponse
from ...models.exception_response import ExceptionResponse
from typing import cast



def _get_kwargs(
    *,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,

) -> Dict[str, Any]:
    

    cookies = {}


    params: Dict[str, Any] = {}
    params["PageSize"] = page_size


    params["PageOffset"] = page_offset



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/online/Query/Invoice/Sync",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryInvoiceSyncResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ExceptionResponse.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,

) -> Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """ Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )

    print("*"*20, "/online/Query/Invoice/Sync")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Query/Invoice/Sync")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,

) -> Optional[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """ Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryInvoiceSyncResponse]
     """


    return sync_detailed(
        client=client,
json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,

) -> Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """ Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceSyncResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
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
    json_body: QueryInvoiceRequest,
    page_size: int,
    page_offset: int,

) -> Optional[Union[ExceptionResponse, QueryInvoiceSyncResponse]]:
    """ Zapytanie o faktury

     Zapytanie o faktury

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryInvoiceSyncResponse]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )).parsed
