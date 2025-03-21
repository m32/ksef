from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from typing import cast
from ...models.exception_response import ExceptionResponse
from ...models.common_invoice_download_response_200 import CommonInvoiceDownloadResponse200
from ...models.invoice_download_request import InvoiceDownloadRequest



def _get_kwargs(
    ksef_reference_number: str,
    *,
    json_body: InvoiceDownloadRequest,

) -> Dict[str, Any]:
    

    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/common/download/{KsefReferenceNumber}".format(KsefReferenceNumber=ksef_reference_number,),
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CommonInvoiceDownloadResponse200.from_dict(response.content)



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceDownloadRequest,

) -> Response[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF i skrót dokumentu

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF i skrót dokumentu

    Args:
        ksef_reference_number (str):
        json_body (InvoiceDownloadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        ksef_reference_number=ksef_reference_number,
json_body=json_body,

    )

    print("*"*20, "/common/download/{KsefReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//common/download/{KsefReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceDownloadRequest,

) -> Optional[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF i skrót dokumentu

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF i skrót dokumentu

    Args:
        ksef_reference_number (str):
        json_body (InvoiceDownloadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]
     """


    return sync_detailed(
        ksef_reference_number=ksef_reference_number,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceDownloadRequest,

) -> Response[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF i skrót dokumentu

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF i skrót dokumentu

    Args:
        ksef_reference_number (str):
        json_body (InvoiceDownloadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        ksef_reference_number=ksef_reference_number,
json_body=json_body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ksef_reference_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: InvoiceDownloadRequest,

) -> Optional[Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]]:
    """ Pobranie faktury z repozytorium KSeF - kryteria oparte o numer KSeF i skrót dokumentu

     Pobranie faktury z repozytorium KSeF na podstawie kryteriów opartych o numer KSeF i skrót dokumentu

    Args:
        ksef_reference_number (str):
        json_body (InvoiceDownloadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CommonInvoiceDownloadResponse200, ExceptionResponse]
     """


    return (await asyncio_detailed(
        ksef_reference_number=ksef_reference_number,
client=client,
json_body=json_body,

    )).parsed
