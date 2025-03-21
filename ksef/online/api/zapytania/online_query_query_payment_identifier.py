from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.query_payment_request import QueryPaymentRequest
from typing import cast
from ...models.query_payment_identifier_response import QueryPaymentIdentifierResponse
from ...models.exception_response import ExceptionResponse



def _get_kwargs(
    *,
    json_body: QueryPaymentRequest,
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
        "url": "/online/Query/PaymentIdentifier/Sync",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = QueryPaymentIdentifierResponse.from_dict(response.json())



        return response_202
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueryPaymentRequest,
    page_size: int,
    page_offset: int,

) -> Response[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]:
    """ Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

     Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )

    print("*"*20, "/online/Query/PaymentIdentifier/Sync")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Query/PaymentIdentifier/Sync")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    json_body: QueryPaymentRequest,
    page_size: int,
    page_offset: int,

) -> Optional[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]:
    """ Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

     Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryPaymentIdentifierResponse]
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
    json_body: QueryPaymentRequest,
    page_size: int,
    page_offset: int,

) -> Response[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]:
    """ Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

     Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]
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
    json_body: QueryPaymentRequest,
    page_size: int,
    page_offset: int,

) -> Optional[Union[ExceptionResponse, QueryPaymentIdentifierResponse]]:
    """ Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

     Uzyskanie listy identyfikatorów zbiorczych wygenerowanych w podanym kontekście

    Args:
        page_size (int):
        page_offset (int):
        json_body (QueryPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryPaymentIdentifierResponse]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,
page_size=page_size,
page_offset=page_offset,

    )).parsed
