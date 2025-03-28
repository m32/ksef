from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Union
from typing import Dict
from ...types import UNSET, Unset
from typing import cast
from ...models.query_invoice_async_init_response import QueryInvoiceAsyncInitResponse
from ...models.exception_response import ExceptionResponse
from ...models.query_invoice_request import QueryInvoiceRequest



def _get_kwargs(
    *,
    json_body: QueryInvoiceRequest,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    headers = {}
    if not isinstance(ksef_number_variant, Unset):
        headers["ksef-number-variant"] = ksef_number_variant



    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/online/Query/Invoice/Async/Init",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = QueryInvoiceAsyncInitResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
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
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """ Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        ksef_number_variant (Union[Unset, str]):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
ksef_number_variant=ksef_number_variant,

    )

    print("*"*20, "/online/Query/Invoice/Async/Init")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Query/Invoice/Async/Init")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Optional[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """ Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        ksef_number_variant (Union[Unset, str]):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]
     """


    return sync_detailed(
        client=client,
json_body=json_body,
ksef_number_variant=ksef_number_variant,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """ Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        ksef_number_variant (Union[Unset, str]):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
ksef_number_variant=ksef_number_variant,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: QueryInvoiceRequest,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Optional[Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]]:
    """ Inicjalizacja zapytania o faktury

     Inicjalizacja zapytania o faktury

    Args:
        ksef_number_variant (Union[Unset, str]):
        json_body (QueryInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, QueryInvoiceAsyncInitResponse]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,
ksef_number_variant=ksef_number_variant,

    )).parsed
