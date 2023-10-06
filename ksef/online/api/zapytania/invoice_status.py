from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.query_invoice_async_status_response import QueryInvoiceAsyncStatusResponse
from ...models.exception_response import ExceptionResponse
from typing import cast
from typing import Dict



def _get_kwargs(
    query_element_reference_number: str,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/online/Query/Invoice/Async/Status/{QueryElementReferenceNumber}".format(QueryElementReferenceNumber=query_element_reference_number,),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryInvoiceAsyncStatusResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ExceptionResponse.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """ Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]
     """


    kwargs = _get_kwargs(
        query_element_reference_number=query_element_reference_number,

    )

    print("*"*20, "/online/Query/Invoice/Async/Status/{QueryElementReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Query/Invoice/Async/Status/{QueryElementReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """ Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]
     """


    return sync_detailed(
        query_element_reference_number=query_element_reference_number,
client=client,

    ).parsed

async def asyncio_detailed(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """ Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]
     """


    kwargs = _get_kwargs(
        query_element_reference_number=query_element_reference_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    query_element_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]]:
    """ Sprawdzenie statusu zapytania o faktury

     Sprawdzenie statusu zapytania o faktury

    Args:
        query_element_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, QueryInvoiceAsyncStatusResponse]
     """


    return (await asyncio_detailed(
        query_element_reference_number=query_element_reference_number,
client=client,

    )).parsed
