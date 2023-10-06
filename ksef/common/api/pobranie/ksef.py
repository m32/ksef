from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ksef_response_200 import KsefResponse200
from ...models.invoice_request_k_se_f import InvoiceRequestKSeF
from typing import Dict
from typing import cast
from ...models.exception_response import ExceptionResponse



def _get_kwargs(
    *,
    json_body: InvoiceRequestKSeF,

) -> Dict[str, Any]:
    

    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/common/Invoice/KSeF",
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, KsefResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KsefResponse200.from_dict(response.content)



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, KsefResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceRequestKSeF,

) -> Response[Union[Any, ExceptionResponse, KsefResponse200]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF

    Args:
        json_body (InvoiceRequestKSeF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, KsefResponse200]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    print("*"*20, "/common/Invoice/KSeF")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//common/Invoice/KSeF")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceRequestKSeF,

) -> Optional[Union[Any, ExceptionResponse, KsefResponse200]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF

    Args:
        json_body (InvoiceRequestKSeF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, KsefResponse200]
     """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceRequestKSeF,

) -> Response[Union[Any, ExceptionResponse, KsefResponse200]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF

    Args:
        json_body (InvoiceRequestKSeF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, KsefResponse200]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceRequestKSeF,

) -> Optional[Union[Any, ExceptionResponse, KsefResponse200]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF

    Args:
        json_body (InvoiceRequestKSeF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, KsefResponse200]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
