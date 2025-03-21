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
from ...models.exception_response import ExceptionResponse
from ...models.visibility_invoice_status_response import VisibilityInvoiceStatusResponse



def _get_kwargs(
    hiding_element_reference_number: str,
    *,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    headers = {}
    if not isinstance(ksef_number_variant, Unset):
        headers["ksef-number-variant"] = ksef_number_variant



    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/online/Invoice/Visibility/Status/{HidingElementReferenceNumber}".format(HidingElementReferenceNumber=hiding_element_reference_number,),
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VisibilityInvoiceStatusResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hiding_element_reference_number: str,
    *,
    client: AuthenticatedClient,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]:
    """ Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

     Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

    Args:
        hiding_element_reference_number (str):
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]
     """


    kwargs = _get_kwargs(
        hiding_element_reference_number=hiding_element_reference_number,
ksef_number_variant=ksef_number_variant,

    )

    print("*"*20, "/online/Invoice/Visibility/Status/{HidingElementReferenceNumber}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Invoice/Visibility/Status/{HidingElementReferenceNumber}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    hiding_element_reference_number: str,
    *,
    client: AuthenticatedClient,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]:
    """ Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

     Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

    Args:
        hiding_element_reference_number (str):
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]
     """


    return sync_detailed(
        hiding_element_reference_number=hiding_element_reference_number,
client=client,
ksef_number_variant=ksef_number_variant,

    ).parsed

async def asyncio_detailed(
    hiding_element_reference_number: str,
    *,
    client: AuthenticatedClient,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]:
    """ Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

     Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

    Args:
        hiding_element_reference_number (str):
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]
     """


    kwargs = _get_kwargs(
        hiding_element_reference_number=hiding_element_reference_number,
ksef_number_variant=ksef_number_variant,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    hiding_element_reference_number: str,
    *,
    client: AuthenticatedClient,
    ksef_number_variant: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]]:
    """ Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

     Sprawdzenie statusu operacji ukrycia/odsłonienia faktury

    Args:
        hiding_element_reference_number (str):
        ksef_number_variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, VisibilityInvoiceStatusResponse]
     """


    return (await asyncio_detailed(
        hiding_element_reference_number=hiding_element_reference_number,
client=client,
ksef_number_variant=ksef_number_variant,

    )).parsed
