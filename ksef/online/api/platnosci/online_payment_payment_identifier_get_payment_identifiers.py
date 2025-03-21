from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from typing import Dict
from ...models.get_payment_identifiers_by_k_se_f_number_response import GetPaymentIdentifiersByKSeFNumberResponse
from typing import cast



def _get_kwargs(
    k_se_f_reference_number: str,
    *,
    page_size: int,
    page_offset: int,

) -> Dict[str, Any]:
    

    cookies = {}


    params: Dict[str, Any] = {}
    params["PageSize"] = page_size


    params["PageOffset"] = page_offset



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/online/Payment/Identifier/GetPaymentIdentifiers/{KSeFReferenceNumber}".format(KSeFReferenceNumber=k_se_f_reference_number,),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPaymentIdentifiersByKSeFNumberResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]:
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
    page_size: int,
    page_offset: int,

) -> Response[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]:
    """ Pobranie listy identyfikatorów płatności dla faktury

     Pobranie listy identyfikatorów płatności dla faktury

    Args:
        k_se_f_reference_number (str):
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]
     """


    kwargs = _get_kwargs(
        k_se_f_reference_number=k_se_f_reference_number,
page_size=page_size,
page_offset=page_offset,

    )

    print("*"*20, "/online/Payment/Identifier/GetPaymentIdentifiers/{KSeFReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Payment/Identifier/GetPaymentIdentifiers/{KSeFReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,

) -> Optional[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]:
    """ Pobranie listy identyfikatorów płatności dla faktury

     Pobranie listy identyfikatorów płatności dla faktury

    Args:
        k_se_f_reference_number (str):
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]
     """


    return sync_detailed(
        k_se_f_reference_number=k_se_f_reference_number,
client=client,
page_size=page_size,
page_offset=page_offset,

    ).parsed

async def asyncio_detailed(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,

) -> Response[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]:
    """ Pobranie listy identyfikatorów płatności dla faktury

     Pobranie listy identyfikatorów płatności dla faktury

    Args:
        k_se_f_reference_number (str):
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]
     """


    kwargs = _get_kwargs(
        k_se_f_reference_number=k_se_f_reference_number,
page_size=page_size,
page_offset=page_offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    k_se_f_reference_number: str,
    *,
    client: AuthenticatedClient,
    page_size: int,
    page_offset: int,

) -> Optional[Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]]:
    """ Pobranie listy identyfikatorów płatności dla faktury

     Pobranie listy identyfikatorów płatności dla faktury

    Args:
        k_se_f_reference_number (str):
        page_size (int):
        page_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, GetPaymentIdentifiersByKSeFNumberResponse]
     """


    return (await asyncio_detailed(
        k_se_f_reference_number=k_se_f_reference_number,
client=client,
page_size=page_size,
page_offset=page_offset,

    )).parsed
