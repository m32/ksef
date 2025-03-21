from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.scam_invoice_status_response import ScamInvoiceStatusResponse
from typing import Dict
from typing import cast



def _get_kwargs(
    k_se_f_reference_number: str,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/online/Invoice/Scam/{KSeFReferenceNumber}".format(KSeFReferenceNumber=k_se_f_reference_number,),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, ScamInvoiceStatusResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ScamInvoiceStatusResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, ScamInvoiceStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ExceptionResponse, ScamInvoiceStatusResponse]]:
    """ Pobranie zgłoszenia nadużycia faktury

     Pobranie zgłoszenia nadużycia faktury

    Args:
        k_se_f_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, ScamInvoiceStatusResponse]]
     """


    kwargs = _get_kwargs(
        k_se_f_reference_number=k_se_f_reference_number,

    )

    print("*"*20, "/online/Invoice/Scam/{KSeFReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Invoice/Scam/{KSeFReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ExceptionResponse, ScamInvoiceStatusResponse]]:
    """ Pobranie zgłoszenia nadużycia faktury

     Pobranie zgłoszenia nadużycia faktury

    Args:
        k_se_f_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, ScamInvoiceStatusResponse]
     """


    return sync_detailed(
        k_se_f_reference_number=k_se_f_reference_number,
client=client,

    ).parsed

async def asyncio_detailed(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ExceptionResponse, ScamInvoiceStatusResponse]]:
    """ Pobranie zgłoszenia nadużycia faktury

     Pobranie zgłoszenia nadużycia faktury

    Args:
        k_se_f_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, ScamInvoiceStatusResponse]]
     """


    kwargs = _get_kwargs(
        k_se_f_reference_number=k_se_f_reference_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ExceptionResponse, ScamInvoiceStatusResponse]]:
    """ Pobranie zgłoszenia nadużycia faktury

     Pobranie zgłoszenia nadużycia faktury

    Args:
        k_se_f_reference_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, ScamInvoiceStatusResponse]
     """


    return (await asyncio_detailed(
        k_se_f_reference_number=k_se_f_reference_number,
client=client,

    )).parsed
