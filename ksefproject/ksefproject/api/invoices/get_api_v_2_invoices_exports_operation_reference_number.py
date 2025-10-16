from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.invoice_export_status_response import InvoiceExportStatusResponse
from typing import cast



def _get_kwargs(
    operation_reference_number: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/invoices/exports/{operation_reference_number}".format(operation_reference_number=operation_reference_number,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]:
    if response.status_code == 200:
        response_200 = InvoiceExportStatusResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    operation_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]:
    """ Pobranie statusu eksportu paczki faktur

     

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        operation_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]
     """


    kwargs = _get_kwargs(
        operation_reference_number=operation_reference_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    operation_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]:
    """ Pobranie statusu eksportu paczki faktur

     

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        operation_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, InvoiceExportStatusResponse]
     """


    return sync_detailed(
        operation_reference_number=operation_reference_number,
client=client,

    ).parsed

async def asyncio_detailed(
    operation_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]:
    """ Pobranie statusu eksportu paczki faktur

     

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        operation_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]
     """


    kwargs = _get_kwargs(
        operation_reference_number=operation_reference_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    operation_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, ExceptionResponse, InvoiceExportStatusResponse]]:
    """ Pobranie statusu eksportu paczki faktur

     

    Wymagane uprawnienia: `InvoiceRead`.

    Args:
        operation_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, InvoiceExportStatusResponse]
     """


    return (await asyncio_detailed(
        operation_reference_number=operation_reference_number,
client=client,

    )).parsed
